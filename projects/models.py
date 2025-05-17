from django.db import models
import uuid


# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    featured_video = models.FileField(
        null=True, blank=True, default="default.mp4")
    thumbnail = models.ImageField(
        null=True, blank=True, default="default.jpg")
    tags = models.ForeignKey('Tag', null=True, blank=True, on_delete=models.SET_NULL)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']

    @property
    def videoURL(self):
        try:
            url = self.featured_video.url
        except:
            url = ''
        return url

    @property
    def imageURL(self):
        try:
            url = self.thumbnail.url
        except:
            url = ''
        return url


class Tag(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return self.name
