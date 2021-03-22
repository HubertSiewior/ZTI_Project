from django.contrib import admin

from .models import Ingredient, RecipeStep, Recipe


class IngredientsInLine(admin.TabularInline):
    model = Ingredient
    extra = 2


class RecipeStepsInLine(admin.TabularInline):
    model = RecipeStep
    extra = 2


class RecipeStepAdmin(admin.ModelAdmin):
    inlines = [IngredientsInLine]


class RecipeAdmin(admin.ModelAdmin):
    inlines = [RecipeStepsInLine]


admin.site.register(Ingredient)
admin.site.register(RecipeStep, RecipeStepAdmin)
admin.site.register(Recipe, RecipeAdmin)
