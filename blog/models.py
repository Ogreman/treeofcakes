from django.db import models
from django.contrib.auth.models import User, Group

from .constants import *

from core.models import TimeStampedModel
from core.helper_shortcuts import short_slugify

class Content(TimeStampedModel):

    title = models.CharField(max_length=MAX_TITLE_LENGTH)
    author = models.ForeignKey(User, blank=True, null=True, limit_choices_to=models.Q(groups__name='Authors'), related_name='%(class)s_publications')
    slug = models.CharField(max_length=MAX_SLUG_LENGTH, unique=True, help_text="This is the URL safe name to be used in the URL.", blank=True, null=True)
    active = models.BooleanField("Active/visible content?", editable=True, default=False)

    def save(self, *args, **kwargs):
        self.slug = short_slugify(self.title)
        super(Content, self).save(*args, **kwargs)

    class Meta:
        abstract = True
        ordering = ['-created']
        get_latest_by = "created"


class Post(Content):

    content = models.TextField()

    class Meta(Content.Meta):
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'