import time
from Utilities._helper_selenium import Selenium_Helper
from Utilities.logger import logger
from zameen_url_scraper import Zameen_Scraper
from graana_url_scraper import Graana_Scraper

def base_url_scraper():
    logger.debug("Initialize Selenium_Helper instance --> START")
    selenium_driver = Selenium_Helper()
    logger.debug("Initialize Selenium_Helper instance --> SUCCESS")

    data = {
        'city': 'hyderabad', 'location': 'latifabad', 'tab': 'homes/residential', 'property_type': 'flat',
        'min_price': '10000', 'max_price': '25000', 'buy/rent': 'rent', 'beds': '3'
    }

    # logger.debug("Initialize Zameen_Scraper instance -->  START")
    # zameen = Zameen_Scraper(data, selenium_driver)
    # logger.debug("Initialize Zameen_Scraper instance -->  SUCCESS")
    # zameen_result_url = zameen.webpage_url()
    # print(zameen_result_url)
    #
    # logger.debug("Initialize Graana_Scraper instance -->  START")
    # graana = Graana_Scraper(data, selenium_driver)
    # logger.debug("Initialize Graana_Scraper instance -->  SUCCESS")
    # graana_result_url = graana.webpage_url()
    # print(graana_result_url)


    time.sleep(1000)
    selenium_driver.quit()


if __name__ == '__main__':
    base_url_scraper()