from django.db import models


class Recipe(models.Model):
    name = models.CharField(max_length=100, null=True)
    photo = models.ImageField(upload_to="recipies", default="default.png")
    food = models.ManyToManyField("FoodInRecipe", related_name="recipies", blank=True)
    how_to_create = models.TextField(max_length=10000, null=True)
    #rank=models.DecimalField(max_digit=1,decimal_places=1,null=True) DB갱신후
    #flag=models.PositiveSmallIntegerField  0=디폴트, 1=즐겨찾기, 2=숨긴 레시피
    def __str__(self):
        return self.name


class FoodInRecipe(models.Model):
    name = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.name = self.name.replace(" ", "")
        super().save(*args, **kwargs)
