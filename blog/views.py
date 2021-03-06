from django.views.generic import DetailView, ListView

from braces.views import LoginRequiredMixin

from .models import Post


class PostDetailView(DetailView):

    model = Post
    template_name = "post-single.html"

class PostListView(ListView):

    model = Post
    template_name = "post-list.html"

    def get_queryset(self):
        return super(PostListView, self).get_queryset().are_active()
        