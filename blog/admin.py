from django.contrib import admin
from .models import Post

def activate(modeladmin, request, queryset):
    """Activates multiple rows at once
    """
    rows_updated = queryset.update(active=True)
    if rows_updated == 1:
        count_bit = "1 row was"
    else:
        count_bit = "%s rows were" % rows_updated
    modeladmin.message_user(request, "%s successfully activated." % count_bit)

def deactivate(modeladmin, request, queryset):
    """Dectivates multiple rows at once
    """
    rows_updated = queryset.update(active=False)
    if rows_updated == 1:
        count_bit = "1 row was"
    else:
        count_bit = "%s rows were"
    modeladmin.message_user(request, "%s successfully deactivated." % count_bit)

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