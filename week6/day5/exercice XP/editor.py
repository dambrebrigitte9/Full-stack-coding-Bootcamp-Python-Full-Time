from menu import MenuItem


def  load_manager():
    obj=MenuItem("salade", 10)
    return obj

def show_user_menu():
    menu = load_manager()
    while True:
        print("\n------\t\t--------")
        print("\t MENU ")
        print("(a) Add an item ")
        print("(d) Delete an item ")
        print("(m) View the restaurant menu ")
        print("(x) Exit ")
        print("-")
        choice = input("-\t").lower()

        if choice == "a":
            add_item_to_menu(menu)
        elif choice == "d":
            remove_item_from_menu(menu)
        # elif choice == "v":
        #     show_user_menu(menu)
        elif choice == "x":
            # menu.save_to_file(menu)
            break
        elif choice == "m":
            show_restaurant_menu(menu)
        else:
            print("Your choice is not correct")


def add_item_to_menu(menu):
    try:
        Nom = input("** Item Nom:\t").replace("'","''")
        Prix = int(input("** Item Prix:\t"))
        # menu = load_manager()
        menu.Nom = Nom
        menu.Prix = Prix
        if menu.save() : 
            print("item was added successfully.")
        else:
            print("Error ! ")
    except:
        print("Your entry is not correct")

def remove_item_from_menu(menu):
    try:
        Nom = input("** Item Nom to remove:\t")
        # menu = load_manager()
        menu.Nom = Nom
        if (menu.delete()):
                return print("item was  deleted successfully.")
        return print("An error occurs")
    except:
        print("Something went wrong!")

def show_restaurant_menu(menu):
    # menu = load_manager()
    items = menu.all()
    for item in items:
        print(f"{item[0]}:\t{item[1]}")

show_user_menu()