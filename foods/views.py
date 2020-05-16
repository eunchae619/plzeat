from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from users import models as users_model
from core import mixins
from . import models as foods_model, forms


# Create your views here.


@login_required
def food_list(request):
    page = request.GET.get("page")
    food_list = foods_model.Food.objects.filter(user=request.user.pk)
    paginator = Paginator(food_list, 3)
    foods = paginator.get_page(page)
    context = {"foods": foods, "paginator": paginator}
    return render(request, "foods/food_list.html", context)


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


class FoodRegisterView(CreateView, mixins.LoggedInOnlyView):
    model = foods_model.Food
    form_class = forms.FoodRegisterForm
    success_url = reverse_lazy("core:home")

    def form_valid(self, form):
        food = form.save(commit=False)
        food.user = self.request.user
        food.save()
        return super().form_valid(form)

    def get(self, request, *args, **kwargs):
        self.object = None
        if self.request.user.is_anonymous:
            return redirect(reverse("core:login"))
        print(self.request.user)
        return super().get(request, *args, **kwargs)


def food_delete(request, pk):
    food = foods_model.Food.objects.get(pk=pk)
    food.delete()
    return redirect(reverse("foods:list"))
