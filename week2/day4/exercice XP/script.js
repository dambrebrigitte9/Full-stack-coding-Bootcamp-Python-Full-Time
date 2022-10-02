// Exercice 1 : Information
// Instructions
// Partie I : fonction sans paramètres

// Créez une fonction appelée qui ne prend aucun paramètre.infoAboutMe()
// La fonction doit consoler.log une phrase sur vous (c’est-à-dire votre nom, votre âge, vos passe-temps, etc.).
// Appelez la fonction.


// Partie II : fonction à trois paramètres

// Créez une fonction appelée qui prend 3 paramètres.infoAboutPerson(personName, personAge, personFavoriteColor)
// La fonction doit consoler.log une phrase sur la personne (c’est-à-dire « Votre nom est ..., vous êtes .. ans, votre couleur préférée est ... »)
// Appelez la fonction deux fois avec les arguments suivants :
// infoAboutPerson("David", 45, "blue")
// infoAboutPerson("Josh", 12, "yellow")
function infoAboutMe(){
    console.log("je m'appelle Ali, j'ai 25 ans et j'aime etudier")
}

infoAboutMe()

function infoAboutPerson(personName, personAge, personFavoriteColor){
    console.log("mon nom est " +personName, "j'ai",+personAge, "ans","et", "ma couleur préférée est "+personFavoriteColor)
}
    infoAboutPerson("David ", 45, "blue")
    infoAboutPerson("Josh", 12, "yellow")


    // Exercice 2 : Conseils
    // Instructions
    // John a créé une calculatrice de pourboires simple pour aider à calculer combien de pourboires quand lui et sa famille vont au restaurant.
    
    // Créez une fonction nommée qui ne prend aucun paramètre.calculateTip()
    
    // À l’intérieur de la fonction, demandez à John le montant de la facture.
    
    // Voici les règles
    // Si la facture est inférieure à 50 $, donnez un pourboire de 20 %.
    // Si la facture se situe entre 50 $ et 200 $, donnez un pourboire de 15 %.
    // Si la facture est supérieure à 200 $, donnez un pourboire de 10 %.
    
    // Console.log le montant du pourboire et la facture finale (facture + pourboire).
    
    // Appelez la fonction.calculateTip()


    function calculateTip(){
      facture=Number(prompt("enter le le montant de la facture"))
      let pourboir1=(facture*20)/100
      let pourboir2=(facture*15)/100
      let pourboir3=(facture*10)/100
     
      if (facture <50){
      console.log("le  montant du pourboire est",pourboir1)
      console.log("la facture finale est :", facture+pourboir1)
      }else{
        console.log(" ")
      }

      if(facture>=50 ,facture<=200){
        console.log("le  montant du pourboire est",pourboir2 )
        console.log("la facture finale est :", facture+pourboir2)
      }else{
        console.log(" ")
      }

      if(facture>200){
        console.log("le montant du pourboire est",pourboir3 )
        console.log("la facture finale est :", facture+pourboir3)
      }else{
        console.log(" ")
      }

      

  }


  calculateTip()




//   Exercice 3 : Trouver Les Nombres Divisibles Par 23
// Instructions
// Créez un appel de fonction qui ne prend aucun paramètre.isDivisible()

// Dans la fonction, parcourez en boucle les nombres 0 à 500.

// Console .log tous les nombres divisibles par 23.

// À la fin, console.log la somme de tous les nombres divisibles par 23.

// Outcome : 0 23 46 69 92 115 138 161 184 207 230 253 276 299 322 345 368
// 391 414 437 460 483
// Sum : 5313


// Bonus : Ajoutez un diviseur de paramètres à la fonction.

// isDivisible(divisor)

// Example:
// isDivisible(3) : Console.log all the numbers divisible by 3, and their sum
// isDivisible(45) : Console.log all the numbers divisible by 45, and their sum

function isDivisible(){
   let somme=0
  
  for (var i = 0; i <= 500; i++) {
      // console.log(i);
      if (i%23==0){
        console.log("tous les nombres divisibles par 23 sont",i)
        somme= somme+i
      }
       
  }
  console.log("la somme est : ", somme)
}
isDivisible();


function isDivisible(divisor){
		console.log(" les nombres divisible par",divisor)
		let somme= 0;
		for (var i = 0; i <= 500; i++) {
			if ( i%divisor == 0) {
				console.log(i);
				somme=somme+i
			}
		}
		console.log("la somme est :",somme);
	}

	isDivisible(Number(prompt("taper un nombre : ")));




//   Exercice 4 : Liste De Courses
// Instructions
// let stock = { 
//     "banana": 6, 
//     "apple": 0,
//     "pear": 12,
//     "orange": 32,
//     "blueberry":1
// }  

// let prices = {    
//     "banana": 4, 
//     "apple": 2, 
//     "pear": 1,
//     "orange": 1.5,
//     "blueberry":10
// } 
// Ajoutez les objets et à votre fichier js.stockprices

// Créez un tableau appelé avec les éléments suivants : « banane », « orange » et « pomme ». Cela signifie que vous avez 1 banane, 1 orange et 1 pomme dans votre panier.shoppingList

