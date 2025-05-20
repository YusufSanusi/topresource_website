from django.contrib import admin
from .models import Project, ProjectType

# Register your models here.
class ProjectAdmin(admin.ModelAdmin):
    fields = ['title', 'client', 'project_date', 'description', 'featured_video', 'project_type']


class ProjectTypeAdmin(admin.ModelAdmin):
    fields = ['name']


class VideoAdmin(admin.ModelAdmin):
    fields = ['title', 'video_file', 'thumbnail', 'created']


admin.site.register(Project, ProjectAdmin)
admin.site.register(ProjectType, ProjectTypeAdmin)
