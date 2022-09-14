#EXERCICE 2( Cinemax)
# Une salle de cinéma facture des prix de billets différents en fonction de l’âge d’une personne.
# si une personne a moins de 3 ans, le billet est gratuit.
# s’ils ont entre 3 et 12 ans, le billet est de 10 $.
# s’ils ont plus de 12 ans, le billet est de 15 $.

# Compte tenu de l’objet suivant :

# family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}


# Combien chaque membre de la famille doit-il payer ?

# Imprimez le coût total de la famille pour les films.
# Bonus : Demandez à l’utilisateur d’entrer les noms et les âges au lieu d’utiliser la variable fournie
# (Astuce : demandez à l’utilisateur les noms et les âges et ajoutez-les dans un dictionnaire initialement vide).familyfamily
somme=0
billet=0
users=int(input("entre le nombre de personne qui veut un billet:"))
while users<=0:
    users=int(input("entre le nombre de personne qui veut un billet:"))
   
for i in range(users) :
    age=int(input("entrer votre age {}  :".format(i+1)))
    while age <= 0 and age >= 135 :
        age = int(input("Entrer l'age de la personne {} : ".format(i+1)))
    if age<3:
    
        somme= somme+0
        billet=billet+1
    elif age>=3 and age <=10:

        somme=somme+10
        billet=billet+1
    elif age>12:
   
        somme= somme+15
        billet=billet+1
    else :
        print("rien")
print("la nombre de billet a payer est {a} pour une somme de {b}".format(a=billet,b=somme))

somm=0
bille=0
family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
print(family)
for i in family :
    age2=int(input("entrer votre age "))
    while age2 <= 0 and age2 >= 135 :
        age2 = int(input("Entrer votre de la personne {} : ".format(i+1)))
    if age2<3:
        print("vous devez rien payer")
    
        somm= somm+0
        bille=bille+1
    elif age2>=3 and age2 <=10:
        print("vou devez payez 10$")
        somm=somm+10
        bille=bille+1
        
    elif age2>12:
        print("vous devez payer 15$")
        somm= somm+15
        bille=bille+1
    else :
        print("rien")
print(" le coût total de la famille pour les films est :le nombre de billet a payer est {c} pour une somme de {d}".format(c=bille,d=somm))






