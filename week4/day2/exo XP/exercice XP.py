#exo1 (les ensembles)
from ctypes.wintypes import HHOOK
from operator import index
from subprocess import list2cmdline
from tkinter import Variable
from typing import final


mes_numero=[1,2,5,4]
print(mes_numero)
mes_numero.append(14) 
mes_numero.append(121)
print(mes_numero)
del mes_numero[5]
print(mes_numero)
variable_ami=[9,8,7,6]
print(variable_ami)
final="mes numero favoris sont:" ,mes_numero,"les numero favoris de mes amis sont:" ,variable_ami
print(final)

# A REFAIRE L'EXERCICE 1  PARCE QUE JAI MAL COMPRIS


#EXERCICE 2 (les tuples)
# Étant donné un tuple dont la valeur est des entiers, est-il possible d’ajouter plus d’entiers au tuple ?
# REPONSE: on ne peut pas ajouter d'element a un tuple une fois creer



#exo 3 (les listes)
# Utilisation de cette liste basket = ["Banana", "Apples", "Oranges", "Blueberries"];

# Supprimez « Banana » de la liste.
# Supprimez « Blueberries » de la liste.
# Ajoutez « Kiwi » à la fin de la liste.
# Ajoutez « Pommes » au début de la liste.
# Comptez combien de pommes sont dans le panier.
# Videz le panier.
# Imprimer(panier)
basket = ["Banana", "Apples", "Oranges", "Blueberries"]
del basket[0]
print(basket)
del basket[2]
print(basket)
basket.append("Kiwi")
print(basket)
basket.insert(0,"Pommes")
print(basket)
print(" la longueur de pommes est  :",len("Pommes"))
if len("Pommes")==6:
    print("pommes apparait une seul fois dans la liste")
else:
     print("rien")
del basket[:]
print(basket)

# EXERCICE 4(les flotteurs)
# Récapitulatif – Qu’est-ce qu’un ? Quelle est la différence entre un entier et un float ? float
# Pouvez-vous penser à une autre façon de générer une séquence de flotteurs?
# Créez une liste contenant la séquence suivante 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5 (ne codez pas la séquence en dur).

liste_1=[1.5,2.5,3,3.5,4,4.5,5]
print(liste_1)


# EXERCICE 5 (pour loop)
# Utilisez une boucle pour imprimer tous les nombres de 1 à 20 inclus.for
# À l’aide d’une boucle, qui boucle de 1 à 20 (inclus), imprimez chaque élément qui a un index pair.for

for i in range(1,20+1):
     print(i)
bibi=list(range(1,20+1))
print(bibi)
for i in bibi:
         if(bibi.index(i)%2!=0):
             print(bibi.index(i))


#EXERCICE 6(en boucle)
# Écrivez une boucle while qui demandera continuellement à l’utilisateur son nom, sauf si l’entrée est égale à votre nom.
nom=input("entrer votre nom :")
while nom != "Brigitte":
      nouveau_nom=input("entrer votre nom:")
      print(nouveau_nom)




# EXERCICE 7 (fruits prefere)
# Demandez à l’utilisateur d’entrer son ou ses fruits préférés (un ou plusieurs fruits).
# Astuce : Utilisez la méthode intégrée. Demandez à l’utilisateur de séparer les fruits avec un seul espace, par exemple. .input"apple mango cherry"
# Conservez le(s) fruit(s) préféré(s) dans une liste (convertissez la chaîne de mots en une liste de mots).
# Maintenant que nous avons une liste de fruits, demandez à l’utilisateur d’entrer un nom de n’importe quel fruit.
# Si l’entrée de l’utilisateur se trouve dans la liste des fruits favoris, imprimez « Vous avez choisi l’un de vos fruits préférés! Profitez-en! ».
# Si l’entrée de l’utilisateur n’est PAS dans la liste, imprimez « Vous avez choisi un nouveau fruit. J’espère que vous apprécierez ».

users=input('votre fuits prefere:')
bibi=users.split(",")
print(bibi)
users=list(bibi)
print(type(bibi))
users_2=input("entrer n'importe quel fuits:")
if users_2 in bibi==users:
    print("Vous avez choisi l’un de vos fruits préférés! Profitez-en! ».")
else:
    print("« Vous avez choisi un nouveau fruit. J’espère que vous apprécierez ».")
    
    
    
    #EXERCICE 8 (Qui a commander une pizza)
    #Écrivez une boucle qui demande à un utilisateur d’entrer une série de garnitures de pizza, lorsque l’utilisateur entre « quitter » arrêter de demander des garnitures.
# Lorsqu’ils entrent dans chaque garniture, imprimez un message indiquant que vous ajouterez cette garniture à leur pizza.
# En sortant de la boucle, imprimez toutes les garnitures sur la tarte à pizza et quel est le prix total (10 + 2,5 pour chaque garniture).

users=input("entrer une serie de garniture:")
userss=[]
bel="quitter"
while users!=bel:
    print("j'ai ajouter " +users ,"a ma liste de garniture")
    userss.append(users)
    users=input("entrer une serie de garniture:")  
print(userss)  
prix=10+(len(userss)*2.5)
print(prix)

#EXERCICE 9
#Une salle de cinéma facture des prix de billets différents en fonction de l’âge d’une personne.
# si une personne a moins de 3 ans, le billet est gratuit.
# s’ils ont entre 3 et 12 ans, le billet est de 10 $.
# s’ils ont plus de 12 ans, le billet est de 15 $.
# Demandez à une famille l’âge de chaque personne qui veut un billet.
# Conservez le coût total de tous les billets de la famille et imprimez-le.

# Un groupe d’adolescents vient à votre salle de cinéma et veut regarder un film qui est réservé aux personnes âgées de 16 à 21 ans.
# Avec une liste de noms, écrivez un programme qui demande à l’adolescent son âge, s’il n’est pas autorisé à regarder le film, retirez-le de la liste.
# À la fin, imprimez la liste finale.

famille= int(input("entrer l'age de cette personne:"))
bibi="le billet est gratuit"
baba="le billet est de 10 $"
bebe="le billet est de 15$"
if famille<3:
    
    print(bibi)
elif famille>=3 and famille<=12:
    
    print(baba)
elif famille>12:
    
    print(bebe)
else:
    print("rien")
   

users=" quel est l'age de cette personne qui veut un billet ?"
print(users)
age="l'age  de cette personne de la famille entrer est de", famille ,"ans"
print(age)
bilet_total="la liste de billet sont:",bibi,baba,bebe
print(bilet_total)

nom=input("entre votre nom:")
prenom=input('entrer votre prenom:')
age=int(input("entrer votre age:"))
list=[nom,prenom,age]
print(list)
if age>=16 and age <=21:
    print(list)
else:
    list.remove(list)
print(list)


