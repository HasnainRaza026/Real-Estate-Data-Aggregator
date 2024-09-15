import time
from zameen_scraper import Zameen_Scraper
from selenium import webdriver

def search():
    driver = webdriver.Chrome()
    data = {
        'city': 'hyderabad', 'location': 'latifabad', 'tab': 'homes', 'property_type': 'flat',
        'min_price': '10000', 'max_price': '15000', 'buy/rent': 'rent', 'beds': '5'
    }
    zameen = Zameen_Scraper(data, driver)
    zameen_url = zameen.get_url()
    print(zameen_url)
    time.sleep(1000)
    driver.quit()


if __name__ == '__main__':
    search()