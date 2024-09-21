from Utilities.logger import logger
from Utilities._helper_bs4 import BS4_Helper

class Zameen_Data_Scraper:
    def __init__(self, url):
        self.url = url
        self.soap = BS4_Helper(self.url)

        logger.debug(f"Get Result Page data of {self.url} --> START")

        self.start_scraping_data()

    def start_scraping_data(self):
        data_list = self.get_data_list()
        # print(data_list)
        if len(data_list) > 0:
            logger.info(f"[{len(data_list)}] Data Items Found in [{self.url}]")

    def get_data_list(self):
        try:
            logger.debug(f"Get data list in [{self.url}] --> START")
            data_list = self.soap.get_list(css='li[role="article"]')
            logger.info(f"Get data list in [{self.url}] --> SUCCESS")
            return data_list
        except Exception as error:
            logger.error(f"Unable to Get data get list in [{self.url}], Execution Ended --> ERROR [{error}]")
            return None

