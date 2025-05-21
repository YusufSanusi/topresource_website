import os
from django.db import models
from thumbnails.fields import ImageField
from easy_thumbnails.fields import ThumbnailerImageField
from django.urls import reverse
from django.core.exceptions import ValidationError
from .processors import VideoThumbnailProcessor
import uuid
import magic


def validate_video_file(value):
    """
    Validate that the uploaded file is a video file.
    """
    ext = os.path.splitext(value.name)[1].lower()
    valid_extensions = ['.mp4', '.mov', '.avi', '.wmv', '.flv', '.mkv', '.webm']
    
    if not ext in valid_extensions:
        raise ValidationError(f'Unsupported file extension. Allowed extensions are: {", ".join(valid_extensions)}')
    
    # Check the file's MIME type
    # You can also use python-magic for more robust MIME type checking
    mime = magic.Magic(mime=True)
    mime_type = mime.from_buffer(value.read())
    if not mime_type.startswith('video/'):
        raise ValidationError('Uploaded file is not a valid video.')
    

# class Video(models.Model):
#     title = models.CharField(max_length=200)
#     # Use Django 5.2 storage dictionary format and add video validation
#     video_file = models.FileField(
#         upload_to='videos/',
#         validators=[validate_video_file],
#         help_text="Upload video files only (MP4, MOV, AVI, etc.)"
#     )
#     # For the thumbnail field, django-thumbnails will use the storage specified in settings
#     thumbnail = ImageField(blank=True, null=True, upload_to='thumbnails/')
#     created = models.DateTimeField(auto_now_add=True)
    
#     def __str__(self):
#         return self.title
    
#     def get_absolute_url(self):
#         return reverse('video_detail', args=[str(self.id)])
    
#     def save(self, *args, **kwargs):
#         """Generate thumbnail when the video is saved"""
#         is_new = self.pk is None
#         super().save(*args, **kwargs)
        
#         # Generate thumbnail on new uploads
#         if is_new and self.video_file:
#             self.thumbnail.generate_for_sizes(['small', 'medium', 'large'])
#             # Save again to update the thumbnail field in the database
#             super().save(update_fields=['thumbnail'])


# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200)
    client = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    featured_video = models.FileField(
        upload_to='videos/',
        validators=[validate_video_file],
        help_text="Upload video files only (MP4, MOV, AVI, etc.)",
        default='videos/default-video.mp4',
    )
    thumbnail = ThumbnailerImageField(blank=True, null=True, upload_to='thumbnails/', default='thumbnails/default-video.png')
    project_type = models.ForeignKey('ProjectType', null=True, blank=True, on_delete=models.SET_NULL)
    project_date = models.DateField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created']

    def save(self, *args, **kwargs):
        """Generate thumbnail when the video is saved"""
        is_new = self.pk is None
        super().save(*args, **kwargs)
        
        # Generate thumbnail on new uploads
        if is_new and self.featured_video:
            try:
                self.thumbnail = VideoThumbnailProcessor().process(self.featured_video, width=320, height=240, time=2.5, quality=80)
                # Save again to update the thumbnail field in the database
                super().save(update_fields=['thumbnail'])
            except Exception as e:
                print(f"Error generating thumbnail: {e}")
                # Optionally, you can set a default thumbnail or handle the error as needed
                self.thumbnail = 'thumbnails/default-video.png'
                super().save(update_fields=['thumbnail'])

    @property
    def videoURL(self):
        try:
            url = self.featured_video.url
        except:
            url = ''
        return url
    
    @property
    def thumbnailURL(self):
        try:
            url = self.thumbnail.url
        except:
            url = ''
        return url


class ProjectType(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['created']
