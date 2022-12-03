from django.shortcuts import render
from django.http import HttpResponse # pass view information into the browser



# Create your views here.
def index(request):
	people = [
	  {
	    'id': 1,
	    'name': 'Bob Smith',
	    'age': 35,
	    'country': 'USA'
	  },
	  {
	    'id': 2,
	    'name': 'Martha Smith',
	    'age': 60,
	    'country': 'USA'
	  },
	  {
	    'id': 3,
	    'name': 'Fabio Alberto',
	    'age': 18,
	    'country': 'Italy'
	  },
	  {
	    'id': 4,
	    'name': 'Dietrich Stein',
	    'age': 85,
	    'country': 'Germany'
	  }
	]
	people = {
        'subjects': people
     }
	return render(request, "posts/index.html")


