import unittest
from clients import Client
from database import Database


class TestClients(unittest.TestCase):

    # otestuje vytvoření nového klienta
    def test_new_client(self):
        client = Client("Name", "Surname", "10", "100200300")
        self.assertEqual("Name", client.name)
        self.assertEqual("Surname", client.surname)
        self.assertEqual("10", client.age)
        self.assertEqual("100200300", client.phone_number)

    # otestuje textovou repre. klienta
    def test_print_client(self):
        client = Client("A", "B", "1", "200300200")
        self.assertEqual("A B 1 200300200", client.__str__())

    # otestuje vlastnosti klienta
    def test_client_properties(self):
        client = Client("A", "B", "C", "D")
        self.assertEqual("A", client.name)
        self.assertEqual("B", client.surname)
        self.assertEqual("C", client.age)
        self.assertEqual("D", client.phone_number)

    # otestuje přidání klientů do databáze
    def test_add_client(self):
        database = Database()
        for each in range(5):
            client = Client("A", "B", "C", "D")
            database.add_client(client)
        self.assertEqual(5, database.database_length)

    # testuje vymazání klienta
    def test_delete_client(self):
        database = Database()
        for each in range(5):
            client = Client("A", "B", "C", "D")
            database.add_client(client)
        self.assertEqual(5, database.database_length)
        for each in range(3):
            index = 0
            database.delete_client(index)
            index += 1
        self.assertEqual(2, database.database_length)


if __name__ == '__main__':
    unittest.main()
