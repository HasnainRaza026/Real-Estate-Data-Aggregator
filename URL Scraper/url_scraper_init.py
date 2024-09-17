import time
from Utilities._helper_selenium import Selenium_Helper
from Utilities.logger import logger
from zameen_url_scraper import Zameen_Scraper
# from graana_url_scraper import Graana_Scraper

def base_url_scraper():
    logger.debug("Initialize Selenium_Helper instance --> START")
    selenium_driver = Selenium_Helper()
    logger.debug("Initialize Selenium_Helper instance --> SUCCESS")

    data = {
        'city': 'hyderabad', 'location': 'latifabad', 'tab': 'homes', 'property_type': 'flat',
        'min_price': '10000', 'max_price': '15000', 'buy/rent': 'rent', 'beds': '5'
    }

    logger.debug("Initialize Zameen_Scraper instance -->  START")
    zameen = Zameen_Scraper(data, selenium_driver)
    logger.debug("Initialize Zameen_Scraper instance -->  SUCCESS")

    zameen_result_url = zameen.webpage_url()
    print(zameen_result_url)

    time.sleep(10)
    selenium_driver.quit()


if __name__ == '__main__':
    base_url_scraper()