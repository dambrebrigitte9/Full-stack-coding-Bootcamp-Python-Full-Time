-- Exercice 2 : Location De DVD
-- Instructions
-- Utilisez UPDATE pour changer la langue de certains films. Assurez-vous d’utiliser des langues valides.

-- Quelles clés étrangères (références) sont définies pour la table client ? Comment cela affecte-t-il la façon dont nous INSÉRONS dans la table client ?

-- Nous avons créé une nouvelle table appelée customer_review. Déposez ce tableau. Est-ce une étape facile ou nécessite-t-elle une vérification supplémentaire?

-- Découvrez combien de locations sont encore en suspens (c’est-à-dire qu’elles n’ont pas encore été retournées au magasin).

-- Trouvez les 30 films les plus chers qui sont exceptionnels (c’est-à-dire qui n’ont pas encore été retournés au magasin)

-- Votre ami est au magasin et décide de louer un film. Il sait qu’il veut voir 4 films, mais il ne se souvient pas de leurs noms. Pouvez-vous l’aider à trouver les films qu’il veut louer ?
-- Le 1er film : Le film parle d’une lutteuse de sumo, et l’une des actrices est Penelope Monroe.

-- Le 2ème film : Un court documentaire (moins d'1 heure), noté « R ».

-- Le 3ème film : Un film que son ami Matthew Mahan a loué. Il a payé plus de 4,00 $ pour la location, et il l’a retourné entre le 28 juillet et le 1er août 2005.

-- Le 4ème film : Son ami Matthew Mahan a également regardé ce film. Il avait le mot « bateau » dans le titre ou la description, et il semblait que c’était un DVD très coûteux à remplacer.
UPDATE language set name ='espagnol' where language_id = 2;
UPDATE language set name ='chinois' where language_id = 3

