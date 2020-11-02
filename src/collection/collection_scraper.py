from collection.collection import Collection
import requests
from bs4 import BeautifulSoup
import re
from datetime import datetime
from typing import List
import sqlite3
from query import get_council_by_uprn
import json


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
        conn = sqlite3.connect('data/bin_collections.db')
        c = conn.cursor()
        c.execute(get_council_by_uprn, (uprn,))
        r = c.fetchone()
        conf = CollectionScraperConfig(
            r[0],
            json.loads(r[1].replace("@@UPRN@@", uprn)),
            json.loads(r[2].replace("@@UPRN@@", uprn)),
            r[3],
            r[4],
            r[5],
            r[6],
            r[7],
            r[8]
        )
        return conf


class CollectionScraper:
    def __init__(self, config: CollectionScraperConfig):
        self.__config = config

    def __send_request(self) -> requests.Response:
        session = requests.Session()
        return session.post(
            self.__config.get_url(),
            headers=self.__config.get_headers(),
            data=self.__config.get_body()
        )

    def __get_bin_collection_containers(self):
        response = self.__send_request()
        soup = BeautifulSoup(response.text, 'html.parser')
        return soup.select(self.__config.get_container_selector())

    def __get_bin_type(self, bin_collection_container):
        bin_type_text = bin_collection_container.select(self.__config.get_bin_type_selector())[0].text
        bin_type_match = re.match(self.__config.get_bin_type_regex(), bin_type_text)
        return bin_type_match.group(1)

    def __get_collection_date(self, bin_collection_container) -> datetime.date:
        next_date_string = bin_collection_container.select(self.__config.get_date_selector())[0].text
        date_regex_match = re.match(self.__config.get_date_regex(), next_date_string)
        return datetime.strptime(date_regex_match.group(1), self.__config.get_date_format()).date()

    def get_bin_collections(self) -> List[Collection]:
        collections = []
        containers = self.__get_bin_collection_containers()
        for container in containers:
            bin_type = self.__get_bin_type(container)
            collection_date = self.__get_collection_date(container)
            collections.append(Collection(bin_type, collection_date))
        return collections
