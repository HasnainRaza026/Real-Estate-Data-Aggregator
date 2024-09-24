from zameen_data_scraper import Zameen_Data_Scraper
from graana_data_scraper import Graana_Data_Scraper
from lamudi_data_scraper import Lamudi_Data_Scraper

def scrap_data():
    # zameen = Zameen_Data_Scraper(url="https://www.zameen.com/Rentals/Hyderabad_Qasimabad-672-1.html")
    # zameen_data = zameen.data
    # print(zameen_data)
    #
    # graana = Graana_Data_Scraper(
    #     url="https://www.graana.com/rent/residential-properties-rent-hyderabad-183/?pageSize=30&page=1")
    # graana_data = graana.data
    # print(graana_data)

    lamudi = Lamudi_Data_Scraper(
        url="https://www.lamudi.pk/search/hyderabad/homes-to-rent-30/")
    # lamudi_data = lamudi.data
    # print(lamudi_data)

if __name__ == '__main__':
    scrap_data()