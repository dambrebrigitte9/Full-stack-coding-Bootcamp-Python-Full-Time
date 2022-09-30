// Ebalercice 1 : Liste Des Personnes
// Instructions
// let people = ["Greg", "Mary", "Devon", "James"];


// Partie I - Ebalamen Des Tableaubal
// Écrivez du code pour supprimer « Greg » du tableau.people

// Écrivez du code pour remplacer « James » par « Jason ».

// Écrivez du code pour ajouter votre nom à la fin du tableau.people

// Écrivez du code qui console.logs l’indebal de Mary. jetez un coup d’œil à la méthode indebalOf sur Google.

// Écrivez du code pour faire une copie du tableau à l’aide de la méthode. peopleslice
// La copie ne doit PAS inclure « Marie » ou votre nom.
// Astuce: rappelez-vous que maintenant le tableau devrait ressembler à ceci peoplelet people = ["Mary", "Devon", "Jason", "bibiourname"];
// Astuce : Consultez la documentation de la méthodeslice

// Écrivez du code qui donne l’indebal de « Foo ». Pourquoi renvoie-t-il -1 ?

// Créez une variable appelée quelle valeur est le dernier élément du tableau.
// Astuce : Quelle est la relation entre l’indebal du dernier élément du tableau et la longueur du tableau ?last


// Partie II - Boucles
// À l’aide d’une boucle, parcourez le tableau et la console.log chaque personne.people

// À l’aide d’une boucle, parcourez le tableau et quittez la boucle après avoir .log « Jason » de la console.
// Astuce : jetez un coup d’œil à la déclaration dans la leçon.peoplebreak

// EbalERCICE1

        //partie1
        let people = ["Greg", "Mary", "Devon", "James"];
        1//
        let bibi=people.splice(0,1);
        console.log(people);
        2//
        let eudes=people.splice(2,1,"jason");
        console.log(people);
        3//
        let voisin=people.push("brigitte");
        console.log(people);
        4//
        let marie=people.indexOf("Mary");
        console.log(people);//0
        5//
        let razack=people.slice(0,5);
        console.log(razack);//(4) ['Mary', 'Devon', 'jason', 'brigitte']
        6//
        console.log(people.indexOf("Foo"));//parce que foo n'est pas un element du tableau;
        7//
        let terminale=people[3];
        console.log("le dernier element du tableau est:",terminale)
        

        //partie2
        1//
        for (i in people){
            console.log("le tableau parcouru est:",people[i])
        }
        for (i in people){
            console.log(people[i])
            if (people[i]=='jason'){
                break
            }
            
        }
        
        // for (let x in people) {
        //     console.log(people[x]);
        //     if (people[x] == "Jason")
        //         break;
        //     else{
        //         console.log("erreur")
        //     }
        // }
        



        //exercice2
        //1
        let couleurPrefere=["rouge", "jaune", "blue", "vert" ,"orange"];
        for (bal in couleurPrefere){
            let bibi=Number(bal)+1;
            console.log("mon numero "+bibi +" est " +couleurPrefere[bal]) 
        } 
    
    let suffibales = ["st","nd","rd","th","th"];
	for (let bal in couleurPrefere) {
		let bibi=Number(bal)+1;
		console.log("Mbibi "+ bibi + suffibales[bal] + " choix est " + couleurPrefere[bal]);
	}

    //Exercice 3 : Répéter La Question
// Instructions
// Demandez un numéro à l’utilisateur.
// Astuce : Vérifiez le type de données que vous recevez de l’invite (c.-à-d. Utilisez la méthode)typeof

// Bien que le nombre soit inférieur à 10, continuez à demander à l’utilisateur un nouveau numéro.
// Astuce : Quelle boucle est la plus pertinente pour cette situation ?while
let users=prompt("entrer un numero")
let bib=Number(users)
if( users=!bib){
    console.log("ceci est un caractere")
}
else{
    console.log('ceci cest un nombre')
}


