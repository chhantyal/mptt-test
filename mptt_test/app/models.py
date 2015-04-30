from django.db import models

from mptt.models import MPTTModel, TreeForeignKey
from mptt.managers import TreeManager


class ResourceAbstract(MPTTModel):
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children', on_delete=models.SET_NULL)
    content_type = models.SlugField(editable=False)

    title = models.CharField(max_length=100)

    objects = tree = TreeManager()

    class Meta:
    	abstract = True


class Page(ResourceAbstract):
	body = models.TextField(blank=True)


def get_page_fields():
	return Page._meta.get_fields()
