from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .forms import ProjectForm
from .models import Project


# Create your views here.
def portfolio(request):
    portfolio = Project.objects.all()
    context = {
        'portfolio': portfolio,
    }
    return render(request, 'projects/portfolio.html', context)


def portfolio_management(request):
    form = ProjectForm()
    portfolio = Project.objects.all()
    
    if request.method == 'POST':
        print(request.FILES)
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            print(request.FILES['featured_video'])
            project = form.save(commit=False)
            # if 'featured_video' in request.FILES:
            #     project.featured_video = request.FILES['featured_video']
            #     content_type = project.featured_video.content_type
            project.save()
            return redirect('portfolio')

    context = {
        'form': form,
        'portfolio': portfolio,
    }

    return render(request, 'projects/portfolio-management.html', context)


# @login_required(login_url="login")
def delete_project(request, pk):
    # profile = request.user.profile
    project = Project.objects.get(id=pk)
    if request.method == 'POST':
        project.delete()
        return redirect('portfolio-management')
    context = {'object': project}
    return render(request, 'delete-confirmation.html', context)
