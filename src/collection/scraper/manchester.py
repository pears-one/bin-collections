import requests
import re
from datetime import datetime
from collection import Collection
from typing import List
from collection.scraper import CollectionScraper
from model.property import Property
from bs4 import BeautifulSoup


class ManchesterScraper(CollectionScraper):
    @staticmethod
    def __get_bin_type(bin_collection_container):
        bin_type_text = bin_collection_container.select('h3')[0].text
        bin_type_match = re.match('\s*(.+) (Bin|Container)\s*', bin_type_text)
        return bin_type_match.group(1).lower()

    @staticmethod
    def __get_collection_date(bin_collection_container) -> datetime.date:
        next_date_string = bin_collection_container.select('p.caption')[0].text
        date_regex_match = re.match('Next collection (.*)', next_date_string)
        return datetime.strptime(date_regex_match.group(1), '%A %d %b %Y').date()

    def get_collections(self, prop: Property) -> List[Collection]:
        collections = []
        url = 'https://www.manchester.gov.uk/bincollections'
        body = {
            "mcc_bin_dates_uprn": prop.get_uprn(),
            "mcc_bin_dates_submit": "Go"
        }
        session = requests.Session()
        resp = session.post(
            url,
            data=body
        )
        soup = BeautifulSoup(resp.text, 'html.parser')
        containers = soup.select('div.collection')
        for container in containers:
            bin_type = self.__get_bin_type(container)
            collection_date = self.__get_collection_date(container)
            collections.append(Collection(bin_type, collection_date))
        return collections
