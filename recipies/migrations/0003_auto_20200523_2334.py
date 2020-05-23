# Generated by Django 2.2.5 on 2020-05-23 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipies', '0002_recipe_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='recipe_level',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='recipe',
            name='recipe_quantity',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='recipe',
            name='recipe_time',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='recipe',
            name='subname',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
