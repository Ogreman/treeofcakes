from django.views.generic import DetailView, ListView

from .models import Recipe


class RecipeDetailView(DetailView):

    model = Recipe
    template_name = "recipe-single.html"

    def get_context_data(self, **kwargs):
        context = super(RecipeDetailView, self).get_context_data(**kwargs)
        context['ingredients'] = context.get('object').ingredient_set.all()
        return context
        
class RecipeListView(ListView):

    model = Recipe
    template_name = "recipe-list.html"

    def get_queryset(self):
        return super(RecipeListView, self).get_queryset().are_active()
