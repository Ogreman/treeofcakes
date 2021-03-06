from django.contrib import admin
from .models import Post
from core.admin import activate, deactivate

class PostAdmin(admin.ModelAdmin):
    actions = [activate, deactivate]
    list_display = ['title', 'author', 'active', 'created']
    search_fields = ['title', 'author', 'content']

    def get_form(self, request, obj=None, **kwargs):
        self.exclude = []
        if not request.user.is_superuser:
            self.exclude.append('slug')
        return super(PostAdmin, self).get_form(request, obj, **kwargs)

admin.site.register(Post, PostAdmin)