from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.HowToUseFood)
class HowToUseFoodAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Food)
class FoodAdmin(admin.ModelAdmin):
    pass
