import requests
from datetime import datetime
from collection import Collection
from typing import List
from collection.scraper.scraper import CollectionScraper
from model.property import Property
from bs4 import BeautifulSoup
import logging


class Week:
    def __init__(self, colour: str, bins: List[str]):
        self.__colour = colour
        self.__bins = bins

    def get_colour(self):
        return self.__colour

    def get_bins(self):
        return self.__bins


class SwanseaScraper(CollectionScraper):
    weeks_by_bg_colour = {
        "ForestGreen": Week("Green", ['paper and card', 'glass and cans', 'food waste', 'garden waste']),
        "MediumVioletRed": Week("Pink", ['plastic', 'non recyclables', 'food waste'])
    }

    def __send_request(self, prop: Property):
        url = "http://www1.swansea.gov.uk/recyclingsearch/?lang=eng"
        session = requests.Session()
        resp = session.get(
            url
        )
        soup = BeautifulSoup(resp.text, 'html.parser')
        form = {a['name']: a['value'] if 'value' in a.attrs else '' for a in soup.find_all('input')}
        form['txtPostCode'] = prop.get_postcode()
        return session.post(
            url,
            data=form
        )

    def __get_collections_in_month(self, month) -> List[Collection]:
        month_name = ' ' + month.find('b').text
        collections = []
        for bg_colour, week in self.weeks_by_bg_colour.items():
            dates = [datetime.strptime(d.text + month_name, '%d %B %Y').date() for d in month.find_all('td', attrs={'bgcolor': bg_colour})]
            for d in dates:
                collections += [Collection(t, d) for t in week.get_bins()]
        return collections

    def get_collections(self, prop: Property) -> List[Collection]:
        collections = []
        try:
            resp = self.__send_request(prop)
        except Exception as e:
            logging.error(f"failed to send request for property {str(prop)}: {e}")
            return collections
        soup = BeautifulSoup(resp.text, 'html.parser')
        months = soup.find_all('table', attrs={'title': 'Calendar'})
        for month in months[:2]:
            try:
                collections += self.__get_collections_in_month(month)
            except Exception as e:
                logging.warning(f"failed to get collections for {month.find('b').text} for property {str(prop)}")
        return collections
