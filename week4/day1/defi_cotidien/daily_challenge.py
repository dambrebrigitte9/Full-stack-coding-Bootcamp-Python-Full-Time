#exo 4
from itertools import chain
from operator import index
from typing import final


users=input("entre une valeur avec 10 cractere :")
chaine=len(users)
if chaine==10:
    print("10 caractere entre")
elif chaine<10:
    print("chaine pas asssez longue")
else:
    print("chaine trop longue")
first=users[0]
print(first)
last=users[chaine-1]
print(last)
print(first,first+last,users)
enfant='j'+users[1:], 'i'+users[2:]
print(enfant)

    


    
        
    
    
    
    

    
   
