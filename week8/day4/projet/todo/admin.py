from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import todo, categorie #import the Person model


# Register your models here.
admin.site.register(todo)
admin.site.register(categorie)
