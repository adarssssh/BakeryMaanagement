# Generated by Django 3.2.9 on 2021-11-07 10:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('BakeryOwner', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ingredient', models.CharField(max_length=20, unique=True)),
                ('quantity', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=20, unique=True)),
                ('cost', models.IntegerField()),
                ('Selling_price', models.IntegerField()),
                ('i1', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='i1', to='BakeryOwner.ingredients', unique=True)),
                ('i2', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='i2', to='BakeryOwner.ingredients', unique=True)),
                ('i3', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='i3', to='BakeryOwner.ingredients', unique=True)),
                ('i4', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='i4', to='BakeryOwner.ingredients', unique=True)),
                ('i5', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='i5', to='BakeryOwner.ingredients', unique=True)),
            ],
        ),
    ]
