from django.db import models


# Create your models here.
class Ingredient(models.Model):
    ingredient_name = models.CharField(max_length=25)
    price = models.FloatField()
    kcal = models.IntegerField()
    quantity = models.FloatField()
    if_vegan = models.BooleanField(default=False)
    recipe_step = models.ForeignKey('RecipeStep', on_delete=models.CASCADE)

    def __str__(self):
        return self.ingredient_name


class RecipeStep(models.Model):
    description = models.CharField(max_length=200)
    time = models.IntegerField(default=0)
    recipe = models.ForeignKey('Recipe', on_delete=models.CASCADE)

    def __str__(self):
        return self.description


class Recipe(models.Model):
    dish_name = models.CharField(max_length=25)
    average_time = models.IntegerField()
    average_price = models.IntegerField()
    difficulty = models.CharField(
        choices=[("E", "Easy"), ("M", "Medium"), ("H", "High")],
        default="Medium",
        max_length=10
    )

    def __str__(self):
        return self.dish_name
