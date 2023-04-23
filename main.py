from clients import Client
from database import Database
import pickle
import os


# vyčistí okno aplikace
def clear():
    os.system("cls")


# uloží databázi do souboru
def save_database(openable, obj):
    try:
        with open(openable, "wb") as file:
            pickle.dump(obj, file)
            print("Databáze uložena.")
    except Exception as error:
        print(error)


# funkce pro zadání čísla
def get_number(text=""):
    error = "Chybné zadání, zadejte číslo."
    run = True
    while run:
        try:
            x = int(input(text))
            run = False
            return x
        except ValueError:
            print(error)
        except TypeError:
            print(error)


# kostra programu
def main():
    run = True
    while run:

        # textová reprezentace volby operace
        print(" ------------------------\n",
              "  Evidence pojištěných\n",
              "------------------------\n",
              "Vyberte požadovanou akci:\n",
              "1 - Přidat pojištěného\n",
              "2 - Vypsat všechny pojištěné\n",
              "3 - Vyhledat pojištěného\n",
              "4 - Vymazat pojištěnce\n",
              "5 - Ukončit aplikaci\n",
              "------------------------"
              )

        # zadání požadované operace
        operation_number = get_number()

        # přidání klienta
        if operation_number == 1:
            new_client = Client(input("Zadej jméno klienta: "),
                                input("Zadej příjmení klienta: "),
                                input("Zadej věk klienta: "),
                                input("Zadej telefonní číslo klienta: "))
            evidence.add_client(new_client)
            save_database(current_file, evidence)

        # seznam klientů
        elif operation_number == 2:
            evidence.show_clients()

        # vyhledávání klientů
        elif operation_number == 3:
            name = input("Zadej jméno: ")
            surname = input("Zadej příjmení: ")
            name = name.lower().capitalize().strip()
            surname = surname.lower().capitalize().strip()
            evidence.search_client(name, surname)

        # vymazání klienta
        elif operation_number == 4:
            evidence.enumerate_database()
            go = True
            error_msg = "Index mimo rozsah!"
            while go:
                try:
                    index = get_number(text="Zadej index klienta k vymazání: ")
                    if 0 <= index <= evidence.database_length:
                        evidence.delete_client(index)
                        save_database(current_file, evidence)
                        go = False
                    else:
                        print(error_msg)
                except Exception:
                    print(error_msg)

        elif operation_number == 5:
            run = False

        input("Pokračujte libovolnou klávesou...")

        clear()


# název souboru pro uložení objektu databáze
current_file = "pojistenci.pkl"
# pokusí se otevřít soubor pro načtení databáze, jinak vytvoří novou instanci
try:
    with open(current_file, "rb") as file:
        evidence = pickle.load(file)
        print("Databáze načtena.")
except FileNotFoundError:
    evidence = Database()
    print("Nepodařilo se načíst databázi ze souboru.")

if __name__ == "__main__":
    main()
