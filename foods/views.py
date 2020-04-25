from django.shortcuts import render, redirect
from django.urls import reverse
from users import models as users_model
from . import models as foods_model

# Create your views here.


def food_detail(request, pk):
    food = foods_model.Food.objects.get(pk=pk)
    food_data = foods_model.HowToUseFood.objects.all()
    how_to_trim = ""
    how_to_store = ""
    try:
        equal_food = food_data.get(name=food)
        how_to_trim = equal_food.how_to_trim
        how_to_store = equal_food.how_to_store
    except:
        pass
    context = {
        "food": food,
        "how_to_trim": how_to_trim,
        "how_to_store": how_to_store,
    }
    return render(request, "foods/food_detail.html", context)
