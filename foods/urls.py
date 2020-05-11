from django.urls import path
from . import views


app_name = "foods"

urlpatterns = [
    path("<int:pk>/", views.food_detail, name="food_detail"),
    path("register/", views.FoodRegisterView.as_view(), name="register"),
    path("list/", views.food_list, name="list"),
    path("delete/<int:pk>/", views.food_delete, name="delete"),
]
