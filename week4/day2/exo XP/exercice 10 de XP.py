#EXERCICZ 10 (commande de sandwich)
# sandwich_orders = ["Tuna sandwich", "Avocado sandwich", "Egg sandwich", "Sabih sandwich", "Pastrami sandwich"]
# Utilisez la liste ci-dessus appelée . sandwich_orders
# Créez une liste vide appelée .finished_sandwiches
# Au fur et à mesure que chaque sandwich est fait, déplacez-le dans la liste des sandwichs finis.
# Une fois que tous les sandwichs ont été faits, imprimez un message répertoriant chaque sandwich qui a été fait, tel que . I made your tuna sandwich
sandwich_orders = ["Tuna sandwich", "Avocado sandwich", "Egg sandwich", "Sabih sandwich", "Pastrami sandwich"]
print(sandwich_orders)
finished_sandwiches=[]
print("le deuxieme tableau vide est:",finished_sandwiches)
bib="Tuna sandwich"
eude="Avocado sandwich"
trois="Egg sandwich"
quatre="Sabih sandwich"
cing= "Pastrami sandwich"

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
print("la liste finie de sandwich est :", finished_sandwiches)    
    

    
    


    

   
     
 
  
