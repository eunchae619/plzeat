from django.shortcuts import render
from django.db.models import Count
from django.core.paginator import Paginator
from users import models as users_model
from . import models as recipies_model


def recipe_list(request, pk):
    user = users_model.User.objects.get(pk=pk)
    user_foods = user.foods.all()
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

    paginator = Paginator(recipes, 4)
    page_number = request.GET.get("page")
    paged_recipes = paginator.get_page(page_number)

    context = {
        "user": user,
        "recipes": recipes,
        "paged_recipes": paged_recipes,
        "paginator": paginator,
    }
    return render(request, "recipies/recipe_list.html", context)


def recipe_detail(request, pk):
    recipe = recipies_model.Recipe.objects.get(pk=pk)
    return render(request, "recipies/recipe_detail.html", {"recipe": recipe})

def recipe_worldcup(request):
    # DB에있는 모든 레시피 객체가 all_recipes에 담김
    all_recipes = recipies_model.Recipe.objects.all()
    print(all_recipes)

    # 64개의 레시피 객체를 랜덤으로 뽑아서 random_picked_recipes변수안에 담음
    random_picked_recipes = all_recipes.random(2)

    return render(request, 'recipies/recipe_worldcup.html',{'recipes':random_picked_recipes})