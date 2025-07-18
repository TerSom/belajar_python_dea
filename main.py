from games import cuypy
from tools import warung
from libs import welcomeMessage,exitProgaram

def menu():
    user_option = int(input(f"menu programnya:\n1. Games CUYPY\n2. Warung Mini\n3. keluar program\nsilahkan pilih : "))
    
    if user_option == 1:
        cuypy.start()
    elif user_option == 2:
        warung.start()
    elif user_option == 3:
        exitProgaram()
    else:
        print("harus pilih yang ada di menus saja")
     

def main():
    welcomeMessage()
    menu()
    
if __name__ == "__main__":
    main()