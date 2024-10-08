from Utilities.logger import logger

class Graana_URL_Scraper:
    def __init__(self, data, selenium_driver):
        self.data = data
        self.driver = selenium_driver
        self.url = "https://www.graana.com/sale/residential-properties-sale-hyderabad-183/"

        logger.debug(f"Get Result Page url of {self.url} --> START")

        self.start_scraping_url()

    def start_scraping_url(self):
        # Open "https://www.graana.com/" webpage
        self.driver.goto_page(url=self.url)
        logger.info(f"Open Webpage {self.url} --> SUCCESS")

        self.select_complete_location()
        self.select_buy_or_rent()
        self.select_property_type()
        self.select_price()

        if self.data.get("tab") == "homes/residential":
            self.select_beds()

    def select_buy_or_rent(self):
        try:
            logger.debug(f"Select buy or rent in [{self.url}] --> START")

            self.driver.click_element(xpath='//body/div[@id="__next"]/div[@class="MuiBox-root mui-style-1uxvpob"]/div/div/div[1]/div[1]/button[1]')
            if self.data.get("buy/rent") == "buy":
                self.driver.click_element(xpath='//li[contains(translate(normalize-space(@value), "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "abcdefghijklmnopqrstuvwxyz"), "buy")]')
            else:
                self.driver.click_element(xpath='//li[contains(translate(normalize-space(@value), "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "abcdefghijklmnopqrstuvwxyz"), "rent")]')

            logger.info(f"Select buy or rent in [{self.url}] --> SUCCESS")

        except Exception as error:
            logger.error(f"Unable to Select buy or rent in [{self.url}], Execution Ended --> ERROR [{error}]")

    def select_complete_location(self):
        location = f"{self.data.get("location")}, {self.data.get("city")}"
        try:
            logger.debug(f"Select Complete Location [{location}] in [{self.url}] --> START")

            self.driver.click_element(xpath='//span[@class="MuiTypography-root MuiTypography-body1New mui-style-15gx462"]')
            self.driver.input_text(xpath='//input[@id=":r2:" or @class="MuiInputBase-input MuiOutlinedInput-input MuiInputBase-inputAdornedStart MuiInputBase-inputAdornedEnd MuiAutocomplete-input MuiAutocomplete-inputFocused mui-style-1gnht4k"]', value=self.data.get("city"))
            self.driver.click_element(xpath='//li[@data-option-index="0"]')

            self.driver.input_text(xpath='//input[@id=":r2:" or @placeholder="Search for more areas"]', value=self.data.get("location"))
            self.driver.click_element(xpath='//li[@data-option-index="0"]')

            logger.info(f"Select Complete Location [{location}] in [{self.url}] --> SUCCESS")

        except Exception as error:
            logger.error(f"Unable to Select Complete Location [{location}] in [{self.url}], Execution Ended --> ERROR [{error}]")

    def select_property_type(self):
        property_type = f"{self.data.get("tab")} - {self.data.get("property_type")}"
        try:
            logger.debug(f"Select Property Type [{property_type}] in [{self.url}] --> START")

            self.driver.click_element(xpath='//body/div[@id="__next"]/div[@class="MuiBox-root mui-style-1uxvpob"]/div/div/div/div[2]/button[1]')
            if self.data.get("tab") == "homes/residential":
                self.driver.click_element(xpath='//button[contains(translate(normalize-space(text()), "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "abcdefghijklmnopqrstuvwxyz"), "residential")]')
            elif self.data.get("tab") == "plots":
                self.driver.click_element(xpath='//button[contains(translate(normalize-space(text()), "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "abcdefghijklmnopqrstuvwxyz"), "plot")]')
            else:
                self.driver.click_element(xpath='//button[contains(translate(normalize-space(text()), "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "abcdefghijklmnopqrstuvwxyz"), "commercial")]')
            self.driver.click_element(xpath=f'//span[translate(normalize-space(text()), "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "abcdefghijklmnopqrstuvwxyz")= "{self.data.get("property_type")}"]')
            self.driver.click_element(xpath='//button[translate(normalize-space(text()), "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "abcdefghijklmnopqrstuvwxyz")= "apply"]')

            logger.info(f"Select Property Type [{property_type}] in [{self.url}] --> SUCCESS")

        except Exception as error:
            logger.error(f"Unable to Select Property Type [{property_type}] in [{self.url}], Execution Ended --> ERROR [{error}]")

    def select_price(self):
        price = f"Minimum: {self.data.get("min_price")} | Maximum {self.data.get("max_price")}"
        try:
            logger.debug(f"Select Price [{price}] in [{self.url}] --> START")

            self.driver.click_element(xpath='//div[@class="MuiBox-root mui-style-1uxvpob"]//div[3]//button[1]')
            self.driver.input_text(xpath=f'//input[@class="MuiInputBase-input MuiOutlinedInput-input mui-style-1x5jdmq" and @placeholder="0"]', value=self.data.get("min_price"))
            self.driver.input_text(xpath=f'//input[@class="MuiInputBase-input MuiOutlinedInput-input mui-style-1x5jdmq" and translate(normalize-space(@placeholder), "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "abcdefghijklmnopqrstuvwxyz")= "any"]', value=self.data.get("max_price"))
            self.driver.scroll_down(pixels=200)
            self.driver.click_element(xpath='//button[translate(normalize-space(text()), "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "abcdefghijklmnopqrstuvwxyz")= "apply"]')

            logger.info(f"Select Price [{price}] in [{self.url}] --> SUCCESS")

        except Exception as error:
            logger.error(f"Unable to Select Price [{price}] in [{self.url}], Execution Ended --> ERROR [{error}]")


    def select_beds(self):
        try:
            logger.debug(f"Select Beds in [{self.url}] --> START")

            self.driver.click_element(xpath='//div[@class="MuiBox-root mui-style-1uxvpob"]//div//div[5]//button[1]')
            beds = self.data.get("beds")
            if beds in ("any", "none"):
                beds = "any"
            self.driver.scroll_down(pixels=200)
            self.driver.click_element(xpath=f'//div[@class="MuiBox-root mui-style-1drmyhy"]//span[translate(normalize-space(text()), "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "abcdefghijklmnopqrstuvwxyz")="{beds}"]')
            self.driver.click_element(xpath='//button[translate(normalize-space(text()), "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "abcdefghijklmnopqrstuvwxyz")= "apply"]')

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






