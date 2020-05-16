from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def my_validator():
    pass


def validate_quantity(value):
    print(value)
    if int(value) < 1:
        raise ValidationError(
            _("양수를 입력 해 주세요"), params={"value": value},
        )
