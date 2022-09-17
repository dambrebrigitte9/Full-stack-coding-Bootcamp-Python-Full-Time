# #EXERCICE 4
# Utilisez cette liste :

# users = ["Mickey","Minnie","Donald","Ariel","Pluto"]
# Analysez ces résultats :

# #1/

# >>> print(disney_users_A)
# {"Mickey": 0, "Minnie": 1, "Donald": 2, "Ariel": 3, "Pluto": 4}

# #2/

# >>> print(disney_users_B)
# {0: "Mickey",1: "Minnie", 2: "Donald", 3: "Ariel", 4: "Pluto"}

# #3/ 

# >>> print(disney_users_C)
# {"Ariel": 0, "Donald": 1, "Mickey": 2, "Minnie": 3, "Pluto": 4}


# Utilisez une boucle for pour recréer le 1er résultat. Astuce : ne codez pas les chiffres en dur.
# Utilisez une boucle for pour recréer le 2ème résultat. Astuce : ne codez pas les chiffres en dur.
# Utilisez une méthode pour recréer le 3ème résultat. Astuce : Le 3ème résultat est trié par ordre alphabétique.
# Ne recréez que le 1er résultat pour :
# Les caractères, dont les noms contiennent la lettre « i ».
# Les caractères, dont les noms commencent par la lettre « m » ou « p ».

users = ["Mickey","Minnie","Donald","Ariel","Pluto"]
print(users)
bibi={}
for i in range(0,5):
    for u in users:
        bibi[users[i]]=i
        
print(bibi)


bib={}
for i in range(0,5):
    bib[i]=users[i]      
print(bib)


bi={}
users.sort()
for i in range(0,5):
     bi[users[i]]=i
     print(bi)
    



