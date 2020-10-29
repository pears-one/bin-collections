from people.person import Person
from alerts.alert import Alert
from collection.bin_day import BinDay
from collection.collection_scraper import CollectionScraper, CollectionScraperConfig


class AlertCompiler:
    def __init__(self, person: Person):
        self.__person = person

    def __get_collections(self):
        scraper_config = CollectionScraperConfig.from_uprn(self.__person.get_uprn())
        scraper = CollectionScraper(scraper_config)
        return scraper.get_bin_collections()

    def __get_next_bin_day(self):
        return BinDay.get_next_from_collections(self.__get_collections())

    def get_next_alert(self):
        return Alert(self.__person, self.__get_next_bin_day())
