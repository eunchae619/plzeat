from . import models as foods_models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def my_validator(value):
    # my_food = foods_models.Food.objects.filter(user=value.user)
    print(value)
    print(value)
    print(value)
    print(value)
    if value in my_food:
        raise ValidationError(
            _("이미있음"), params={"value": value},
        )
