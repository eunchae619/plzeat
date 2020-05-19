from django.shortcuts import render, redirect
from django.urls import reverse
from users import models as users_models
from django.views import View
from django.contrib.auth import authenticate, login
from django.contrib import messages
from users import forms
from . import mixins


def home(request):
    if request.user.is_anonymous:
        return redirect(reverse("core:login"))
    user = users_models.User.objects.get(pk=request.user.pk)
    foods = user.foods.all().order_by("expired_date")[:4]
    return render(request, "main/home.html", {"foods": foods})


class LoginView(mixins.LoggedOutOnlyView, View):
    def get(self, request):
        form = forms.LoginForm()
        return render(request, "users/login.html", {"form": form})

    def post(self, request):
        form = forms.LoginForm(request.POST)
        not_verified = None
        if form.is_valid():
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=email, password=password)
            if user is not None:
                check_user = users_models.User.objects.get(email=email)
                pk = check_user.pk
                if check_user.email_verified is True:
                    login(request, user)
                    messages.success(request, f"환영합니다, {user.nickname}님!")
                    return redirect(reverse("core:home"))
                else:
                    not_verified = "이메일 인증을 해주세요."

        return render(
            request, "users/login.html", {"form": form, "not_verified": not_verified,}
        )
