from django.conf.urls import patterns, include, url

from .views import RecipeDetailView, RecipeListView, RecipeVoteView

urlpatterns = patterns('',
    url(
        regex=r"^(?P<slug>[\w-]+)/$",
        view=RecipeDetailView.as_view(),
        name="recipe_detail"
    ),
    url(
        regex=r"^vote/(?P<pk>\d+)/$",
        view=RecipeVoteView.as_view(),
        name="recipe_vote"
    ),
    url(
        regex=r"^$",
        view=RecipeListView.as_view(),
        name="post_list"
    ),
)
