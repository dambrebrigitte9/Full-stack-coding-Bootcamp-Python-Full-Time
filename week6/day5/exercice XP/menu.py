# Exercice 1 : Gestionnaire De Menu De Restaurant
# Instructions
# Description: Créez un système de gestion des menus de restaurant pour un gestionnaire. Le programme doit permettre au gestionnaire d’afficher le menu, d’ajouter un élément et de supprimer un élément.



# PARTIE 1
# Dans cet exercice, nous utiliserons PostgreSQL et Python. Créez une nouvelle base de données et une nouvelle table dans pgAdmin (ou dans psql). Lisez les instructions ci-dessous avant de créer le nouveau tableau

# Créez une nouvelle classe appelée, les attributs doivent être le nom et le prix de chaque article.MenuItem

# Créer plusieurs méthodes (,,) Ces méthodes permettront à un utilisateur d’enregistrer, de supprimer et de mettre à jour des éléments de la base de données.savedeleteupdate

# Dans la classe, créez une méthode appelée qui retournera une liste de tous nosobjets.MenuItemallMenuItem

# Créez une autre méthode appelée qui retournera un objet unique en fonction de son nom, si un objet est introuvable (il n’y a pas d’élément correspondant au nom dans la méthode) retour.get_by_nameMenuItemget_by_nameNone


# Boîte de code :

# item = MenuItem('Burger', 35)
# item.save()
# item.delete()
# item.update('Veggie Burger', 37)
# item2 = MenuItem.get_by_name('Beef Stew')
# items = MenuItem.all()


# Partie 2
# Créez un fichier appelémenu_editor.py, qui aura les fonctions suivantes :
# load_manager()- Cette fonction doit créer une nouvelle instance.MenuItem

# show_user_menu()- Cette fonction doit afficher le menu du programme (pas lemenu du restaurant!), et demander à l’utilisateur de choisir un article. Appelez la fonction appropriée qui correspond à l’entrée de l’utilisateur.

# add_item_to_menu()- Cela demandera à l’utilisateur de saisir le nom et le prix de l’article. Il n’interagira pas avec le menu lui-même, mais appellera simplement la fonction appropriée à partir del’objet MenuItem.
# Si l’élément a été ajouté avec succès, imprimez un message indiquant :.item was added successfully

# remove_item_from_menu()- Cette fonction doit demander à l’utilisateur de saisir le nom de l’article qu’il souhaite supprimer du menu du restaurant. La fonction ne doit pas interagir avec le menu lui-même, mais simplement appeler la fonction appropriée à partir del’objet MenuItem.
# Si l’élément a été supprimé avec succès, imprimez un message pour informer l’utilisateur que cette opération a été effectuée.
# Si ce n’est pas le cas, imprimez un message indiquant qu’une erreur s’est produite.

# show_restaurant_menu()- imprimer lemenu du restaurant.

# Lorsque l’utilisateur choisit de quitter le programme, affichez le menu du restaurant et quittez le programme.

# Voici un exemple du menu présenté à l’utilisateur :

# Gestionnaire de menus d’exercices


# creation de la table de la  base de donnee


#      CREATE TABLE Menu(
#          Menu_id SERIAL PRIMARY KEY,
#          Nom VARCHAR(50) NOT NULL,
#          Prix numeric NOT NULL
    
#      );

import psycopg2

def connection():
    HOSTNAME = 'localhost'
    USERNAME = 'postgres'
    PASSWORD = '12345'
    DATABASE = 'restaurant'

    connection = psycopg2.connect(host=HOSTNAME, user=USERNAME, password=PASSWORD, dbname=DATABASE )
    return connection
 
class MenuItem:
    def __init__(self, Nom, Prix):
        self.Nom=Nom
        self.Prix=Prix

    def save(self):
        con = self.connection()
        cursor = con.cursor()
        query = f"Insert into items (Nom,Prix) values ('{self.Nom}',{self.Prix});"
        cursor.execute(query)
        con.commit()
        # results = cursor.fetchall()
        cursor.close()
        return True

    def delete(self):
        con = self.connection()
        cursor = con.cursor()
        query = f"Delete from items where name = '{self.Nom}';"
        cursor.execute(query)
        con.commit()
        # results = cursor.fetchall()
        cursor.close()
        return True

    def update(self,Nom, Prix):
        con=self.connection()
        cursor=con.xursor()
        query=f"Update items set name = '{Nom}',price = {Prix} where name = '{self.Nom}';"
        cursor.execute(query)
        con.commit()
        result=cursor.fetchall()
        cursor.close()
        return result
        

    def MenuItemallMenuItem(self):
        conn=self.connexion
        cursor=conn.cursor()
        query="select Nom ,Prix from MenuItem;"
        cursor.execute(query)
        conn.commit()
        results=cursor.fetchall()
        cursor.close()
        return results

    def get_by_nameMenuItemget_by_nameNone(entier,Nom):
        conn=entier.connection()
        cursor=conn.cursor()
        query=f"selct Name,Prix from itemq where name ilike '{Nom}';"
        cursor.execute(query)
        result=cursor.fetchall()
        print (result)
        cursor.close()
        if len(result) > 0:
            return entier(result[0][0],result[0][1])
            return None

