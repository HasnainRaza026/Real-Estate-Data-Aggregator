from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

class Graana_Scraper:
    def __init__(self, data, driver) -> None:
        self.data = data
        self.driver = driver

        # Open a webpage
        self.driver.get("https://www.graana.com/")

        # # Refresh the page
        # self.driver.refresh()
        #
        # # Optional: Wait for the page to load again
        # self.driver.implicitly_wait(10)  # waits up to 10 seconds for elements to be present
        #
        # self.select_buy_or_rent()
        # self.select_city()
        # self.select_location()
        # self.select_property_type()
        # self.select_price()
        # if self.data.get("tab") == "homes":
        #     self.select_beds()
        # self.click_find()
        # # self.get_url()

    def select_buy_or_rent(self):
        self.driver.find_element(
                By.XPATH, f'//button[text()="{self.data.get("buy/rent").title()}"]').click()

    def select_city(self):
        self.driver.find_element(
            By.XPATH, '//*[@id="body-wrapper"]/header/div[6]/div/div[2]/div[2]/div[1]/div[1]/div[1]/div/div[1]/span').click()

        city_input = self.driver.find_element(
            By.XPATH,
            '//*[@id="body-wrapper"]/header/div[6]/div/div[2]/div[2]/div[1]/div[1]/div[1]/div/div[2]/div/div[1]/input')
        city_input.send_keys(self.data.get("city"))

        self.driver.find_element(
            By.XPATH,
            '//*[@id="body-wrapper"]/header/div[6]/div/div[2]/div[2]/div[1]/div[1]/div[1]/div/div[2]/div/div[1]/div/span/button').click()

    def select_location(self):
        location_input = self.driver.find_element(
            By.XPATH, '//*[@id="body-wrapper"]/header/div[6]/div/div[2]/div[2]/div[1]/div[1]/div[2]/div/div/div/div/div/input')
        location_input.send_keys(self.data.get("location"))

        self.driver.find_element(
            By.XPATH,
            '//*[@id="body-wrapper"]/header/div[6]/div/div[2]/div[2]/div[1]/div[1]/div[2]/div/div/div/div[2]/div/ul/div[1]/div/li/button').click()

    def select_property_type(self):
        self.driver.find_element(
            By.XPATH,
            '//*[@id="body-wrapper"]/header/div[6]/div/div[2]/div[2]/div[1]/div[2]/div[1]/div/div[1]/span').click()

        self.driver.find_element(
                By.XPATH,
                f'//li[text()="{self.data.get("tab").title()}"]').click()

        self.driver.find_element(
            By.XPATH,
            f'//li[text()="{self.data.get("property_type").title()}"]').click()

    def select_price(self):
        self.driver.find_element(
            By.XPATH,
            '//*[@id="body-wrapper"]/header/div[6]/div/div[2]/div[2]/div[1]/div[2]/div[2]/div/div[1]/span').click()

        self.driver.find_element(
                By.XPATH,
                f'//input[@id="activeNumericInput"]').send_keys(self.data.get("min_price"))

        self.driver.find_element(
                By.XPATH,
                f'//input[@id="inactiveNumericInput"]').send_keys(self.data.get("max_price"))

    def select_beds(self):
        self.driver.find_element(
            By.XPATH,
            '//*[@id="body-wrapper"]/header/div[6]/div/div[2]/div[2]/div[1]/div[2]/div[4]/div/div[1]/span').click()

        beds = self.data.get("beds")
        if beds in ("any", "none"):
            beds = "All"
        self.driver.find_element(
            By.XPATH,
            f'//button[text()="{beds}"]').click()

    def click_find(self):
        self.driver.find_element(
            By.XPATH,
            '//*[@id="body-wrapper"]/header/div[6]/div/div[2]/div[2]/div[1]/div[1]/a').click()

    def get_url(self):
        current_url = self.driver.current_url
        return current_url














