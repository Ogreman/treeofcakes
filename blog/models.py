from django.db import models
from django.core.urlresolvers import reverse

from core.models import Content


class Post(Content):

    content = models.TextField()

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"slug": self.slug})

    class Meta(Content.Meta):
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'