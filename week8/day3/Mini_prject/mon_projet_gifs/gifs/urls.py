from django.urls import path #path function
from . import views
path('', views.affichage, name='index'),
