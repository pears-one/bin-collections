import logging
from collection.scraper.scraper import CollectionScraper
from collection.scraper.camden import CamdenScraper
from collection.scraper.manchester import ManchesterScraper

scrapers_by_name = {
    'https://www.manchester.gov.uk/bincollections': ManchesterScraper,
    'https://environmentservices.camden.gov.uk/property': CamdenScraper
}


class Factory:
    @staticmethod
    def new_scraper(council_url: str) -> CollectionScraper:
        if council_url in scrapers_by_name:
            return scrapers_by_name[council_url]()
        else:
            logging.error(f"no scraper configured for {council_url}")
            return CollectionScraper()
