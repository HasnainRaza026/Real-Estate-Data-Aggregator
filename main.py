from customtkinter import *
from Visualization.dashboard import Dashboard
from Scraper import base_scraper


if __name__ == '__main__':
    window = CTk()
    dash_board = Dashboard(window)

    # base_scraper.main()
    window.mainloop()
