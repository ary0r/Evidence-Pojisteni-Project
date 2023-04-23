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


class TestDatabase(unittest.TestCase):

    def test_add_client(self):
        database = Database()
        client = Client("Name", "Surname", "Age", "Phone_Number")
        database.add_client(client)




if __name__ == '__main__':
    unittest.main()
