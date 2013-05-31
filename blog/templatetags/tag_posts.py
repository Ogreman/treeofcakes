from django import template

from blog.models import Post

register = template.Library()

@register.inclusion_tag('includes/side-new-posts.html')
def side_new_posts():
    return {
        'new_posts': Post.objects.are_active()
    }
