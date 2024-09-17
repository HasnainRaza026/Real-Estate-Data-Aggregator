from Utilities.logger import logger
class Zameen_Scraper:
    def __init__(self, data, selenium_driver):
        self.data = data
        self.driver = selenium_driver
        self.url = "https://www.zameen.com/"

        logger.debug(f"Get Result Page url of {self.url} --> START")

        self.start_scraping()

    def start_scraping(self):
        # Open "https://www.zameen.com/" webpage
        self.driver.goto_page(url=self.url)
        logger.info(f"Open Webpage {self.url} --> SUCCESS")

        # Refresh the page to remove popup ads
        self.driver.reload_page(url=self.url)
        logger.info(f"Reload Webpage {self.url} --> SUCCESS")

        self.select_buy_or_rent()
        self.select_city()
        self.select_location()
        self.select_property_type()
        self.select_price()

        if self.data.get("tab") == "homes":
            self.select_beds()

        self.click_find()

    def select_buy_or_rent(self):
        try:
            logger.debug(f"Select buy or rent in [{self.url}] --> START")

            self.driver.click_element(xpath=f'//button[text()="{self.data.get("buy/rent").title()}"]')

            logger.info(f"Select buy or rent in [{self.url}] --> SUCCESS")

        except Exception as error:
            logger.error(f"Unable to Select buy or rent in [{self.url}], Execution Ended --> ERROR [{error}]")

    def select_city(self):
        try:
            logger.debug(f"Select City in [{self.url}] --> START")

            self.driver.click_element(xpath='//*[@id="body-wrapper"]/header/div[6]/div/div[2]/div[2]/div[1]/div[1]/div[1]/div/div[1]/span')
            self.driver.input_text(xpath='//*[@id="body-wrapper"]/header/div[6]/div/div[2]/div[2]/div[1]/div[1]/div[1]/div/div[2]/div/div[1]/input', value=self.data.get("city"))
            self.driver.click_element(xpath='//*[@id="body-wrapper"]/header/div[6]/div/div[2]/div[2]/div[1]/div[1]/div[1]/div/div[2]/div/div[1]/div/span/button')

            logger.info(f"Select City in [{self.url}] --> SUCCESS")

        except Exception as error:
            logger.error(f"Unable to Select City in [{self.url}], Execution Ended --> ERROR [{error}]")

    def select_location(self):
        try:
            logger.debug(f"Select Location in [{self.url}] --> START")

            self.driver.input_text(xpath='//*[@id="body-wrapper"]/header/div[6]/div/div[2]/div[2]/div[1]/div[1]/div[2]/div/div/div/div/div/input', value=self.data.get("location"))
            self.driver.click_element(xpath='//*[@id="body-wrapper"]/header/div[6]/div/div[2]/div[2]/div[1]/div[1]/div[2]/div/div/div/div[2]/div/ul/div[1]/div/li/button')

            logger.info(f"Select Location in [{self.url}] --> SUCCESS")

        except Exception as error:
            logger.error(f"Unable to Select Location in [{self.url}], Execution Ended --> ERROR [{error}]")

    def select_property_type(self):
        try:
            logger.debug(f"Select Property Type in [{self.url}] --> START")

            self.driver.click_element(xpath='//*[@id="body-wrapper"]/header/div[6]/div/div[2]/div[2]/div[1]/div[2]/div[1]/div/div[1]/span')
            self.driver.click_element(xpath=f'//li[text()="{self.data.get("tab").title()}"]')
            self.driver.click_element(xpath=f'//li[text()="{self.data.get("property_type").title()}"]')

            logger.info(f"Select Property Type in [{self.url}] --> SUCCESS")

        except Exception as error:
            logger.error(f"Unable to Select Property Type in [{self.url}], Execution Ended --> ERROR [{error}]")

    def select_price(self):
        try:
            logger.debug(f"Select Price in [{self.url}] --> START")

            self.driver.click_element(xpath='//*[@id="body-wrapper"]/header/div[6]/div/div[2]/div[2]/div[1]/div[2]/div[2]/div/div[1]/span')
            self.driver.input_text(xpath=f'//input[@id="activeNumericInput"]', value=self.data.get("min_price"))
            self.driver.input_text(xpath=f'//input[@id="inactiveNumericInput"]', value=self.data.get("max_price"))

            logger.info(f"Select Price in [{self.url}]  --> SUCCESS")

        except Exception as error:
            logger.error(f"Unable to Select Price in [{self.url}], Execution Ended --> ERROR [{error}]")


    def select_beds(self):
        try:
            logger.debug(f"Select Beds in [{self.url}] --> START")

            self.driver.click_element(xpath='//*[@id="body-wrapper"]/header/div[6]/div/div[2]/div[2]/div[1]/div[2]/div[4]/div/div[1]/span')
            beds = self.data.get("beds")
            if beds in ("any", "none"):
                beds = "All"
            self.driver.click_element(xpath=f'//button[text()="{beds}"]')

            logger.info(f"Select Beds in [{self.url}] --> SUCCESS")

        except Exception as error:
            logger.error(f"Unable to Select Beds in [{self.url}], Execution Ended --> ERROR [{error}]")

    def click_find(self):
        try:
            logger.debug(f"Click Find in [{self.url}] --> START")

            self.driver.click_element(xpath='//*[@id="body-wrapper"]/header/div[6]/div/div[2]/div[2]/div[1]/div[1]/a')

            logger.info(f"Click Find in [{self.url}] --> SUCCESS")

        except Exception as error:
            logger.error(f"Unable to Click Find in [{self.url}], Execution Ended --> ERROR [{error}]")

    def webpage_url(self):
        try:
            logger.debug(f"Get Result Page url in [{self.url}] --> START")

            result_page_url = self.driver.get_url()

            if result_page_url is not None:
                logger.info(f"Get Result Page url in [{self.url}] --> SUCCESS")
                return result_page_url
            else:
                logger.error(f"Unable to Get Result Page url in [{self.url}], Execution Ended --> ERROR [Returned url is none]")
                return None

        except Exception as error:
            logger.error(f"Unable to Get Result Page url in {self.url}, Execution Ended --> ERROR [{error}]")
            return None






