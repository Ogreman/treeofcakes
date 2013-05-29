from django.db import models
from django.core.urlresolvers import reverse

from core.models import Content

from .constants import *


class Ingredient(models.Model):

    name = models.CharField(max_length=MAX_INGREDIENT_LENGTH)
    description = models.TextField()

    def __unicode__(self):
        return self.name


class Recipe(Content):

    ingredients = models.ManyToManyField(Ingredient, through='RecipeIngredient', null=True, blank=True)
    content = models.TextField()

    def get_absolute_url(self):
        return reverse("recipe_detail", kwargs={"slug": self.slug})

    class Meta(Content.Meta):
        verbose_name = 'Recipe'
        verbose_name_plural = 'Recipes'


class RecipeIngredient(models.Model):

    recipe = models.ForeignKey(Recipe)
    ingredient = models.ForeignKey(Ingredient)
    amount = models.DecimalField(max_digits=MAX_RECIPEINGREDIENT_DIGITS, decimal_places=MAX_RECIPEINGREDIENT_DECIMALS)
    unit = models.CharField(max_length=25, choices=UNIT_CHOICES)

