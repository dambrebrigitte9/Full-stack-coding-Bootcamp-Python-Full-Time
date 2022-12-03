from django.shortcuts import render

# Create your views here.
context={
    "animals": [
        {
            "id" :1,
            "name": "Dog",
            "legs": 4,
            "weight": 5.67,
            "height":4.2,
            "speed": 34,
            "family": 2
        },
        {
            "id": 2,
            "name": "Domestic Cat",
            "legs": 2,
            "weight": 5.67,
            "height":4.2,
            "speed": 34,
            "family": 1
        },
        {
            "id": 3,
            "name": "Panther",
            "legs": 2,
            "weight": 5.67,
            "height":4.2,
            "speed": 34,
            "family": 1 
        },
         {
            "id": 4,
            "name": "Lion",
            "legs": "3",
            "weight": 5.67,
            "height":4.2,
            "speed": 34,
            "family": 3 
        },
         {
            "id": 5,
            "name": "vache",
            "legs": 5,
            "weight": 5.67,
            "height":4.2,
            "speed": 34,
            "family": 5
        }
    ],
    "families": [
        {
            "id": 1,
            "name": "Felidae"
        },
        {
            "id": 2,
            "name": "Caninae"
        },
        {
            "id": 3,
            "name": "mammifère"
        },
        {
            "id": 4,
            "name": "reptile"
        },
        {
            "id": 5,
            "name": "insecte"
        },
        {
            "id": 6,
            "name": "arachnide"
        },
        {
            "id": 7,
            "name": "amphibien"
        },
        {
            "id": 8,
            "name": "etc"
        }

    ]
}

def famille(request, X):
    context.update({'X' : X})
    return render(request, "animals/famille.html", context)

def animal(request, X):
    context.update({'X' : X})
    return render(request, "animals/animal.html", context)
