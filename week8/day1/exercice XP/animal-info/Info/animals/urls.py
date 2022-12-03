from django.urls import path #path function
from . import views # . is shorthand for the current directory
from django.urls import  include ,path


# one urlpattern per line
urlpatterns = [
    path('family/<int:X>/', views.famille, name='famille'),
    path('animal/<int:X>/', views.animal, name='animal'),
   
  
]
