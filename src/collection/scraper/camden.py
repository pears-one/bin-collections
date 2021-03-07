import requests
import re
from datetime import datetime
from typing import List
from collection import Collection
from collection.scraper import CollectionScraper
from bs4 import BeautifulSoup


class CamdenScraper(CollectionScraper):
    @staticmethod
    def __get_bin_type(bin_collection_container):
        bin_type_text = bin_collection_container.find('h3').text
        bin_type_match = re.match('Domestic (.+) collection', bin_type_text)
        return bin_type_match.group(1)

    @staticmethod
    def __get_collection_date(bin_collection_container) -> datetime.date:
        date_container = bin_collection_container.select('td.next-service')[0]
        date_container.span.extract()
        next_date_string = date_container.text.strip()
        return datetime.strptime(next_date_string, '%d/%m/%Y').date()

    def get_collections(self, uprn: str) -> List[Collection]:
        collections = []
        url = f'https://environmentservices.camden.gov.uk/property/{uprn}'
        session = requests.Session()
        resp = session.get(
            url
        )
        soup = BeautifulSoup(resp.text, 'html.parser')
        containers = soup.select('div.service-wrapper')
        for container in containers:
            bin_type = self.__get_bin_type(container)
            collection_date = self.__get_collection_date(container)
            collections.append(Collection(bin_type, collection_date))
        return collections
