from django.urls import path #path function
from . import views
urlpatterns = [
    path('', views.affiche, name='affiche'),
    path('ajoutegif', views.ajoutegif, name='ajoutegif'),
    path('ajoutecategorie', views.ajoutecategorie, name='ajoutecategorie'),
]