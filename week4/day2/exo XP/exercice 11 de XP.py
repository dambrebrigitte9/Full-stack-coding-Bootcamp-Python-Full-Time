#EXERCICE 10 (commandes sandwich#2)
# En utilisant la liste de l’exercice précédent, assurez-vous que le sandwich 'pastrami' apparaît dans la liste au moins trois fois.
# sandwich_orders
# Ajoutez du code vers le début de votre programme pour imprimer un message indiquant que la charcuterie est à court de pastrami,
# puis utilisez une boucle pour supprimer toutes les occurrences de 'pastrami' de . whilesandwich_orders
# Assurez-vous qu’aucun sandwich au pastrami ne se retrouve dans .finished_sandwiches

from itertools import count
from multiprocessing.sharedctypes import Value


sandwich_orders = ["Tuna sandwich", "Avocado sandwich", "Egg sandwich", "Sabih sandwich", "Pastrami sandwich" ,"Pastrami sandwich","Pastrami sandwich" ]
print(sandwich_orders)
finished_sandwiches=[]
print("le deuxieme tableau vide est:",finished_sandwiches)
bib="Tuna sandwich"
eude="Avocado sandwich"
trois="Egg sandwich"
quatre="Sabih sandwich"
cing= "Pastrami sandwich"
ajout= "Pastrami sandwich "


if bib in sandwich_orders:
    print("le premier sandwich  est fait")
    finished_sandwiches.append(bib)
    print(finished_sandwiches)
else:
    print("r")
if eude in sandwich_orders:
    print("le deuxieme sandwich  est fait")
    finished_sandwiches.append(eude)
    print(finished_sandwiches)
else:
    print("r")
if trois in sandwich_orders:
    print("le troisieme sandwich  est fait")
    finished_sandwiches.append(trois)
    print(finished_sandwiches)
else:
    print("r")
if quatre in sandwich_orders:
    print("le quatrieme sandwich  est fait")
    finished_sandwiches.append(quatre)
    print(finished_sandwiches)
else:
    print("r")
if cing in sandwich_orders:
    print("le cinqieme sandwich  est fait")
    finished_sandwiches.append(cing)
    print(finished_sandwiches)
else:
    print("r")
    
# if ajout in sandwich_orders:
#     print("l'occurence a ete ajouter")
#     finished_sandwiches.append(ajout)
#     print(finished_sandwiches)
# else:
#     print("erreur")
    
print("la charcuterie est a cours de pastrami !!!!!!!") 

valueToBeRemoved = "Pastrami sandwich" 

 
try:
    while True:
        sandwich_orders.remove(valueToBeRemoved)
except ValueError:
    pass
 
print(" le resultat final est ",sandwich_orders)
print(finished_sandwiches)

finished_sandwiches.remove( "Pastrami sandwich")
print(finished_sandwiches)