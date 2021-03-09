from repository.property import PropertyRepository
from repository.person import PersonRepository
from collection.scraper import Factory
from model.property import Property
from model.alert import Alert
from collection.bin_day import BinDay
from messaging.text_client import TextClient


class AlertManager:
    def __init__(
            self,
            property_repository: PropertyRepository,
            person_repository: PersonRepository,
            message_client: TextClient
    ):
        self.__property_repository = property_repository
        self.__person_repository = person_repository
        self.__message_client = message_client

    def get_alerts(self):
        properties = self.__property_repository.get_properties()
        alerts = [
            Alert(res, self.__get_next_bin_day(prop))
            for prop in properties
            for res in self.__get_residents(prop.get_uprn())
        ]
        return alerts

    def __get_residents(self, uprn: str):
        residents = self.__person_repository.get_residents(uprn)
        return residents

    def __get_collections(self, prop: Property):
        scraper = Factory.new_scraper(prop.get_council())
        return scraper.get_collections(prop)

    def __get_next_bin_day(self, prop: Property):
        return BinDay.get_next_from_collections(self.__get_collections(prop))

    def send_messages(self, alerts):
        for alert in alerts:
            self.__message_client.send_message(alert.get_message(), alert.get_person().get_number())
