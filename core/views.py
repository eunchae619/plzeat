from django.shortcuts import render
from users import models as users_models


def home(request):
    users = users_models.User.objects.all()
    return render(request, "main/home.html", {"users": users})
