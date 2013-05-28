from django.conf.urls import patterns, include, url

from .views import PostDetailView, PostListView

urlpatterns = patterns('',
    url(
        regex=r"^(?P<slug>[\w-]+)/$",
        view=PostDetailView.as_view(),
        name="post_detail"
    ),
    url(
        regex=r"^$",
        view=PostListView.as_view(),
        name="post_list"
    ),
)
