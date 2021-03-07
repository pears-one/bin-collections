class Property:
    def __init__(self, uprn: str, postcode: str, house_number: str, street_name: str, council: str):
        self.__uprn = uprn
        self.__postcode = postcode
        self.__house_number = house_number
        self.__street_name = street_name
        self.__council = council

    def get_uprn(self):
        return self.__uprn

    def get_postcode(self):
        return self.__postcode

    def get_house_number(self):
        return self.__house_number

    def get_street_name(self):
        return self.__street_name

    def get_council(self):
        return self.__council
