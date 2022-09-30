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
      if (facture <50){
        console.log("le pourboire est",(facture*20)/100)
      }else{
        if(facture<=50 ,facture>=200){
          console.log("le pourboire est", (facture*15)/100)
        }else{
          if(facture>200){
            console.log("le pourboire est", (facture*10)/100)
          }else{
            console.log("erreur")
          }
        }

      }

    }
    calculateTip()




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
