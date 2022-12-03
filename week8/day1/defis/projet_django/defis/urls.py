from django.urls import path #path function
from . import views # . is shorthand for the current directory
from django.urls import  include ,path


# one urlpattern per line
urlpatterns = [
    path('', views.index, name='index'),
    # path('index', views.people, name='index'),


  
]
