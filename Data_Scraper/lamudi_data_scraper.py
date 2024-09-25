import math

from Utilities.logger import logger
from Utilities._helper_bs4 import BS4_Helper

class Lamudi_Data_Scraper:
    def __init__(self, url):
        self.url = url
        self.soap = BS4_Helper(self.url, lamudi=True)
        self.data = None

        logger.debug(f"Get Result Page data of {self.url} --> START")

        self.start_scraping_data()

    def start_scraping_data(self):
        total_properties = self.soap.total_properties_found(property_css='div[class="flex flexYcenter flexBetween u-mb8"] div')
        pages = math.ceil(total_properties/25)  # Rounding up to the next whole number
        logger.info(f"{total_properties} Total Properties found, split into {pages} Pages in {self.url}")
        for page in range(pages):
            self.data = self.soap.get_data(url=self.url, page=page, list_css='div[class="card-horizontal_cardHorizontal__OzX3s"]',
                            url_css='a', price_css='h4',
                            location_css='div[class="card-horizontal_cardSubTitle__3FJyc"]', beds_css='div[class="card-horizontal_cardSpecs__3U-Ym"] div',
                            baths_css='div[class="card-horizontal_cardSpecs__3U-Ym"] div',
                            images_css='figure[class="card-horizontal_imgSlides__2NL7C"]')  # Can't found image
            if page+1 == 1:
                self.url = self.url + f"?page={page+1}"
            self.url = self.url.replace(f"?page={page+1}", f"?page={page+2}")
            logger.info(f"Scrap Property Data from Page {page+1} --> SUCCESS")

        # self.data = self.soap.data


