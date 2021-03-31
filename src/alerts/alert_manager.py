from repository.property import PropertyRepository
from repository.person import PersonRepository
from collection.scraper.factory import Factory
from model.property import Property
from model.alert import Alert
from collection.bin_day import BinDay
from typing import List
import logging
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
        alerts = []
        for prop in properties:
            try:
                alerts_for_prop = self.__get_alerts_for_property(prop)
                logging.info(f"{len(alerts_for_prop)} alerts found for {prop}")
                alerts += alerts_for_prop
            except Exception as e:
                logging.error(e)
        return alerts

    def __get_alerts_for_property(self, prop: Property):
        return [
            Alert(res, bin_day)
            for bin_day in self.__get_bin_days(prop)
            for res in self.__get_residents(prop.get_uprn())
        ]

    def __get_residents(self, uprn: str):
        residents = self.__person_repository.get_residents(uprn)
        return residents

    def __get_collections(self, prop: Property):
        scraper = Factory.new_scraper(prop.get_council())
        return scraper.get_collections(prop)

    def __get_bin_days(self, prop: Property):
        return BinDay.get_all_from_collection(self.__get_collections(prop))

    def send_messages(self, alerts: List[Alert]):
        for alert in alerts:
            self.__message_client.send_message(alert.get_message(), alert.get_number())
