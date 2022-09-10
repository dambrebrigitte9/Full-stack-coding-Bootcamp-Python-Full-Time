#exo1 (les ensembles)
from ctypes.wintypes import HHOOK
from operator import index
from tkinter import Variable
from typing import final


# mes_numero=[1,2,5,4]
# print(mes_numero)
# mes_numero.append(14) 
# mes_numero.append(121)
# print(mes_numero)
# del mes_numero[5]
# print(mes_numero)
# variable_ami=[9,8,7,6]
# print(variable_ami)
# final="mes numero favoris sont:" ,mes_numero,"les numero favoris de mes amis sont:" ,variable_ami
# print(final)

# A REFAIRE L'EXERCICE 1 DEMAIN PARCE QUE JAI MAL COMPRIS


#exo 2 (les tuples)
#on ne peut pas ajouter d'element a un tuple une fois creer



#exo 3 (les listes)
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

#exo 4(les flotteurs)
liste_1=[1.5,2.5,3,3.5,4,4.5,5]
print(liste_1)


#exo 5 (pour loop)
for i in range(1,20+1):
     print(i)
bibi=list(range(1,20+1))
print(bibi)
for i in bibi:
         if(bibi.index(i)%2!=0):
             print(bibi.index(i))


#exo 6(en boucle)
nom=input("entrer votre nom :")
while nom != "Brigitte":
      nouveau_nom=input("entrer votre nom:")
      print(nouveau_nom)




#exo 7(fruits prefere)
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
