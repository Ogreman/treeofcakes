from django.views.generic import DetailView, ListView

from .models import Recipe


class RecipeDetailView(DetailView):

    model = Recipe
    template_name = "recipe-single.html"

class RecipeListView(ListView):

    model = Recipe
    template_name = "recipe-list.html"

    def get_queryset(self):
        return super(RecipeListView, self).get_queryset().are_active()
