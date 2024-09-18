from Utilities.logger import logger
class Graana_Scraper:
    def __init__(self, data, selenium_driver):
        self.data = data
        self.driver = selenium_driver
        self.url = "https://www.graana.com/"

        logger.debug(f"Get Result Page url of {self.url} --> START")

        self.start_scraping()

    def start_scraping(self):
        # Open "https://www.graana.com/" webpage
        self.driver.goto_page(url=self.url)
        logger.info(f"Open Webpage {self.url} --> SUCCESS")

        # self.remove_ads()


        self.select_buy_or_rent()
        self.select_complete_location()
        self.click_find()
        self.select_property_type()
        # self.select_price()
        #
        # if self.data.get("tab") == "homes":
        #     self.select_beds()
        #


    def remove_ads(self):
        try:
            logger.debug(f"Remove Ads in [{self.url}] --> START")

            self.driver.click_element(xpath='//button[@id="close-need-help-btn"]')

            logger.info(f"Remove Ads in [{self.url}] --> SUCCESS")

        except Exception as error:
            logger.error(f"Unable to Remove Ads in [{self.url}], Execution Ended --> ERROR [{error}]")

    def select_buy_or_rent(self):
        try:
            logger.debug(f"Select buy or rent in [{self.url}] --> START")

            if self.data.get("buy/rent") == "buy":
                self.driver.click_element(xpath='//button[@class="MuiButtonBase-root MuiButton-root MuiButton-contained MuiButton-containedSecondary MuiButton-sizeMedium MuiButton-containedSizeMedium MuiButton-colorSecondary MuiButton-root MuiButton-contained MuiButton-containedSecondary MuiButton-sizeMedium MuiButton-containedSizeMedium MuiButton-colorSecondary mui-style-x1hok3"]')
            else:
                self.driver.click_element(xpath='//button[@class="MuiButtonBase-root MuiButton-root MuiButton-contained MuiButton-containedSecondary MuiButton-sizeMedium MuiButton-containedSizeMedium MuiButton-colorSecondary MuiButton-root MuiButton-contained MuiButton-containedSecondary MuiButton-sizeMedium MuiButton-containedSizeMedium MuiButton-colorSecondary mui-style-1ap4hl3"]')

            logger.info(f"Select buy or rent in [{self.url}] --> SUCCESS")

        except Exception as error:
            logger.error(f"Unable to Select buy or rent in [{self.url}], Execution Ended --> ERROR [{error}]")

    def select_complete_location(self):
        location = f"{self.data.get("location")}, {self.data.get("city")}"
        try:
            logger.debug(f"Select Complete Location [{location}] in [{self.url}] --> START")

            self.driver.input_text(xpath='//input[@type="text"]', value=location)
            # self.driver.click_element(xpath='//input[@type="text"]')
            self.driver.click_element(xpath='//ul[@class="MuiList-root MuiList-padding mui-style-jkt0xd"]//div[@role="button"][position()=1]')

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
        try:
            logger.debug(f"Select Price in [{self.url}] --> START")

            self.driver.click_element(xpath='//div[@name="Price (PKR)"]//span[1]')
            self.driver.input_text(xpath=f'//input[@id="activeNumericInput"]', value=self.data.get("min_price"))
            self.driver.input_text(xpath=f'//input[@id="inactiveNumericInput"]', value=self.data.get("max_price"))

            logger.info(f"Select Price in [{self.url}]  --> SUCCESS")

        except Exception as error:
            logger.error(f"Unable to Select Price in [{self.url}], Execution Ended --> ERROR [{error}]")


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

            self.driver.click_element(xpath='//button[@class="MuiButtonBase-root MuiButton-root MuiButton-contained MuiButton-containedPrimary MuiButton-sizeMedium MuiButton-containedSizeMedium MuiButton-colorPrimary MuiButton-root MuiButton-contained MuiButton-containedPrimary MuiButton-sizeMedium MuiButton-containedSizeMedium MuiButton-colorPrimary mui-style-silsk4"]')

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






