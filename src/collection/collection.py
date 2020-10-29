from datetime import date, timedelta


class Collection:
    def __init__(self, bin_type: str, collection_date: date):
        self.__bin_type = bin_type
        self.__collection_date = collection_date

    def get_bin_type(self):
        return self.__bin_type

    def get_date(self):
        return self.__collection_date

    def is_tomorrow(self) -> bool:
        return self.get_date() == date.today() + timedelta(1)

    def __str__(self):
        return "< " + str(self.__bin_type) + "  on  " + str(self.__collection_date) + " >"

    def __repr__(self):
        return "< " + str(self.__bin_type) + "  on  " + str(self.__collection_date) + " >"
