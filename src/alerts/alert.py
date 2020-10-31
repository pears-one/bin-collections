from people.person import Person
from collection.bin_day import BinDay


class Alert:
    def __init__(self, person: Person, bin_day: BinDay):
        self.__person = person
        self.__bin_day = bin_day

    def get_person(self):
        return self.__person

    def get_date(self):
        return self.__bin_day.get_collection_date()

    def get_message(self):
        return f"Hi {self.get_person().get_name()}, the {', '.join(self.__bin_day.get_bin_types())} bins are getting collected on {self.get_date()}"
