class Client:

    # konstruktor klienta
    def __init__(self, name, surname, age, phone_number):

        self._name = name
        self._surname = surname
        self._age = age
        self._phone_number = phone_number

    # textová reprezentace klienta
    def __str__(self):
        return "{} {} {} {}".format(self._name,
                                    self._surname,
                                    self._age,
                                    self._phone_number)

    # vlastnost - jméno
    @property
    def name(self):
        return self._name

    # vlastnost - příjmení
    @property
    def surname(self):
        return self._surname

    # vlastnost - věk
    @property
    def age(self):
        return self._age

    # vlastnost - telefonní číslo
    @property
    def phone_number(self):
        return self._phone_number