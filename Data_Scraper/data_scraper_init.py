from zameen_data_scraper import Zameen_Data_Scraper

def scrap_data():
    zameen = Zameen_Data_Scraper(url="https://www.zameen.com/Rentals_Flats_Apartments/Hyderabad_Latifabad-673-1.html?price_min=10000&price_max=25000&beds_in=3")

if __name__ == '__main__':
    scrap_data()