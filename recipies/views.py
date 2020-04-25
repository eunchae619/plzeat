from django.shortcuts import render
from users import models as users_model
from . import models as recipies_model
from django.db.models import Count


def recipe_list(request, pk):
    user = users_model.User.objects.get(pk=pk)
    user_food_list = []
    for food in user.foods.all():
        user_food_list.append(food.name)
    reco_recipe = recipies_model.Recipe.objects.all()
    resulted_reco_recipe = []
    for reco_food in reco_recipe:
        food_list = []
        count = 0
        reco_food_len = 0
        for food in reco_food.food.all():
            count = count + user_food_list.count(food.name)
            reco_food_len = reco_food_len + 1
        if count == reco_food_len:
            resulted_reco_recipe.append(reco_food.name)
    recipes = reco_recipe.filter(name__in=resulted_reco_recipe)
    # print("user가 갖고있는 식자재 객체")
    # print(user.foods.all())
    # print("추천레시피가 갖고있는 식자재 객체")
    # print(reco_food.food.all())

    context = {
        "user": user,
        "recipes": recipes,
    }
    return render(request, "recipies/recipe_list.html", context)


def recipe_detail(request):
    return render(request, "recipies/recipe_detail.html")
