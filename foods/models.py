from django.db import models
from users import models as users_models

# Create your models here.


class HowToUseFood(models.Model):
    name = models.CharField(max_length=100)
    how_to_trim = models.TextField(max_length=10000, null=True)
    how_to_store = models.TextField(max_length=10000, null=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.name = self.name.replace(" ", "")
        super().save(*args, **kwargs)


class Food(models.Model):
    name = models.CharField(max_length=20)
    photo = models.ImageField(upload_to="enrolled_food", default="default.png")
    expired_date = models.DateField(null=False)
    quantity = models.IntegerField(null=True)
    created = models.DateTimeField(auto_now_add=True, null=True)
    user = models.ForeignKey(
        users_models.User, related_name="foods", on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.name = self.name.replace(" ", "")
        super().save(*args, **kwargs)
