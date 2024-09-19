from Utilities.wait import wait
from Utilities.logger import logger
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

class Selenium_Helper:
    def __init__(self):
        self.url = None
        self.second = 0.5
        self.keys = Keys()

        # options = self.get_chrome_options()
        # logger.debug("Set chrome driver options --> SUCCESS")

        logger.debug("Initialize chrome Driver --> START")
        self.driver = Chrome()
        # self.driver = Chrome(service=Service(ChromeDriverManager().install()), options=options)
        logger.debug("Initialize chrome Driver --> SUCCESS")

        logger.debug("Initialize Driver Implicit wait --> START")
        self.driver.implicitly_wait(15)
        logger.debug("Initialize Driver Implicit wait --> SUCCESS")

    def _get_element(self, xpath):
        try:
            logger.debug(f"Get element [{xpath}]  --> START")
            element = self.driver.find_element(By.XPATH, xpath)
            logger.debug(f"Get element [{xpath}]  --> SUCCESS")
            return element
        except Exception as error:
            logger.error(f"Unable to Get element [{xpath}]  --> ERROR [{error}]")
            return None

    def click_element(self, xpath):
        retry = False  # To track if it's a retry attempt
        for attempt in range(2):  # Try twice: first attempt + retry
            try:
                element = self._get_element(xpath)
                if element is not None:
                    logger.debug(f"Click element [{xpath}] --> START (Attempt {attempt + 1})")
                    element.click()
                    logger.debug(f"Click element [{xpath}] --> SUCCESS (Attempt {attempt + 1})")
                    wait(self.second)
                    break  # Exit loop if the element is clicked successfully
                else:
                    logger.error(f"Unable to Click element [{xpath}] --> ERROR [element is None]")
                    if not retry:  # Only reload the page on the first failure
                        retry = True
                        logger.info(f"Reloading page and retrying click element [{xpath}] --> START")
                        self.reload_page()  # Reload the page
                        logger.info(f"Reloading page [{self.driver.current_url}] --> DONE")
                    else:
                        logger.error(f"Click element [{xpath}] --> FAILED after retry")
            except Exception as error:
                logger.error(f"Unable to Click element [{xpath}] --> ERROR [{error}] (Attempt {attempt + 1})")
                if not retry:  # Only reload the page on the first failure
                    retry = True
                    logger.info(f"Reloading page and retrying click element [{xpath}] --> START")
                    self.reload_page()  # Reload the page
                    logger.info(f"Reloading page [{self.driver.current_url}] --> DONE")
                else:
                    logger.error(f"Click element [{xpath}] --> FAILED after retry")

    def input_text(self, xpath, value):
        retry = False  # To track if it's a retry attempt
        for attempt in range(2):  # Try twice: first attempt + retry
            try:
                element = self._get_element(xpath)
                if element is not None:
                    logger.debug(f"Send keys [{value}] to element [{xpath}] --> START (Attempt {attempt + 1})")
                    element.send_keys(value)
                    logger.debug(f"Send keys [{value}] to element [{xpath}] --> SUCCESS (Attempt {attempt + 1})")
                    wait(self.second)
                    break  # Exit loop if successful
                else:
                    logger.error(f"Failed to Send keys [{value}] to element [{xpath}] --> ERROR [element is None]")

                    if not retry:  # Only reload the page on the first failure
                        retry = True
                        logger.info(f"Reloading page and retrying send keys to element [{xpath}] --> START")
                        self.reload_page()  # Reload the page
                        logger.info(f"Reloading page [{self.driver.current_url}] --> DONE")
                    else:
                        logger.error(f"Failed to Send keys to element [{xpath}] --> FAILED after retry")
            except Exception as error:
                logger.error(
                    f"Unable to Send keys [{value}] to element [{xpath}] --> ERROR [{error}] (Attempt {attempt + 1})")
                if not retry:  # Only reload the page on the first failure
                    retry = True
                    logger.info(f"Reloading page and retrying send keys to element [{xpath}] --> START")
                    self.reload_page()  # Reload the page
                    logger.info(f"Reloading page [{self.driver.current_url}] --> DONE")
                else:
                    logger.error(f"Failed to Send keys to element [{xpath}] --> FAILED after retry")

    def goto_page(self, url):
        try:
            logger.debug(f"Visit page [{self.url}] --> START")
            self.driver.get(url)
            self.url = url
            logger.debug(f"Visit page [{self.url}] --> SUCCESS")
        except Exception as error:
            logger.error(f"Failed to visit page [{self.url}] --> ERROR [{error}]")

    def reload_page(self):
        wait(self.second)
        try:
            logger.debug(f"Reload page [{self.url}] --> START")
            self.driver.refresh()
            logger.debug(f"Reload page [{self.url}] --> SUCCESS")
        except Exception as error:
            logger.error(f"Failed to reload page [{self.url}] --> ERROR [{error}]")

    def scroll_down(self, pixels=None):
        try:
            logger.debug(f"Scroll Down by {pixels} pixels in {self.url} --> START ")
            self.driver.execute_script(f"window.scrollBy(0, {pixels});")
            logger.debug(f"Scroll Down by {pixels} pixels in {self.url} --> SUCCESS ")
        except Exception as error:
            logger.error(f"Failed to Scroll Down by {pixels} pixels in {self.url} --> ERROR [{error}]")

    def quit(self):
        try:
            logger.debug(f"Quit Driver --> START")
            self.driver.quit()
            logger.debug(f"Quit Driver --> SUCCESS")
        except Exception as error:
            logger.error(f"Failed to Quit Driver --> ERROR [{error}]")

    def get_url(self):
        try:
            logger.debug(f"Get Current url --> START")
            result_page_url = self.driver.current_url
            logger.debug(f"Get Current url --> SUCCESS")
            return result_page_url
        except Exception as error:
            logger.error(f"Failed to Get Current url --> ERROR [{error}]")
            return None


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