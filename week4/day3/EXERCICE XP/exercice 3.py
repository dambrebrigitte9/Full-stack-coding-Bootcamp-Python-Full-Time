# EXERCICE 3 ()
# Voici quelques informations sur une marque.
# name: Zara 
# creation_date: 1975 
# creator_name: Amancio Ortega Gaona 
# type_of_clothes: men, women, children, home 
# international_competitors: Gap, H&M, Benetton 
# number_stores: 7000 
# major_color: 
#     France: blue, 
#     Spain: red, 
#     US: pink, green


# 2. Créez un dictionnaire appelé quelle valeur est l’information de la première partie (transformez les informations en clés et valeurs).
# 3. Modifiez le nombre de magasins à 2.
# 4. Imprimez une phrase qui explique qui sont les clients zaras.
# 5. Ajoutez une clé appelée avec la valeur .
# 6. Vérifiez si la clé est dans le dictionnaire. Si c’est le cas, ajoutez le magasin Desigual.
# 7. Supprimez les informations sur la date de création.
# 8. Imprimez le dernier concurrent international.
# 9. Imprimez les principales couleurs de vêtements aux États-Unis.
# 10. Imprimez la quantité de paires de valeurs de clé (c’est-à-dire la longueur du dictionnaire).
# 11. Imprimez les clés du dictionnaire.
# 12. Créez un autre dictionnaire appelé avec les détails suivants:brandcountry_creationSpaininternational_competitorsmore_on_zara

# creation_date: 1975 
# number_stores: 10 000


# 13. Utilisez une méthode pour ajouter les informations du dictionnaire au dictionnaire .
# 14. Imprimez la valeur de la clé . Qu’est-ce qu’il vient de se passer?more_on_zarabrandnumber_stores




users={
'name': 'Zara ',
'creation_date': 1975 ,
'creator_name':[' Amancio ','Ortega','Gaona'], 
'type_of_clothes':[' men', 'women', 'children','home'], 
'international_competitors':['Gap', 'H&M', 'Benetton'], 
'number_stores': 7000 ,
'major_color':{ 
  'France': 'blue', 
  'Spain': 'red', 
  'US':['pink', 'green'],
}
}

print(users)
users['number_stores']=2
print(users)
print("les clients de zara sont: ",users['creator_name'][0], "avec",users['creator_name'][1], "et " ,users['creator_name'][2])
users['mes produits']=['savon',' gel de douche','pomades']
print(users)
print(type(users['type_of_clothes']))
if 'international_competitors' in users:

    users['international_competitors'].append('portugal')
else:
  print("ffffffff")
print(users['international_competitors'])
print(users)
del users['creation_date']
print(users)
print(users['international_competitors'][2])

print("les principales couleurs de vêtements aux États-Unis sont le :",users['major_color']['US'][0],"et le ",users['major_color']['US'][1])

print("la longuer du dictionnaire est: ",len(users))
for x,y in users.items():
  print(x)

more_on_zara={
'creation_date': 1975 ,
'number_stores': 10000 ,
}
print(more_on_zara)

users.update(more_on_zara)
print("mon dictionnaire final est:",users)
print("la valeur de la clé est:",more_on_zara['creation_date'],"et ", more_on_zara['number_stores'])
print("il vient de mettre a jour mon dictionnair en remplacant les anciennes clés de mon dict par les nouvelles de ma clée ")
