from django.conf.urls import patterns, include, url

from .views import RecipeDetailView, RecipeListView

urlpatterns = patterns('',
    url(
        regex=r"^(?P<slug>[\w-]+)/$",
        view=RecipeDetailView.as_view(),
        name="recipe_detail"
    ),
    url(
        regex=r"^$",
        view=RecipeListView.as_view(),
        name="post_list"
    ),
)
