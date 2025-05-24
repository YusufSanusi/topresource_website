import os
from django.db import models
from easy_thumbnails.fields import ThumbnailerImageField
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
    
    # Check the file's MIME type using python-magic for more robust MIME type checking
    mime = magic.Magic(mime=True)
    mime_type = mime.from_buffer(value.read())
    if not mime_type.startswith('video/'):
        raise ValidationError('Uploaded file is not a valid video.')


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
    date = models.DateField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created']

    def save(self, *args, **kwargs):
        """Generate thumbnail when the video is saved"""
        # generating_thumbnail = self.pk is None
        # super().save(*args, **kwargs)
        if self.featured_video:
            video_extension = os.path.splitext(self.featured_video.name)[1].lower()
            self.featured_video.name = f'video_{self.title}{video_extension}'.lower()

        # Check if video is being updated or is new
        generating_thumbnail = False
        if self.featured_video and (not self.pk or 'featured_video' in kwargs.get('update_fields', [])):
            generating_thumbnail = True

        super().save(*args, **kwargs)

        thumbnail_processor = VideoThumbnailProcessor(self.featured_video)
        temp_thumbnail = thumbnail_processor.process(width=1280, height=720)

        self.thumbnail.save(f"thumbnail_{self.title}.webp".lower(), temp_thumbnail, save=False)

        # Save again to update the thumbnail field in the database
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
