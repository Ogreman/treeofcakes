from django.db import models
from django.core.urlresolvers import reverse

from core.models import Content, TimeStampedModel

from .constants import *
from .managers import RecipeManager


class Ingredient(models.Model):

    name = models.CharField(max_length=MAX_INGREDIENT_LENGTH)
    description = models.TextField(blank=True)

    def __unicode__(self):
        return self.name


class Recipe(Content):

    ingredients = models.ManyToManyField(Ingredient, through='RecipeIngredient', null=True, blank=True)

    objects = RecipeManager()

    def vote_link(self):
        return reverse("recipe_vote", kwargs={"pk": self.id})

    def get_absolute_url(self):
        return reverse("recipe_detail", kwargs={"slug": self.slug})

    def count_votes(self):
        return self.votes.count()

    class Meta(Content.Meta):
        verbose_name = 'Recipe'
        verbose_name_plural = 'Recipes'


class RecipeIngredient(models.Model):

    recipe = models.ForeignKey(Recipe, related_name="ingredient_set")
    ingredient = models.ForeignKey(Ingredient)
    amount = models.DecimalField(max_digits=MAX_RECIPEINGREDIENT_DIGITS, decimal_places=MAX_RECIPEINGREDIENT_DECIMALS)
    unit = models.CharField(max_length=25, choices=UNIT_CHOICES)

    def __unicode__(self):
        return self.ingredient.name


class RecipeVote(TimeStampedModel):

    recipe = models.ForeignKey(Recipe, related_name="votes")
    ip = models.CharField(max_length=40)
    session = models.CharField(max_length=2048)

    class Meta:
        unique_together = ("recipe", "session")
