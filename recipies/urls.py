from django.urls import path
from . import views

app_name = "recipies"

urlpatterns = [
    path("list/<int:pk>", views.recipe_list, name="recipe_list"),
    path("detail/<int:pk>", views.recipe_detail, name="recipe_detail"),
    path('worldcup/',views.recipe_worldcup,name="worldcup"),
]
