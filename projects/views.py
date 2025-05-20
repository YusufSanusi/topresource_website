from django.shortcuts import render, redirect

from .forms import ProjectForm
from .models import Project


# Create your views here.
def portfolio(request):
    projects = Project.objects.all()
    context = {
        'projects': projects,
    }
    return render(request, 'projects/portfolio.html', context)


def portfolio_management(request):
    form = ProjectForm()
    projects = Project.objects.all()
    
    if request.method == 'POST':
        print(request.FILES)
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            if 'featured_video' in request.FILES:
                project.featured_video = request.FILES['featured_video']
                content_type = project.featured_video.content_type
            project.save()
            return redirect('portfolio')

    context = {
        'form': form,
        'projects': projects,
    }

    return render(request, 'projects/portfolio-management.html', context)
