from django import forms
from . import models


class FoodRegisterForm(forms.ModelForm):
    class Meta:
        model = models.Food
        fields = (
            "name",
            "photo",
            "expired_date",
            "quantity",
        )
