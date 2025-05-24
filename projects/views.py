from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.contrib.auth.decorators import login_required

from .forms import ProjectForm
from .models import Project
import os


# Create your views here.
class Portfolio(ListView):
    model = Project
    template_name = 'projects/portfolio.html'
    context_object_name = 'portfolio'
    paginate_by = 10

    def get_queryset(self):
        return super().get_queryset().order_by('-created')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        left_index = (int(context['page_obj'].number) - 2)
        right_index = (int(context['paginator'].num_pages) + 2)

        if left_index < 1:
            left_index = 1

        if right_index > int(context['paginator'].num_pages):
            right_index = int(context['paginator'].num_pages) + 1

        context['custom_range'] = range(left_index, right_index)
        
        return context



class ProjectDetail(DetailView):
    model = Project
    template_name = 'projects/portfolio-detail.html'
    context_object_name = 'project'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     return context


def project_example(request, pk):
    project = Project.objects.get(id=pk)
    context = {
        'project': project,
    }
    return render(request, 'projects/portfolio-detail.html', context)


class PortfolioManagement(ListView):
    model = Project
    form_class = ProjectForm
    template_name = 'projects/portfolio-management.html'
    context_object_name = 'portfolio'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ProjectForm()
        return context
    
    def post(self, request, *args, **kwargs):
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('portfolio')
        
        # If form is invalid, re-render page with errors
        context = self.get_context_data(**kwargs)
        context['form'] = form
        return self.render_to_response(context)


# @login_required(login_url="login")
def delete_project(request, pk):
    # profile = request.user.profile
    project = Project.objects.get(id=pk)
    if request.method == 'POST':
        project.delete()
        return redirect('portfolio-management')
    context = {'object': project}
    return render(request, 'delete-confirmation.html', context)
