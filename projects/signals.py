from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import Project


def createThumbnail(sender, instance, **kwargs):
    pass
