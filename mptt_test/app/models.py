from django.db import models

from mptt.models import MPTTModel, TreeForeignKey
from mptt.managers import TreeManager
from model_utils.managers import InheritanceManager


class ResourceAbstract(MPTTModel):
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children', on_delete=models.SET_NULL)
    content_type = models.SlugField(editable=False)

    title = models.CharField(max_length=100)

    objects = tree = TreeManager()

    class Meta:
        abstract = True


class Page(ResourceAbstract):
    body = models.TextField(blank=True)


class PageProxy(Page):

    objects = InheritanceManager()

    class Meta:
        proxy = True


class Blog(PageProxy):
    quote = models.CharField(max_length=255)
