from Utilities import logger

class Lamudi_URL_Scraper:
    def __init__(self, data, selenium_driver):
        self.data = data
        self.driver = selenium_driver
        self.url = "https://www.lamudi.pk/"

        logger.debug(f"Get Result Page url of {self.url} --> START")

        self.start_scraping_url()

    def start_scraping_url(self):
        # Open "https://www.lamudi.pk/" webpage
        self.driver.goto_page(url=self.url)
        logger.info(f"Open Webpage {self.url} --> SUCCESS")

        self.select_buy_or_rent()
        self.select_location()
        self.select_property_type()
        self.select_price()

        if self.data.get("tab") == "homes/residential":
            self.select_beds()
        self.click_find()

    def select_buy_or_rent(self):
        type = self.data.get("buy/rent")
        try:
            logger.debug(f"Select [{type}] in [{self.url}] --> START")

            if self.data.get("buy/rent") == "buy":
                self.driver.click_element(xpath='//button[translate(normalize-space(text()), "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "abcdefghijklmnopqrstuvwxyz")= "buy"]')
            else:
                self.driver.click_element(xpath='//button[translate(normalize-space(text()), "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "abcdefghijklmnopqrstuvwxyz")= "rent"]')

            logger.info(f"Select [{type}] in [{self.url}] --> SUCCESS")

        except Exception as error:
            logger.error(f"Unable to Select [{type}] in [{self.url}], Execution Ended --> ERROR [{error}]")

    def select_location(self):
        location = f"{self.data.get("location")}, {self.data.get("city")}"
        try:
            logger.debug(f"Select Complete Location [{location}] in [{self.url}] --> START")

            self.driver.click_element(xpath='//button[@class="dropdown-menu_dropdownTrigger__1QLc2 dropdown-menu_btn__2S9UB"]')
            self.driver.input_text(xpath='//input[contains(translate(normalize-space(@placeholder), "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "abcdefghijklmnopqrstuvwxyz"), "city")]', value=self.data.get("city"))
            self.driver.click_element(xpath='//div[@class="autocomplete_menuList__dlG0j"]/div[1]')

            self.driver.input_text(xpath='//input[contains(translate(normalize-space(@placeholder), "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "abcdefghijklmnopqrstuvwxyz"), "location")]', value=self.data.get("location"))
            self.driver.click_element(xpath='//li[@class="autocomplete_item__1rTbD"][1]')

            logger.info(f"Select Complete Location [{location}] in [{self.url}] --> SUCCESS")

        except Exception as error:
            logger.error(f"Unable to Select Complete Location [{location}] in [{self.url}], Execution Ended --> ERROR [{error}]")

    def select_property_type(self):
        property_type = f"{self.data.get("tab")} - {self.data.get("property_type")}"
        try:
            logger.debug(f"Select Property Type [{property_type}] in [{self.url}] --> START")

            self.driver.click_element(xpath='//div[@class="home-filters_moreFiltersList__5iqDV flex  flex-ycenter u-spbwx8"]//button[@class="dropdown-menu_dropdownTrigger__1QLc2"][1]')
            if self.data.get("tab") == "homes/residential":
                self.driver.click_element(xpath='//div[contains(@role,"tab")][contains(translate(normalize-space(text()), "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "abcdefghijklmnopqrstuvwxyz"), "homes")]')
            elif self.data.get("tab") == "plots":
                self.driver.click_element(xpath='//div[contains(@role,"tab")][contains(translate(normalize-space(text()), "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "abcdefghijklmnopqrstuvwxyz"), "plots")]')
            else:
                self.driver.click_element(xpath='//div[contains(@role,"tab")][contains(translate(normalize-space(text()), "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "abcdefghijklmnopqrstuvwxyz"), "commercial")]')
            self.driver.click_element(xpath=f'//div[contains(@role,"tabpanel")]//div[translate(normalize-space(text()), "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "abcdefghijklmnopqrstuvwxyz")= "{self.data.get("property_type")}s"]')

            logger.info(f"Select Property Type [{property_type}] in [{self.url}] --> SUCCESS")

        except Exception as error:
            logger.error(f"Unable to Select Property Type [{property_type}] in [{self.url}], Execution Ended --> ERROR [{error}]")

    def select_price(self):
        price = f"Minimum: {self.data.get("min_price")} | Maximum {self.data.get("max_price")}"
        try:
            logger.debug(f"Select Price [{price}] in [{self.url}] --> START")

            self.driver.click_element(xpath='//button[contains(translate(normalize-space(text()), "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "abcdefghijklmnopqrstuvwxyz"), "price")]')
            self.driver.input_text(xpath=f'//div[contains(@class,"home-filters_tabContainer__5eU2C")]//input[contains(translate(@name, "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "abcdefghijklmnopqrstuvwxyz"),"min")]', value=self.data.get("min_price"), backspace=True)
            self.driver.input_text(xpath=f'//div[contains(@class,"home-filters_tabContainer__5eU2C")]//input[contains(translate(@name, "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "abcdefghijklmnopqrstuvwxyz"),"max")]', value=self.data.get("max_price"), backspace=True)
            self.driver.click_element(xpath='//div[contains(@class,"home-filters_tabContainer__5eU2C")]//button[contains(@type,"button")][translate(normalize-space(text()), "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "abcdefghijklmnopqrstuvwxyz")="done"]')

            logger.info(f"Select Price [{price}] in [{self.url}] --> SUCCESS")

        except Exception as error:
            logger.error(f"Unable to Select Price [{price}] in [{self.url}], Execution Ended --> ERROR [{error}]")


    def select_beds(self):
        try:
            logger.debug(f"Select Beds in [{self.url}] --> START")

            self.driver.click_element(xpath='//button[contains(translate(text(), "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "abcdefghijklmnopqrstuvwxyz"), "beds")]')
            beds = self.data.get("beds")
            if beds in ("any", "none"):
                beds = "studio"
            elif beds in ("6", "7", "8", "9", "10+"):
                beds = "6+"
            self.driver.click_element(xpath=f'//div[translate(normalize-space(text()), "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "abcdefghijklmnopqrstuvwxyz")= "{beds}"]')
            # self.driver.scroll_down(pixels=200)
            self.driver.click_element(xpath='//div[contains(@class,"dropdown-menu_dropdownContainer__2F9CT dropdown-menu_active__2o-p0")]//button[contains(@type,"button")][translate(normalize-space(text()), "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "abcdefghijklmnopqrstuvwxyz")= "done"]')

            logger.info(f"Select Beds in [{self.url}] --> SUCCESS")

        except Exception as error:
            logger.error(f"Unable to Select Beds in [{self.url}], Execution Ended --> ERROR [{error}]")

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

    def click_find(self):
        try:
            logger.debug(f"Click Find in [{self.url}] --> START")

            self.driver.click_element(xpath='//button[contains(translate(text(), "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "abcdefghijklmnopqrstuvwxyz"), "search")]')

            logger.info(f"Click Find in [{self.url}] --> SUCCESS")

        except Exception as error:
            logger.error(f"Unable to Click Find in [{self.url}], Execution Ended --> ERROR [{error}]")






