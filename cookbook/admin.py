from django.contrib import admin

from .models import Ingredient, RecipeStep, Recipe

# todo rozbudowac to troszku

admin.site.register(Ingredient)
admin.site.register(RecipeStep)
admin.site.register(Recipe)

