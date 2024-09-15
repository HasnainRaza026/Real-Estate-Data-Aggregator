import os
from PIL import Image, ImageTk
from customtkinter import *

class Dashboard:
    """
    Dashboard class creates the main window and manages the different frames within the application.
    It includes methods to initialize the UI, handle navigation between frames, validate user input,
    and search properties based on the provided criteria.
    """

    def __init__(self, window):
        """
        Initialize the Dashboard window, configure appearance mode, load images,
        set up the grid layout, and initialize frames.

        :param window: The root window for the dashboard.
        """
        self.window = window
        self.window.geometry("550x400")
        self.window.title("Main Window")
        self.window.resizable(False, False)
        set_appearance_mode("light")

        # Load images for light and dark mode buttons
        light_mode_path = os.path.join(os.path.dirname(__file__), "../Assests/Pictures/light_mode.png")
        dark_mode_path = os.path.join(os.path.dirname(__file__), "../Assests/Pictures/dark_mode.png")
        self.light_mode_img = CTkImage(Image.open(light_mode_path), size=(20, 20))
        self.dark_mode_img = CTkImage(Image.open(dark_mode_path), size=(20, 20))

        # Load the light theme path
        self.light_theme_path = os.path.join(os.path.dirname(__file__), "../Assests/Themes/sky.json")
        set_default_color_theme(self.light_theme_path)

        # Configure the grid layout to make the frame expand
        self.window.grid_rowconfigure(0, weight=1)
        self.window.grid_columnconfigure(0, weight=1)

        self.data = None    # Initialize data to store user input

        self.initialize()


    def initialize(self):
        """
        Set up the main frame and buttons, initialize all the frames,
        and prepare the list of frames for navigation.
        """
        # Main frame for entering data
        self.frame_main = CTkFrame(self.window)
        self.frame_main.grid(sticky="nsew")

        # Configure rows and columns of the main frame
        self.frame_main.grid_rowconfigure(0, weight=1)
        self.frame_main.grid_rowconfigure(1, weight=1, minsize=250)
        self.frame_main.grid_rowconfigure(2, weight=1)
        self.frame_main.grid_columnconfigure(0, weight=1)
        self.frame_main.grid_columnconfigure(1, weight=1)
        self.frame_main.grid_columnconfigure(1, weight=1)

        # Button to change appearance mode
        self.change_mode_button = CTkButton(self.frame_main, text="", image=self.light_mode_img, width=30,
                                            command=self.change_appearance_mode)
        self.change_mode_button.grid(row=0, column=1, padx=10, pady=10, sticky="e")

        # Button to navigate to the next frame
        self.next_button = CTkButton(self.frame_main, text="NEXT", height=40, font=("Arial", 20, "bold"),
                                            command=self.next_frame)
        self.next_button.grid(row=2, column=1, padx=60, pady=20, sticky="e")

        # Button to navigate to the previous frame
        self.back_button = CTkButton(self.frame_main, state="disabled", text="BACK", height=40, font=("Arial", 20, "bold"),
                                            command=lambda: self.show_frame("back"))
        self.back_button.grid(row=2, column=0, padx=60, pady=20, sticky="w")

        # Set up all frames
        self.setup_first_frame()
        self.setup_second_frame()
        self.setup_third_frame()

        # List of frames for navigation
        self.frame_list = [self.frame_first, self.frame_second, self.frame_third]
        self.frame_index = 0


    def setup_first_frame(self):
        """
        Set up the first frame for user to input the city and location.
        """
        self.frame_first = CTkFrame(self.frame_main)
        self.frame_first.grid(row=1, column=0, sticky="nsew", columnspan=2)

        # Configure rows for the first frame
        self.frame_first.grid_rowconfigure(0, weight=1)
        self.frame_first.grid_rowconfigure(1, weight=1)

        # Subframe to hold input fields
        self.subframe_first = CTkFrame(self.frame_first)
        self.subframe_first.grid(row=0, column=0, padx=12, pady=40, sticky="nsew")

        # city entry widgets
        self.city_label = CTkLabel(self.subframe_first, text="CITY", font=("Arial White", 20, "bold"))
        self.city_label.grid(row=0, column=0, padx=30)
        self.city_entry = CTkEntry(self.subframe_first, width=300, height=40)
        self.city_entry.grid(row=0, column=1, padx=30, pady=15)

        # location entry widgets
        self.location_label = CTkLabel(self.subframe_first, text="LOCATION", font=("Arial", 20, "bold"))
        self.location_label.grid(row=1, column=0, padx=30)
        self.location_entry = CTkEntry(self.subframe_first, width=300, height=40)
        self.location_entry.grid(row=1, column=1, padx=30, pady=15)


    def setup_second_frame(self):
        """
        Set up the second frame with a tab view for selecting property type.
        """
        self.frame_second = CTkFrame(self.frame_main)

        # Configure rows for the second frame
        self.frame_second.grid_rowconfigure(0, weight=1)
        self.frame_second.grid_rowconfigure(1, weight=1)

        # Subframe to hold tabview
        self.subframe_second = CTkFrame(self.frame_second)
        self.subframe_second.grid(row=0, column=0, padx=25, pady=5, sticky="nsew")

        # Tabview for different property types
        self.tabview = CTkTabview(master=self.subframe_second,  height=210, width=500)
        self.tabview.grid(row=0, column=0, sticky="nsew")

        # Define tabs
        tabs = ["HOMES", "PLOTS", "COMMERCIAL"]
        for tab in tabs:
            self.tabview.add(tab)

        self.property_type_var = StringVar(value="none")    # Variable to store selected property type

        # Radio button options for each tab
        homes_radio_options = [
            ("House", "house"), ("Flat", "flat"), ("Upper Portion", "upper portion"),
            ("Lower Portion", "lower portion"), ("Farm House", "farm house"), ("Room", "room"),
            ("Penthouse", "penthouse")
        ]

        plots_radio_options = [
            ("Residential Plot", "residential plot"), ("Commercial Plot", "commercial plot"),
            ("Agricultural Land", "agricultural land"), ("Industrial Land", "industrial land"),
            ("Plot File", "plot file"), ("Plot Form", "plot form")
        ]

        commercial_radio_options = [
            ("Office", "office"), ("Shop", "shop"), ("Warehouse", "warehouse"),
            ("Factory", "factory"), ("Building", "building"), ("Other", "other")
        ]

        # Function to create radio buttons for a tab
        def create_radio_buttons(tab_name, options, tab_object):
            for i, (text, value) in enumerate(options):
                radiobutton = CTkRadioButton(
                    self.tabview.tab(tab_name), text=text, variable=self.property_type_var,
                    value=value, command=lambda: self.get_tab(tab_name)
                )
                radiobutton.grid(row=i // 3, column=i % 3, padx=20, pady=15)

        # Create radio buttons for each tab
        create_radio_buttons("HOMES", homes_radio_options, self.tabview.tab("HOMES"))
        create_radio_buttons("PLOTS", plots_radio_options, self.tabview.tab("PLOTS"))
        create_radio_buttons("COMMERCIAL", commercial_radio_options, self.tabview.tab("COMMERCIAL"))

    def setup_third_frame(self):
        """
        Set up the third frame with input fields for price range, rent/buy option, and number of beds.
        """
        self.frame_third = CTkFrame(self.frame_main)

        # Configure rows for the third frame
        self.frame_third.grid_rowconfigure(0, weight=1)
        self.frame_third.grid_rowconfigure(1, weight=1)

        # Subframe to hold input fields
        self.subframe_third = CTkFrame(self.frame_third)
        self.subframe_third.grid(row=0, column=0, pady=40, sticky="nsew")

        # Minimum price entry and label widgets
        self.min_label = CTkLabel(self.subframe_third, text="MINIMUM PRICE", font=("Arial White", 16, "bold"))
        self.min_label.grid(row=0, column=0, padx=20, pady=20)
        self.min_price_entry = CTkEntry(self.subframe_third)
        self.min_price_entry.grid(row=0, column=1, padx=20, pady=20)

        # Maximum price entry and label widgets
        self.max_label = CTkLabel(self.subframe_third, text="MAXIMUM PRICE", font=("Arial", 16, "bold"))
        self.max_label.grid(row=1, column=0, padx=20, pady=20)
        self.max_price_entry = CTkEntry(self.subframe_third)
        self.max_price_entry.grid(row=1, column=1, padx=20, pady=20)

        # Rent/Buy Radio button
        self.rent_buy_var = StringVar(value="none")
        radiobutton_rent = CTkRadioButton(self.subframe_third, text="Rent", variable=self.rent_buy_var,
                                           value="rent")
        radiobutton_rent.grid(row=0, column=2, padx=0, pady=20, sticky="e")
        radiobutton_buy = CTkRadioButton(self.subframe_third, text="Buy", variable=self.rent_buy_var,
                                          value="buy", width=50)
        radiobutton_buy.grid(row=0, column=2, padx=20, pady=20, sticky="w")

        self.bed_label = CTkLabel(self.subframe_third, text="SELECT BEDS", font=("Arial", 14, "bold"))
        self.bed_label.grid(row=1, column=2, padx=20, pady=0, sticky="n")
        self.beds_var = StringVar(value="Any")
        optionmenu_beds = CTkOptionMenu(self.subframe_third, values=["Any", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "None"], variable=self.beds_var)
        optionmenu_beds.grid(row=1, column=2, padx=40, pady=0, sticky="s")


    def get_tab(self, tab):
        """
        Retrieve the selected tab name and store the corresponding property type.

        :param tab_name: The name of the tab selected.
        """
        self.selected_tab = tab

    def change_appearance_mode(self):
        """
        Toggle the appearance mode between light and dark, and update the change_mode_button image.
        """
        if get_appearance_mode() == "Dark":
            set_appearance_mode("light")
            set_default_color_theme(self.light_theme_path)
            self.change_mode_button.configure(image=self.light_mode_img)
        else:
            set_appearance_mode("dark")
            set_default_color_theme(self.light_theme_path)
            self.change_mode_button.configure(image=self.dark_mode_img)

    def next_frame(self):
        """
        Navigate to the next frame if user inputs are valid, otherwise display an error message.
        """
        if self.frame_index == 0:
            if not self.validate_first_frame():
                return
        elif self.frame_index == 1:
            if not self.validate_second_frame():
                return
        elif self.frame_index == 2:
            if not self.validate_third_frame():
                return
            self.search_properties()

        self.show_frame("next")

    def show_frame(self, frame):
        """
        Show the next or previous frame based on the direction argument.

        :param direction: A string, either "next" or "back", indicating the direction to navigate.
        """
        if frame == "next" and self.frame_index < len(self.frame_list) - 1:
            self.frame_list[self.frame_index].grid_forget()
            self.frame_index += 1
            self.back_button.configure(state="normal")
            if self.frame_index == len(self.frame_list) - 1:
                self.next_button.configure(text="SEARCH")
            self.frame_list[self.frame_index].grid(row=1, column=0, sticky="nsew", columnspan=2)
        elif frame == "back" and self.frame_index > 0:
            self.frame_list[self.frame_index].grid_forget()
            self.frame_index -= 1
            self.frame_list[self.frame_index].grid(row=1, column=0, sticky="nsew", columnspan=2)
            if self.frame_index == 0:
                self.back_button.configure(state="disabled")
            else:
                self.next_button.configure(text="NEXT")

    def validate_first_frame(self):
        """
        Validate the inputs provided in the first frames.

        :return: Boolean indicating whether the inputs are valid.
        """
        error_label_first_frame = CTkLabel(self.frame_first, text="", text_color="red", font=("Arial", 12))
        error_label_first_frame.configure(text="")
        error_label_first_frame.grid(row=2, columnspan=2)
        if not self.city_entry.get().strip():
            error_label_first_frame.configure(text="City is required!")
            return False
        if not self.location_entry.get().strip():
            error_label_first_frame.configure(text="Location is required!")
            return False
        return True

    def validate_second_frame(self):
        error_label = CTkLabel(self.frame_second, text="", text_color="red", font=("Arial", 12))
        error_label.grid(row=2, columnspan=2)
        if self.property_type_var.get() == "none":
            error_label.configure(text="Please select the desired property type.")
            return False
        return True

    def validate_third_frame(self):
        error_label = CTkLabel(self.frame_third, text="", text_color="red", font=("Arial", 12))
        error_label.grid(row=2, columnspan=2)
        if self.rent_buy_var.get() == "none":
            error_label.configure(text="Please select Buy or Rent.")
            return False
        try:
            min_price = float(self.min_price_entry.get().strip())
            max_price = float(self.max_price_entry.get().strip())
            if min_price < 0 or max_price < 0:
                raise ValueError("Prices cannot be negative.")
            if min_price > max_price:
                error_label.configure(text="Minimum price cannot be greater than maximum price.")
                return False
        except ValueError:
            error_label.configure(text="Please enter valid numeric prices.")
            return False
        return True

    def search_properties(self):
        self.data = {
            "city": self.city_entry.get().lower(),
            "location": self.location_entry.get().lower(),
            "tab": self.selected_tab.lower(),
            "property_type": self.property_type_var.get().lower(),
            "min_price": self.min_price_entry.get().lower(),
            "max_price": self.max_price_entry.get().lower(),
            "buy/rent": self.rent_buy_var.get().lower(),
            "beds": self.beds_var.get().lower(),
        }





