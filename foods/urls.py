from django.urls import path
from . import views


app_name = "foods"

urlpatterns = [path("<int:pk>", views.food_detail, name="food_detail")]
