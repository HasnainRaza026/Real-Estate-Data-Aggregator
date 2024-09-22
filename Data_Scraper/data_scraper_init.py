from zameen_data_scraper import Zameen_Data_Scraper
from graana_data_scraper import Graana_Data_Scraper

def scrap_data():
    zameen = Zameen_Data_Scraper(url="https://www.zameen.com/Rentals/Hyderabad-30-1.html")
    zameen_data = zameen.data
    print(zameen_data)

    # graana = Graana_Data_Scraper(
    #     url="")
    # graana_data = graana.data
    # print(graana_data)

if __name__ == '__main__':
    scrap_data()