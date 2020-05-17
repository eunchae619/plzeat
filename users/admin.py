from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models
from foods import models as foods_models

# Register your models here.


class FoodInline(admin.TabularInline):
    model = foods_models.Food


@admin.register(models.User)
class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (
            "Personal Info",
            {"fields": ("username", "email", "nickname", "password", "login_method",)},
        ),
        ("About Email", {"fields": ("email_verified",)},),
        (
            "Permissions",
            {
                "classes": ("collapse",),
                "fields": ("is_active", "is_staff", "is_superuser",),
            },
        ),
    )

    inlines = [
        FoodInline,
    ]

    list_display = (
        "username",
        "is_superuser",
        "email_verified",
        "email_secret",
    )
