from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from .models import gifs, catégorie
from django.shortcuts import render
from .form import gifsForm, catégorieForm
# Create your views here.

def affiche(request):
    context = {
        'gifs' : gifs.objects.all(),
        'categorie' : catégorie.objects.all(),
    }
    return render(request, 'posts/affiche.html', context)



def ajoutegif(request):
    context = {
        'form' : gifsForm(),
    }
    return render(request, 'posts/ajoutegif.html', context)



def ajoutecategorie(request):
    context = {
        'form' : catégorieForm(),
    }
    return render(request, 'posts/ajoutecategorie.html', context)
