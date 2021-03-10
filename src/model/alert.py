from model.person import Person
from datetime import date
from collection.bin_day import BinDay
from typing import List


class Alert:
    def __init__(self, person: Person, bin_day: BinDay):
        self.__person = person
        self.__bin_day = bin_day

    def get_person(self):
        return self.__person

    def get_date(self):
        return self.__bin_day.get_collection_date()

    def get_message(self):
        bins = self.__bin_day.get_bin_types()
        date_string = self.__format_date(self.get_date())
        msg = f"Hi {self.get_person().get_name()}, "
        msg += f"the {self.__nice_join(bins)} bins are getting collected on {date_string}."
        return msg

    @staticmethod
    def __nice_join(things: List[str]) -> str:
        if len(things) > 1:
            last_thing = things.pop()
            things.append(f"{things.pop()} and {last_thing}")
        return ', '.join(things)

    @staticmethod
    def __format_date(d: date) -> str:
        n = d.day
        ordinal = str(n) + {1: 'st', 2: 'nd', 3: 'rd'}.get(10 <= (n % 100) <= 20 and n or n % 10, 'th')
        return d.strftime(f'%A, {ordinal} %B')
