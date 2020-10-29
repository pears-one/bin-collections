from collection.collection import Collection
import requests
from bs4 import BeautifulSoup
import re
from datetime import datetime
from typing import List


class CollectionScraperConfig:
    def __init__(
            self,
            request_url: str,
            request_headers: dict,
            request_body: dict,
            container_selector: str,
            bin_type_selector: str,
            bin_type_regex: str,
            date_selector: str,
            date_regex: str,
            date_format: str,
    ):
        self.__request_url = request_url
        self.__request_headers = request_headers
        self.__request_body = request_body
        self.__container_selector = container_selector
        self.__bin_type_selector = bin_type_selector
        self.__bin_type_regex = bin_type_regex
        self.__date_selector = date_selector
        self.__date_regex = date_regex
        self.__date_format = date_format

    def get_url(self):
        return self.__request_url

    def get_headers(self):
        return self.__request_headers

    def get_body(self):
        return self.__request_body

    def get_container_selector(self):
        return self.__container_selector

    def get_date_selector(self):
        return self.__date_selector

    def get_date_format(self):
        return self.__date_format

    def get_date_regex(self):
        return self.__date_regex

    def get_bin_type_selector(self):
        return self.__bin_type_selector

    def get_bin_type_regex(self):
        return self.__bin_type_regex

    @staticmethod
    def from_uprn(uprn: str):
        return CollectionScraperConfig(
            request_url='https://www.manchester.gov.uk/bincollections',
            request_headers={'User-Agent': 'Mozilla/5.0'},
            request_body={'mcc_bin_dates_uprn': uprn, 'mcc_bin_dates_submit': 'Go'},
            container_selector="div.collection",
            bin_type_selector="h3",
            bin_type_regex="(.+) Bin",
            date_selector="p.caption",
            date_regex="Next collection (.*)",
            date_format='%A %d %b %Y',
        )


class CollectionScraper:
    def __init__(self, config: CollectionScraperConfig):
        self.__config = config

    def send_request(self) -> requests.Response:
        session = requests.Session()
        return session.post(
            self.__config.get_url(),
            headers=self.__config.get_headers(),
            data=self.__config.get_body()
        )

    def get_bin_collection_containers(self):
        response = self.send_request()
        soup = BeautifulSoup(response.text, 'html.parser')
        return soup.select(self.__config.get_container_selector())

    def get_bin_type(self, bin_collection_container):
        bin_type_text = bin_collection_container.select(self.__config.get_bin_type_selector())[0].text
        bin_type_match = re.match(self.__config.get_bin_type_regex(), bin_type_text)
        return bin_type_match.group(1)

    def get_collection_date(self, bin_collection_container) -> datetime.date:
        next_date_string = bin_collection_container.select(self.__config.get_date_selector())[0].text
        date_regex_match = re.match(self.__config.get_date_regex(), next_date_string)
        return datetime.strptime(date_regex_match.group(1), self.__config.get_date_format()).date()

    def get_bin_collections(self) -> List[Collection]:
        collections = []
        containers = self.get_bin_collection_containers()
        for container in containers:
            bin_type = self.get_bin_type(container)
            collection_date = self.get_collection_date(container)
            collections.append(Collection(bin_type, collection_date))
        return collections
