from django.contrib import admin

# Register your models here.

from .models import Category, Recipe


class CategoryAdmin(admin.ModelAdmin):
    ...

class RecipeAdmin(admin.ModelAdmin):
    ...

admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Category, CategoryAdmin)
