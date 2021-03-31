from model.person import Person
from datetime import date
from collection.bin_day import BinDay
from typing import List


class AlertError(Exception):
    def __init__(self, message: str, uprn: str, bins: List[str], collection_date: date):
        self.message = message
        self.bins = bins
        self.uprn = uprn
        self.collection_date = collection_date

    def __str__(self):
        return f"{self.message}: {self.bins} bins at {self.uprn} on {self.collection_date}"


class Alert:
    def __init__(self, person: Person, bin_day: BinDay):
        self.__person = person
        self.__bin_day = bin_day

    def get_name(self):
        return self.__person.get_name()

    def get_uprn(self):
        return self.__person.get_uprn()

    def get_number(self):
        return self.__person.get_number()

    def get_date(self):
        return self.__bin_day.get_collection_date()

    def get_bins(self):
        return self.__bin_day.get_bin_types()

    def get_message(self):
        bins = self.get_bins()
        if len(bins) < 1:
            raise AlertError("no bin types found in the bin day", self.get_uprn(), self.get_bins(), self.get_date())
        collection_date = self.get_date()
        if collection_date < date.today():
            raise AlertError("collection date is in the past", self.get_uprn(), self.get_bins(), self.get_date())
        date_string = self.__format_date(collection_date)
        msg = f"Hi {self.get_name()}, "
        msg += f"the {self.__nice_join(bins)} bins are getting collected on {date_string}."
        return msg

    @staticmethod
    def __nice_join(things: List[str]) -> str:
        return things[0] if len(things) == 1 else ' and '.join([', '.join([c for c in things[:-1]]), things[-1]])

    @staticmethod
    def __format_date(d: date) -> str:
        n = d.day
        ordinal = str(n) + {1: 'st', 2: 'nd', 3: 'rd'}.get(10 <= (n % 100) <= 20 and n or n % 10, 'th')
        return d.strftime(f'%A, {ordinal} %B')
