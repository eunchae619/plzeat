# Generated by Django 2.2.5 on 2020-04-25 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='test',
            field=models.CharField(max_length=12, null=True),
        ),
    ]