// Créez une fonction appelée qui ne prend aucun paramètre. myBill()

// La fonction doit renvoyer le prix total de votre fichier . Pour ce faire, vous devez suivre ces règles:shoppingList
// L’article doit être en stock. (Astuce : vérifier if .. in)
// Si l’article est en stock, découvrez le prix de l’objet.prices

// Appelez la fonction.myBill()

// Bonus: Si l’article est en stock, diminuez le stock de l’article de 1

let stock = { 
  "banana": 6, 
  "apple": 0,
  "pear": 12,
  "orange": 32,
  "blueberry":1
} 

let prices = {    
  "banana": 4, 
  "apple": 2, 
  "pear": 1,
  "orange": 1.5,
  "blueberry":10
} 

let shoppingList=[
  "banana",
  "orange",
  "apple" 
]

function myBill(){
  let somme=0
  for (i of shoppingList){
    if (stock[i]>0){
      somme=somme+prices[i]
      stock[i] -= 1
    }
    else{
      console.log("rupture:",i)
    }
  }
  console.log("la somme est de ",somme)


}

myBill()


// Exercice 5 : Qu’y A-T-Il Dans Mon Portefeuille ?
// Instructions
// Remarque: Lisez l’illustration (point 4), tout en lisant les instructions

// Créez une fonction nommée qui reçoit deux arguments :changeEnough(itemPrice, amountOfChange)
// le prix d’un article
// et un tableau représentant la quantité de monnaie dans votre poche.

// Dans la fonction, déterminez si vous pouvez ou non vous permettre l’article.
// Si la somme de la modification est supérieure ou égale au prix de l’article (c’est-à-dire que cela signifie que vous pouvez vous permettre l’article), la fonction doit retourner true
// Si la somme de la modification est inférieure au prix de l’article (c’est-à-dire que cela signifie que vous ne pouvez pas vous permettre l’article), la fonction doit retourner false

// Le changement sera toujours représenté dans l’ordre suivant: quarts, sous, nickels, centimes.
// A quarters is 0.25
// A dimes is 0.10
// A nickel is 0.05
// A penny is 0.01


// 4. Pour illustrer :

// Après avoir créé la fonction, appelez-la comme suit :

// changeEnough(4.25, [25, 20, 5, 0])
// La valeur représente le prix de l’article4.25
// Le tableau représente 25 quarts, 20 sous, 5 nickels et 0 centime.[25, 20, 5, 0]
// La fonction devrait revenir, car avoir 25 trimestres, 20 sous, 5 nickels et 0 centime vous donne ce qui est supérieur à 4,25 (le montant total dû)true6.25 + 2 + .25 + 0 = 8.50


// Exemples

// changeEnough(14.11, [2,100,0,0]) => returns false
// changeEnough(0.75, [0,0,20,5]) => returns true


function changeEnough(itemPrice, amountOfChange){
  for (u in amountOfChange){
    if (amountOfChange[u] >=4.25){
      return true
    }
    else{
      return false
    }
  }
}

changeEnough(4.25, [25, 20, 5, 0])



// Exercice 6 : Frais De Vacances
// Instructions
// Créons des fonctions qui calculent les coûts de vos vacances:

// Définissez une fonction appelée . hotelCost()
// Il doit demander à l’utilisateur le nombre de nuits qu’il souhaite séjourner à l’hôtel.
// Si l’utilisateur ne répond pas ou si la réponse n’est pas un numéro, demandez à nouveau.
// L’hôtel coûte 140 $ par nuit. La fonction devrait le prix total de l’hôtel. return

// Définissez une fonction appelée .planeRideCost()
// Il devrait demander à l’utilisateur sa destination.
// Si l’utilisateur ne répond pas ou si la réponse n’est pas une chaîne, demandez à nouveau.
// La fonction devrait avoir un prix différent en fonction de l’emplacement.return
// « Londres »: 183$
// « Paris » : 220$
// Toutes les autres destinations : 300$

// Définissez une fonction appelée .rentalCarCost()
// Il devrait demander à l’utilisateur le nombre de jours qu’il souhaite louer la voiture.
// Si l’utilisateur ne répond pas ou si la réponse n’est pas un numéro, demandez à nouveau.
// Calculez le coût de location de la voiture. La voiture coûte 40 $ tous les jours.
// Si l’utilisateur loue une voiture pour plus de 10 jours, il bénéficie d’une réduction de 5%.
// La fonction devrait le prix total de la location de voiture. return

// Définissez une fonction appelée qui renvoie le coût total des vacances de l’utilisateur en appelant les 3 fonctions que vous avez créées ci-dessus.
// Exemple : Le coût de la voiture : $x, le coût de l’hôtel : $y, le coût des billets d’avion : $z.
// Astuce : Il faut appeler les fonctions , et à l’intérieur de la fonction .totalVacationCost()hotelCost()planeRideCost()rentalCarCost()totalVacationCost()

// Appeler la fonction totalVacationCost()

// Bonus: Au lieu d’utiliser une à l’intérieur des 3 premières fonctions, utilisez uniquement une invite à l’intérieur de la fonction. Vous devez modifier les 3 premières fonctions en conséquence.prompttotalVacationCost()