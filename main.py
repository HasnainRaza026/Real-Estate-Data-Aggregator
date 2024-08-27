from scraper import base_scraper

base_scraper.main()


# import time
#
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# # chrome_driver_path = "C:/Users/Dell/Documents/chromedriver-win64/chromedriver.exe"
#
# # Initialize WebDriver (for Chrome)
# driver = webdriver.Chrome()
#
# # Open a webpage
# driver.get("https://www.speedtest.net/")
#
# # Wait for a specific element to be present before interacting with it
# element = WebDriverWait(driver, 100).until(
#     EC.presence_of_element_located(
#         (By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]'))
# )
#
# element.click()
#
# # Wait for a specific element to be present before interacting with it
# d_speed = WebDriverWait(driver, 180).until(
#     EC.presence_of_element_located(
#         (By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span'))
# )
# print(d_speed.text)
# print(driver.find_element(By.XPATH,
#       '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text)
# # time.sleep(100)
#
# driver.quit()
