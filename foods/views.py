from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from django import forms as django_forms
from users import models as users_model
from core import mixins
from . import models as foods_model, forms


# Create your views here.


def food_list(request):
    if request.user.is_anonymous:
        return redirect(reverse("core:login"))
    page = request.GET.get("page")
    food_list = foods_model.Food.objects.filter(user=request.user.pk)
    paginator = Paginator(food_list, 9)
    foods = paginator.get_page(page)
    context = {"foods": foods, "paginator": paginator}
    return render(request, "foods/food_list.html", context)


def food_detail(request, pk):
    try:
        food = foods_model.Food.objects.get(pk=pk)
    except foods_model.Food.DoesNotExist:
        return redirect(reverse("core:home"))
    if food.user != request.user:
        return redirect(reverse("core:login"))
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


class FoodRegisterView(CreateView, mixins.LoggedInOnlyView):
    model = foods_model.Food
    form_class = forms.FoodRegisterForm
    success_url = reverse_lazy("core:home")
    context_object_name = "my_form"

    def form_valid(self, form):
        food = form.save(commit=False)
        my_food = foods_model.Food.objects.filter(user=self.request.user.pk)
        filtered_food = my_food.filter(name=food.name)
        if filtered_food:
            form.add_error("name", "이미 존재하는 식자재입니다")
            return self.form_invalid(form)
        else:
            food.user = self.request.user
            food.save()
            return super().form_valid(form)

    def get(self, request, *args, **kwargs):
        self.object = None
        if self.request.user.is_anonymous:
            return redirect(reverse("core:login"))
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(FoodRegisterView, self).get_context_data(**kwargs)
        context["my_form"] = context["form"]
        return context


def food_delete(request, pk):
    food = foods_model.Food.objects.get(pk=pk)
    food.delete()
    return redirect(reverse("foods:list"))
