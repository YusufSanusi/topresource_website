from django.forms import ModelForm, Textarea, Select, TextInput, DateInput
from .models import Project, ProjectType


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'client', 'project_date', 'description', 'featured_video', 'project_type']
        widgets = {
            'title': TextInput(attrs={'id': 'title'}),
            'client': TextInput(attrs={'id': 'client'}),
            'project_date': DateInput(attrs={'id': 'project_date'}),
            'description': Textarea(attrs={'rows': 4, 'id': 'description'}),
            'project_type': Select(attrs={'id': 'project_type'}, choices=ProjectType.objects.all()),
        }
        labels = {
            'title': 'Project Title',
            'client': 'Client',
            'description': 'Project Description',
            'featured_video': 'Upload Video',
            'project_type': 'Project Type',
        }
        help_texts = {
            'title': 'Enter the title of the project.',
            'client': 'Enter the name of the client.',
            'description': 'Provide a brief description of the project.',
            'featured_video': 'Upload a video file (MP4, MOV, AVI, etc.).',
            'project_type': 'Select relevant the project type.',
        }

    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})

        
