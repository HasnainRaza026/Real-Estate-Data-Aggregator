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
        self.driver.reload_page()
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

            if self.data.get("buy/rent") == "buy":
                self.driver.click_element(xpath='//button[@aria-label="For sale"]')
            else:
                self.driver.click_element(xpath='//button[normalize-space()="Rent"]')

            logger.info(f"Select buy or rent in [{self.url}] --> SUCCESS")

        except Exception as error:
            logger.error(f"Unable to Select buy or rent in [{self.url}], Execution Ended --> ERROR [{error}]")

    def select_city(self):
        city = self.data.get("city")
        try:
            logger.debug(f"Select City, [{city}] in [{self.url}] --> START")

            self.driver.click_element(xpath='//div[@aria-label="City filter"]//span[@class="b94532fd"]')
            self.driver.input_text(xpath='//input[@class="e96a3e41"]', value=city)
            self.driver.click_element(xpath='//span[@class="_569dbe30"]//button[1]')

            logger.info(f"Select City [{city}] in [{self.url}] --> SUCCESS")

        except Exception as error:
            logger.error(f"Unable to Select City [{city}] in [{self.url}], Execution Ended --> ERROR [{error}]")

    def select_location(self):
        location = self.data.get("location")
        try:
            logger.debug(f"Select Location [{location}] in [{self.url}] --> START")

            self.driver.input_text(xpath='//input[@type="text"]', value=location)
            self.driver.click_element(xpath='//li[@data-selected="true"]//button[@class="_48de9e1e"]')

            logger.info(f"Select Location [{location}] in [{self.url}] --> SUCCESS")

        except Exception as error:
            logger.error(f"Unable to Select Location [{location}] in [{self.url}], Execution Ended --> ERROR [{error}]")

    def select_property_type(self):
        property_type = f"{self.data.get("tab")} - {self.data.get("property_type")}"
        try:
            logger.debug(f"Select Property Type [{property_type}] in [{self.url}] --> START")

            self.driver.click_element(xpath='//div[@aria-label="Category filter"]//span[@class="b94532fd"]')
            if self.data.get("tab") == "homes/residential":
                self.driver.click_element(xpath='//div[@class="_56cacfa2"]//li[1]')
            elif self.data.get("tab") == "plots":
                self.driver.click_element(xpath='//div[@class="_56cacfa2"]//li[2]')
            else:
                self.driver.click_element(xpath='//div[@class="_56cacfa2"]//li[3]')
            self.driver.click_element(xpath=f'//li[text()="{self.data.get("property_type").title()}"]')

            logger.info(f"Select Property Type [{property_type}] in [{self.url}] --> SUCCESS")

        except Exception as error:
            logger.error(f"Unable to Select Property Type [{property_type}] in [{self.url}], Execution Ended --> ERROR [{error}]")

    def select_price(self):
        price = f"Minimum: {self.data.get("min_price")} | Maximum {self.data.get("max_price")}"
        try:
            logger.debug(f"Select Price [{price}] in [{self.url}] --> START")

            self.driver.click_element(xpath='//div[@name="Price (PKR)"]//span[1]')
            self.driver.input_text(xpath=f'//input[@id="activeNumericInput"]', value=self.data.get("min_price"))
            self.driver.input_text(xpath=f'//input[@id="inactiveNumericInput"]', value=self.data.get("max_price"))

            logger.info(f"Select Price [{price}] in [{self.url}]  --> SUCCESS")

        except Exception as error:
            logger.error(f"Unable to Select Price [{price}] in [{self.url}], Execution Ended --> ERROR [{error}]")


    def select_beds(self):
        try:
            logger.debug(f"Select Beds in [{self.url}] --> START")

            self.driver.click_element(xpath='//div[@name="beds"]//span[1]')
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

            self.driver.click_element(xpath='//a[normalize-space()="Find"]')

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






