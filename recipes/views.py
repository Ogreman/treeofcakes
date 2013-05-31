from django.views.generic import View, ListView, DetailView
from django.views.generic.detail import SingleObjectMixin
from django.db import IntegrityError

from .models import Recipe, RecipeVote
from core.views import JSONResponseMixin

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

class RecipeVoteView(JSONResponseMixin, SingleObjectMixin, View):
    
    model = Recipe

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        try:
            RecipeVote(
                    recipe=self.object,
                    ip=request.META['REMOTE_ADDR'],
                    session=request.session.session_key
                ).save()
            context = { 'voted': True, 'votes': self.object.count_votes() }
        except IntegrityError:
            context = { 'voted': False }
        return self.render_to_response(context)

