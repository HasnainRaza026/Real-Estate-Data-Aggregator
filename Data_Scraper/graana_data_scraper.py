import math

from Utilities.logger import logger
from Utilities._helper_bs4 import BS4_Helper

class Graana_Data_Scraper:
    def __init__(self, url):
        self.url = url
        self.soap = BS4_Helper(self.url, graana=True)
        self.data = None

        logger.debug(f"Get Result Page data of {self.url} --> START")

        self.start_scraping_data()

    def start_scraping_data(self):
        total_properties = self.soap.total_properties_found(property_css='div[class="MuiTypography-root MuiTypography-subtitle2New mui-style-1xrzzd4"]')
        pages = math.ceil(total_properties/30)  # Rounding up to the next whole number
        logger.info(f"{total_properties} Total Properties found, split into {pages} Pages in {self.url}")
        for page in range(pages):
            self.data = self.soap.get_data(url=self.url, page=page, list_css='div[class="MuiBox-root mui-style-17zbhp0"]',
                            url_css='a', price_css='div[class="MuiTypography-root MuiTypography-h4New mui-style-gz23my"]',
                            location_css='h5', beds_css='div[class="MuiTypography-root MuiTypography-body2New mui-style-1548769"]',
                            baths_css='div[class="MuiTypography-root MuiTypography-body2New mui-style-1548769"]',
                            images_css='div[class="swiper-lazy MuiBox-root mui-style-cqtyl0"] img')
            self.url = self.url.replace(f"page={page+1}", f"page={page+2}")
            logger.info(f"Scrap Property Data from Page {page+1} --> SUCCESS")

        self.data = self.soap.data


