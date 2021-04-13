from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from .models import Recipe, RecipeStep, Ingredient
from django.shortcuts import get_object_or_404, render
from django.forms.models import model_to_dict
import numpy as np
import json

def index(request):
    return HttpResponse("Hello, world.")
# todo wszystko https://docs.djangoproject.com/pl/3.1/intro/tutorial03/
def getAllRecipes(request):
    return HttpResponse(Recipe.objects.all().values())

def getAllRecipeSteps(request):
    return HttpResponse(RecipeStep.objects.all().values())

def getAllIngredientes(request):
    return HttpResponse(Ingredient.objects.all().values())

def addIngredient(request):
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)

    ingredient = Ingredient(
        ingredient_name= body['ingredient_name'],
        price= body['price'],
        kcal= body['kcal'],
        quantity=body['quantity'],
        if_vegan=body['if_vegan']
    )
    ingredient.save()
    return JsonResponse(ingredient)