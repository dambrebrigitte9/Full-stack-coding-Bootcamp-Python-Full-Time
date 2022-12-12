from django.contrib import admin
from .models import gifs, catégorie #import the Person model


# Register your models here.
admin.site.register(gifs)
admin.site.register(catégorie)

