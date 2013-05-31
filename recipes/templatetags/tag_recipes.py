from django import template

from recipes.models import Recipe

register = template.Library()

@register.inclusion_tag('includes/side-top-recipes.html')
def side_top_recipes():
    return {
        'top_recipes': Recipe.objects.are_active().order_by_votes()
    }
