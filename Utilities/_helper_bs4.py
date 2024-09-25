from bs4 import BeautifulSoup
import requests
from Utilities.logger import logger

class BS4_Helper:
    def __init__(self, url, zameen=False, graana=False, lamudi=False):
        self.zameen = zameen
        self.graana = graana
        self.lamudi = lamudi

        self.url = url
        self.soup = None
        self.data = {}

        self._make_bs4_instance()

    def get_data(self, url, page, list_css, url_css, price_css, location_css, beds_css,
                 baths_css, images_css):
        self.url = url
        try:
            logger.debug(f"Make BS4 Instance for [{self.url}] --> START")
            self._make_bs4_instance()
            logger.debug(f"Make BS4 Instance for [{self.url}] --> SUCCESS")

            logger.debug(f"Get data list in [{self.url}] --> START")
            data_list = self._get_list(list_css=list_css)
            logger.debug(f"Get data list in [{self.url}] --> SUCCESS")

            logger.debug("Get data from the list --> START")

            for index, list_item in enumerate(data_list):
                data_location = self._get_location(list_item=list_item, location_css=location_css)
                unique_key = f"{data_location} [{page+1} - {index+1}]"
                self.data[unique_key] = {}

                data_price = self._get_price(list_item=list_item, price_css=price_css)
                self.data[unique_key]["price"] = data_price

                data_beds = self._get_beds(list_item=list_item, beds_css=beds_css)
                self.data[unique_key]["beds"] = data_beds

                data_baths = self._get_baths(list_item=list_item, baths_css=baths_css)
                self.data[unique_key]["baths"] = data_baths

                data_url = self._get_url(list_item=list_item, url_css=url_css)
                if self.zameen:
                    data_url = "https://www.zameen.com" + data_url
                elif self.graana:
                    data_url = "https://www.graana.com" + data_url
                else:
                    data_url = "https://www.lamudi.pk" + data_url
                self.data[unique_key]["url"] = data_url

                data_img = self._get_images(list_item=list_item, images_css=images_css)
                if self.graana:
                    data_img = "https://www.graana.com/" + data_img
                self.data[unique_key]["img"] = data_img
                logger.debug(f"Get data from the list item [{index + 1}] --> SUCCESS")

            logger.debug("Get data from the complete list --> SUCCESS")

        except Exception as error:
            logger.error(f"Unable to Get data from the list --> ERROR [{error}]")
            return None

    def _make_bs4_instance(self):
        response = self._get_html()
        if response is not None:
            logger.debug(f"Making BeautifulSoup Instance --> START")
            self.soup = BeautifulSoup(response.content, "html.parser")
            logger.debug(f"Making BeautifulSoup Instance --> SUCCESS")
        else:
            logger.error(f"Execution Ended --> Can't get HTML of [{self.url}]")

    def _get_html(self):
        try:
            logger.debug(f"Get HTML of [{self.url}] --> START")
            response = requests.get(self.url)
            response.raise_for_status()
            logger.debug(f"Get HTML of [{self.url}] --> SUCCESS")
            return response
        except Exception as error:
            logger.error(f"Unable to Get HTML of [{self.url}], Execution Ended --> ERROR [{error}]")
            return None

    def total_properties_found(self, property_css):
        try:
            logger.debug(f"Get Total Number of Properties using [{property_css}] in [{self.url}] --> START")
            all_tags = self.soup.select(property_css)
            if self.zameen:
                total_properties = [tag.get_text() for tag in all_tags if 'Properties' in tag.get_text()]
                total_properties = total_properties[0].split()
                total_properties = int(total_properties[0])
            elif self.graana:
                total_properties = all_tags[0].get_text()
                total_properties = total_properties.split()
                total_properties = int(total_properties[1])
            else:
                total_properties = all_tags[0].get_text()
                total_properties = total_properties.split()
                total_properties = int(total_properties[4])
            logger.debug(f"Get Total Number of Properties using [{property_css}] in [{self.url}] --> SUCCESS")
            return total_properties
        except Exception as error:
            logger.error(f"Unable to Get Total Number of Properties using [{property_css}] in [{self.url}] --> ERROR [{error}]")
            return None

    def _get_list(self, list_css):
        try:
            logger.debug(f"Get list using [{list_css}] in [{self.url}] --> START")
            data_list = self.soup.select(list_css)
            logger.debug(f"Get list using [{list_css}] in [{self.url}] --> SUCCESS")
            return data_list
        except Exception as error:
            logger.error(f"Unable to Get list using [{list_css}] in [{self.url}] --> ERROR [{error}]")
            return None

    def _get_url(self, list_item, url_css):
        try:
            logger.debug(f"Get URLs in data using [{url_css}] in [{self.url}] --> START")
            elements = list_item.select(url_css)
            data = self._helper_get(elements=elements, css=url_css, is_url=True)
            if data is not None:
                logger.debug(f"Get URLs in data using [{url_css}] in [{self.url}] --> SUCCESS")
            return data
        except Exception as error:
            logger.error(f"Unable to Get URLs in data using [{url_css}] in [{self.url}] --> ERROR [{error}]")
            return None

    def _get_price(self, list_item, price_css):
        try:
            logger.debug(f"Get Price in data using [{price_css}] in [{self.url}] --> START")
            elements = list_item.select(price_css)
            data = self._helper_get(elements=elements, css=price_css)
            if data is not None:
                logger.debug(f"Get Price in data using [{price_css}] in [{self.url}] --> SUCCESS")
            return data
        except Exception as error:
            logger.error(f"Unable to Get Price in data using [{price_css}] in [{self.url}] --> ERROR [{error}]")
            return None

    def _get_location(self, list_item, location_css):
        try:
            logger.debug(f"Get Locations in data using [{location_css}] in [{self.url}] --> START")
            elements = list_item.select(location_css)
            data = self._helper_get(elements=elements, css=location_css)
            if data is not None:
                logger.debug(f"Get Locations in data using [{location_css}] in [{self.url}] --> SUCCESS")
            return data
        except Exception as error:
            logger.error(f"Unable to Get Locations in data using [{location_css}] in [{self.url}] --> ERROR [{error}]")
            return None

    def _get_beds(self, list_item, beds_css):
        try:
            logger.debug(f"Get Beds in data using [{beds_css}] in [{self.url}] --> START")
            elements = list_item.select(beds_css)
            if self.lamudi:
                elements = list(elements[1])
                data = elements[1]
                return data
            data = self._helper_get(elements=elements, css=beds_css)
            if data is not None:
                logger.debug(f"Get Beds in data using [{beds_css}] in [{self.url}] --> SUCCESS")
            return data
        except Exception as error:
            logger.error(f"Unable to Get Beds in data using [{beds_css}] in [{self.url}] --> ERROR [{error}]")
            return None

    def _get_baths(self, list_item, baths_css):
        try:
            logger.debug(f"Get Baths in data using [{baths_css}] in [{self.url}] --> START")
            elements = list_item.select(baths_css)
            if self.graana:
                elements = list(elements[1])
            elif self.lamudi:
                elements = list(elements[2])
                data = elements[1]
                return data
            data = self._helper_get(elements=elements, css=baths_css)
            if data is not None:
                logger.debug(f"Get Baths in data using [{baths_css}] in [{self.url}] --> SUCCESS")
            return data
        except Exception as error:
            logger.error(f"Unable to Get Baths in data using [{baths_css}] in [{self.url}] --> ERROR [{error}]")
            return None

    def _get_images(self, list_item, images_css):
        try:
            logger.debug(f"Get images in data using [{images_css}] in [{self.url}] --> START")
            elements = list_item.select(images_css)
            data = self._helper_get(elements=elements, css=images_css, is_img=True)
            if data is not None:
                logger.debug(f"Get images in data using [{images_css}] in [{self.url}] --> SUCCESS")
            return data
        except Exception as error:
            logger.error(f"Unable to Get images in data using [{images_css}] in [{self.url}] --> ERROR [{error}]")
            return None

    def _helper_get(self, elements, css, is_url=False, is_img=False):
        if elements:
            element = elements[0]
            if is_url:
                data = element.get('href')
                return data
            elif is_img:
                data = element.get('src')
                if data is None:
                    data = element.get('data-src')
                    return data
                return data
            data_url = element.get_text()
            return data_url
        else:
            logger.warning(f"No elements found using [{css}] in [{self.url}]")
            return None





