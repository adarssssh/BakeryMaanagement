from django.contrib import admin

# Register your models here.
from .models import User,Products,Ingredients

admin.register(User)(admin.ModelAdmin)
admin.register(Products)(admin.ModelAdmin)
admin.register(Ingredients)(admin.ModelAdmin)
