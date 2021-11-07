# Generated by Django 3.2.9 on 2021-11-07 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BakeryOwner', '0002_ingredients_products'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ingredients',
            name='id',
        ),
        migrations.AlterField(
            model_name='ingredients',
            name='ingredient',
            field=models.CharField(max_length=20, primary_key=True, serialize=False, unique=True),
        ),
    ]
