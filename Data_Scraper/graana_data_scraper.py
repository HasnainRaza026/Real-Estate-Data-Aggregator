from Utilities.logger import logger
from Utilities._helper_bs4 import BS4_Helper

class Graana_Data_Scraper:
    def __init__(self, url):
        self.url = url
        self.soap = BS4_Helper(self.url)
        self.data = None

        logger.debug(f"Get Result Page data of {self.url} --> START")

        self.start_scraping_data()

    def start_scraping_data(self):
        data_list = self.get_data_list()
        if len(data_list) > 0:
            logger.info(f"{len(data_list)} Data Items Found in [{self.url}]")

            self.data = self.soap.get_data(data_list=data_list, url_css='a', price_css='span[aria-label="Price"]',
                               location_css='div[aria-label="Location"]', beds_css='span[aria-label="Beds"]',
                               baths_css='span[aria-label="Baths"]', images_css='img[aria-label="Listing photo"]')

    def get_data_list(self):
        try:
            logger.debug(f"Get data list in [{self.url}] --> START")
            data_list = self.soap.get_list(list_css='li[role="article"]')
            logger.info(f"Get data list in [{self.url}] --> SUCCESS")
            return data_list
        except Exception as error:
            logger.error(f"Unable to Get data get list in [{self.url}], Execution Ended --> ERROR [{error}]")
            return None

