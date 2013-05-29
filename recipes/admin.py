from django.contrib import admin
from .models import Recipe, Ingredient, RecipeIngredient
from core.admin import activate, deactivate

class IngredientInline(admin.TabularInline):
    model = RecipeIngredient

class RecipeAdmin(admin.ModelAdmin):
    actions = [activate, deactivate]
    list_display = ['title', 'author', 'active', 'created']
    search_fields = ['title', 'author', 'content']
    inlines = [IngredientInline,]

    def get_form(self, request, obj=None, **kwargs):
        self.exclude = []
        if not request.user.is_superuser:
            self.exclude.append('slug')
        return super(RecipeAdmin, self).get_form(request, obj, **kwargs)

admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredient)