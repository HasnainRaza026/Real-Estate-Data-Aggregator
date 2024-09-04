import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options


class Zameen_Scraper:
    def __init__(self) -> None:
        driver = webdriver.Chrome()

        # Open a webpage
        driver.get("https://www.zameen.com/")


        # Refresh the page
        driver.refresh()

        # Optional: Wait for the page to load again
        driver.implicitly_wait(10)  # waits up to 10 seconds for elements to be present

        rent_button = driver.find_element(By.XPATH, '//*[@id="body-wrapper"]/header/div[6]/div/div[2]/div[1]/div/button[2]')
        rent_button.click()

        time.sleep(1000)
        driver.quit()