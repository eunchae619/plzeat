from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.Recipe)
class RecipeAdmin(admin.ModelAdmin):
    filter_horizontal = ("food",)


@admin.register(models.FoodInRecipe)
class FoodInRecipeAdmin(admin.ModelAdmin):
    pass
