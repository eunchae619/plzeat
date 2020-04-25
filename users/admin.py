from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models
from foods import models as foods_models

# Register your models here.


class FoodInline(admin.TabularInline):
    model = foods_models.Food


@admin.register(models.User)
class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (("Custom Profile", {"fields": ()},),)

    inlines = [
        FoodInline,
    ]
