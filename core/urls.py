from django.urls import path
from . import views

app_name = "core"

urlpatterns = [
    path("home", views.home, name="home"),
    path("", views.LoginView.as_view(), name="login"),
]
