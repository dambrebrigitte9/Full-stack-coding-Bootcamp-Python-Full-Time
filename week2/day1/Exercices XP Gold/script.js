//exerce1
let colors = ["my","favorite","color","is","blue"];
let colorsPrefer=colors.join(' ');
console.log(colorsPrefer);//my,favorite,color,is,blue

//exercice2
//1.Créez 2 variables. Les valeurs doivent être des chaînes. Par exemple:
let bibi='fille';
let eudes='garcons';
//2. Découpez et échangez les 2 premiers caractères des deux chaînes de la partie 1.
let bibie=bibi.replace("fi","ga");
let eude=eudes.replace("ga", "fi");
console.log(eude+' ' +bibie);
//let str3= bibie+eude;
//3.Créez une troisième variable où la valeur est la concaténation des deux chaînes de la partie 1 (séparées par un espace).
let nom=bibie+' '+eude+' ';
//4.Enfin console.log la nouvelle chaîne concaténée.
console.log(nom)// 'fille garcons';

//exercice3
let a=prompt("entrer votre premiere valeur");
num1 =Number(a);
let b=prompt("entrer votre deuxieme valeur");
num2=Number(b);
alert(`La somme de ${num1} et de ${num2} est ${num1+num2}`);
alert(`La soustraction de ${num1} et de ${num2} est ${num1-num2}`);
alert(`La multiplication de ${num1} et de ${num2} est ${num1*num2}`);
alert(`la division de ${num1} et de ${num2} est ${num1/num2}`);


