#Exercice 1
print(("hello world \n")*4, ("i love python \n")*4)
#Exercice 2
users= int(input("entre un numbre entre 1 et 12 :"))

for i in range (3,5+1):
 if (i==range(3,5+1)):
        print(i,"printemps")
for v in range(6,8+1):
    if(v==range(6,8+1)):
       print(v,"ete")
for u in range(9,11+1):
   if(u==range(9,11+1)):
       print(u,"automne")
for x in range(12,2+1):
    if(x==range(12,2+1)):
        print(x,"hiver")
    else:
       print("ereur")

  #exo2
users= int(input("entre un numbre entre 1 et 12 :"))
if (users>=3 and users<=5):
    print("printemps")
elif(users>=6 and users<=8):
    print("été")
elif(users>=9 and users<=11):
    print("automne")
elif(users in [12,2] ):
    print("hiver")






