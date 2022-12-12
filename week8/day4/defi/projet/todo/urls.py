from django.urls import path #path function
from . import views # . is shorthand for the current directory

# one urlpattern per line
urlpatterns = [
    path('', views.display_todos, name='display_todos'),
    path('ajoute', views.ajoute, name='ajoute'),
]