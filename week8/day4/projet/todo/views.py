from django.shortcuts import render
from django.shortcuts import render
from .models import categorie, todo
from django.shortcuts import render
from .form import TodoForm

# Create your views here.
def display_todos(request):
    context = {
        'category' : categorie.objects.all(),
    }
    return render(request, 'posts/display_todos.html', context)

def ajoute(request):
	context = {
	'forms' : TodoForm(),
	}
	return render(request, 'posts/ajoute.html', context)