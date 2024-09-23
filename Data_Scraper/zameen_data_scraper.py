import math

from Utilities.logger import logger
from Utilities._helper_bs4 import BS4_Helper

class Zameen_Data_Scraper:
    def __init__(self, url):
        self.url = url
        self.soap = BS4_Helper(self.url, zameen=True)
        self.data = None

        logger.debug(f"Get Result Page data of {self.url} --> START")

        self.start_scraping_data()

    def start_scraping_data(self):
        total_properties = self.soap.total_properties_found(property_css='h1')
        pages = math.ceil(total_properties/25)  # Rounding up to the next whole number
        logger.info(f"{total_properties} Total Properties found, split into {pages} Pages in {self.url}")
        for page in range(pages):
            self.data = self.soap.get_data(url=self.url, page=page, list_css='li[role="article"]', url_css='a',
                            price_css='span[aria-label="Price"]', location_css='div[aria-label="Location"]',
                            beds_css='span[aria-label="Beds"]', baths_css='span[aria-label="Baths"]',
                            images_css='img[aria-label="Listing photo"]')
            self.url = self.url.replace(f"-{page+1}.html", f"-{page+2}.html")
            logger.info(f"Scrap Property Data from Page {page+1} --> SUCCESS")

        self.data = self.soap.data


