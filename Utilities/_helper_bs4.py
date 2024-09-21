from bs4 import BeautifulSoup
import requests
from Utilities.logger import logger

class BS4_Helper:
    def __init__(self, url):
        self.url = url

        response = self._get_html()
        if response is not None:
            logger.debug(f"Making BeautifulSoup Instance --> START")
            self.soup = BeautifulSoup(response.content, "html.parser")
            logger.debug(f"Making BeautifulSoup Instance --> SUCCESS")
        else:
            logger.error(f"Execution Ended --> Can't get HTML of [{self.url}]")

    def _get_html(self):
        try:
            logger.debug(f"Get HTML of [{self.url}] --> START")
            response = requests.get(self.url)
            response.raise_for_status()
            logger.info(f"Get HTML of [{self.url}] --> SUCCESS")
            return response
        except Exception as error:
            logger.error(f"Unable to Get HTML of [{self.url}], Execution Ended --> ERROR [{error}]")
            return None

    def get_list(self, css):
        try:
            logger.debug(f"Get list using [{css}] in [{self.url}] --> START")
            data_list = self.soup.select(css)
            logger.debug(f"Get list using [{css}] in [{self.url}] --> SUCCESS")
            return data_list
        except Exception as error:
            logger.error(f"Unable to Get list using [{css}] in [{self.url}] --> ERROR [{error}]")
            return None








