class Person:
    def __init__(self, name: str, number: str, uprn: str):
        self.__name = name
        self.__number = number
        self.__uprn = uprn

    def get_uprn(self):
        return self.__uprn

    def get_number(self):
        return self.__number

    def get_name(self):
        return self.__name