while (users<10){
    let users=prompt("entrer un numero")
let bi=Number(users)

    if( a=!bi){
        console.log("ceci est un caractere")
    }else{
        if(users>10){
    break
    }
    else{
        console.log('entrer un nombre sup a 10')
    }
    
}
}




// Exercice 4 : Gestion Des Bâtiments
// Instructions:
// let building = {
//     numberOfFloors : 4,
//     numberOfAptByFloor : {
//         firstFloor : 3,
//         secondFloor : 4,
//         thirdFloor : 9,
//         fourthFloor : 2,
//     },
//     nameOfTenants : ["Sarah", "Dan", "David"],
//     numberOfRoomsAndRent:  {
//         sarah: [3, 990],
//         dan :  [4, 1000],
//         david : [1, 500],
//     },
// }


// Avis Sur Les Objets
// Copiez et collez l’objet ci-dessus dans votre fichier Javascript.

// Console.log le nombre d’étages dans le bâtiment.

// Console.log combien d’appartements se trouvent aux étages 1 et 3.

// Console.log le nom du deuxième locataire et le nombre de pièces qu’il a dans son appartement.

// Vérifiez si la somme du loyer de Sarah et David est plus importante que celle de Dan. Si c’est le cas, augmentez le loyer de Dan à 1200.

let building = {
    numberOfFloors : 4,
    numberOfAptByFloor : {
        firstFloor : 3,
        secondFloor : 4,
        thirdFloor : 9,
        fourthFloor : 2,
    },
    nameOfTenants : ["Sarah", "Dan", "David"],
    numberOfRoomsAndRent:  {
        sarah: [3, 990],
        dan :  [4, 1000],
        david : [1, 500],
    },
}

console.log("le nombre d'etage est" +building.numberOfFloors)
console.log("l'appartement 1 dispose de "+building.numberOfAptByFloor.firstFloor ,"l'appartement 2 dispose de " +building.numberOfAptByFloor.thirdFloor)

console.log("le nom du deuxième locataire est ",building.nameOfTenants[1], "et le nombre de pièces qu’il a dans son appartement est ",building.numberOfRoomsAndRent.dan[0])
somme= building.numberOfRoomsAndRent.sarah[1]+building.numberOfRoomsAndRent.david[1]
let ajout=1200
let addition=ajout+building.numberOfRoomsAndRent.dan[1]
if (somme>building.numberOfRoomsAndRent.dan[1]){
    console.log(addition)

}
else{
    console.log("plus important")
}


    // Exercice 5 : Famille
    // Instructions
    // Créez un objet appelé famille avec quelques paires de valeurs clés.
    // À l’aide d’une boucle, console.log les clés de l’objet.for in
    // À l’aide d’une boucle, console.log les valeurs de l’objet.for in

    let famille={
        nom:'Ouedraogo',
        prenom:'tata',
        age:45
    }
    


    for (i in famille){
        console.log("les elementsde la clé sont :",i)
    }
    

    for (a in famille){
        console.log( "les valeurs sont :",famille[a])
    }



// Exercice 6
// Instructions
// let details = {
//   my: 'name',
//   is: 'Rudolf',
//   the: 'raindeer'
// }
// Compte tenu de l’objet ci-dessus et à l’aide d’une console , .log « mon nom est Rudolf le cerf de pluie »for loop

let details = {
    my : ' name ',
    is : ' Rudolf ',
    the : ' raindeer '
  }

  for (i in details){
    console.log( i+details[i])

  }


//   Exercice 7 : Groupe Secret
// Instructions
// let names = ["Jack", "Philip", "Sarah", "Amanda", "Bernard", "Kyle"];
// Un groupe d’amis a décidé de créer une société secrète. Le nom de la société sera la première lettre de chacun de leurs noms triés par ordre alphabétique.
// Astuce : une chaîne est un tableau de lettres
// Console.log le nom de leur société secrète. La sortie doit être « ABJKPS »

let names = ["Jack", "Philip", "Sarah", "Amanda", "Bernard", "Kyle"];
	let element = []
	for(  x in names){
		element [x] = names[x][0];
	}
	element  = element.sort();
	element  = element.join("");
	console.log(element);