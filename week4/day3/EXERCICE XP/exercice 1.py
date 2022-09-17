#EXERCICE 1 (Convertir Des Listes En Dictionnaires)
# Convertissez les deux listes suivantes en dictionnaires.
# Conseil : Utilisez la méthodezip
# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

for i in zip(keys,values):
    print(i)
    
    