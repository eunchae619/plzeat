from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, ListView
from users import models as users_model
from . import models as foods_model, forms

# Create your views here.


class FoodList(ListView):
    model = foods_model.Food
    paginate_by = 9
    ordering = "created"
    context_object_name = "foods"


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


class FoodRegisterView(CreateView):
    model = foods_model.Food
    form_class = forms.FoodRegisterForm
    success_url = reverse_lazy("core:home")

    def form_valid(self, form):
        food = form.save(commit=False)
        food.user = self.request.user
        food.save()
        return super().form_valid(form)
