from django.db import models


class Recipe(models.Model):
    name = models.CharField(max_length=100, null=True)
    food = models.ManyToManyField("FoodInRecipe", related_name="recipies", blank=True)
    how_to_create = models.TextField(max_length=10000, null=True)

    def __str__(self):
        return self.name


class FoodInRecipe(models.Model):
    name = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.name = self.name.replace(" ", "")
        super().save(*args, **kwargs)
