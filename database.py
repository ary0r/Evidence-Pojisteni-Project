class Database:

    # konstruktor databáze
    def __init__(self):

        self.__list = list()

    # textová reprezentace objektu
    def __str__(self):

        return "Databáze pojištěnců: Jméno/Přijmení/Věk/Telefonní číslo"

    # přidání klienta do databáze
    def add_client(self, client):

        self.__list.append(client)

    # výpis všech klientů
    def show_clients(self):

        for item in self.__list:
            print(item)

    # vyhledání klienta
    def search_client(self, name, surname):

        for client in self.__list:
            if client.name == name and client.surname == surname:
                print(client)

    # výpis klientů a jejich indexu
    def enumerate_database(self):

        for x, y in enumerate(self.__list):
            print(x, y)

    # vymazání klienta dle indexu
    def delete_client(self, index):

        self.__list.pop(index)
