from Utilities.logger import logger
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

class Selenium_Helper:
    def __init__(self):
        options = self.get_chrome_options()
        logger.debug("Set chrome driver options --> SUCCESS")
        self.keys = Keys()
        logger.debug("Initialize chrome Driver --> START")
        self.driver = Chrome(service=Service(ChromeDriverManager().install()), options=options)
        logger.info("Initialize chrome Driver --> SUCCESS")
        logger.debug("Initialize Driver Implicit wait --> START")
        self.driver.implicitly_wait(10)
        logger.debug("Initialize Driver Implicit wait --> SUCCESS")

    def _get_element(self, xpath):
        try:
            logger.debug(f"Get {xpath} element --> START")
            element = self.driver.find_element(By.XPATH, xpath)
            logger.info(f"Get {xpath} element --> SUCCESS")
            return element
        except Exception as error:
            logger.error(f"Unable to Get {xpath} element --> ERROR [{error}]")
            return None

    def click_element(self, xpath):
        try:
            element = self._get_element(xpath)
            if element is not None:
                logger.debug(f"Click {xpath} element --> START")
                element.click()
                logger.info(f"Click {xpath} element --> SUCCESS")
            else:
                logger.error(f"Unable to Click {xpath} element --> ERROR [element is None]")
        except Exception as error:
            logger.error(f"Unable to Click {xpath} element --> ERROR [{error}]")

    def input_text(self, value, xpath):
        try:
            element = self._get_element(xpath)
            if element is not None:
                element.send_keys(value)
            else:
                print("Element not found")
        except Exception as error:
            print(f"Error in Sending the keys to the element: {error}")

    def goto_page(self, url):
        try:
            logger.debug(f"Visit page {url} --> START")
            self.driver.get(url)
            logger.info(f"Visit page {url} --> SUCCESS")
        except Exception as error:
            logger.error(f"Unable to visit page {url} --> ERROR [{error}]")

    def reload_page(self, url):
        try:
            logger.debug(f"Reload page {url} --> START")
            self.driver.refresh()
            logger.info(f"Reload page {url} --> SUCCESS")
        except Exception as error:
            logger.error(f"Unable to reload page {url} --> ERROR [{error}]")

    def quit(self):
        self.driver.quit()

    def get_chrome_options(self):
        logger.debug("Set chrome driver options --> START")
        options = Options()
        options.add_argument("--headless") # Headless mode
        options.add_argument("--disable-gpu") # Disable GPU hardware acceleration
        options.add_argument("--disable-infobars") # Disable browser UI components
        options.add_argument("--disable-extensions") # Disable browser UI components
        options.add_argument("--no-sandbox") # Disable sandbox mode (useful for some OS configurations)
        options.add_argument("--ignore-certificate-errors") # Ignore certificate errors
        options.add_argument("--disable-dev-shm-usage") # Disable dev-shm-usage (necessary for some environments, like Docker)
        options.add_argument("--log-level=3") # Disable logging
        options.add_argument("--window-size=1920x1080") # Set window size (important for headless mode)
        options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3") # User agent to avoid detection
        return options