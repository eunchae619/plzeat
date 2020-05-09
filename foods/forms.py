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
        widgets = {
            "name": forms.TextInput(attrs={"placeholder": "식자재명"}),
            "expired_date": forms.TextInput(attrs={"placeholder": "유통기한 마감일"}),
            "quantity": forms.NumberInput(attrs={"placeholder": "갯수"}),
        }
