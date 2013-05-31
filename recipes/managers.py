from django.db import models
from django.db.models import Count
from core.managers import ContentQuerySet, ContentManager

class RecipeQuerySet(ContentQuerySet):

    def with_votes(self):
        return self.annotate(vote_count=Count('votes'))

    def order_by_votes(self):
        return self.with_votes().order_by('-vote_count')

class RecipeManager(ContentManager):

    def get_query_set(self):
        return RecipeQuerySet(self.model, using=self._db)

    def with_votes(self):
        return self.get_query_set().with_votes()

    def order_by_votes(self):
        return self.get_query_set().order_by_votes()