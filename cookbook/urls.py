from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('recipe', views.getAllRecipes, name='getAllRecipes'),
    path('recipestep', views.getAllRecipeSteps, name='getAllRecipe'),
    path('ingredient',views.getAllIngredientes, name = 'getAllIngredientes'),
    path('addingredient', views.addIngredient, name='addIngredient')

]