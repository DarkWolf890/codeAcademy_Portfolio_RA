"""menu manager"""
import csv

class Menu():
    """this class is for displaying the menu and managing the user input only"""
    freshId = 0

    def __init__(self, freshId=0):
        self.freshId = freshId

    # This are functions for reading and updating the menu data

    def get_menu_data(self):
        """This functions stores the csv in a string"""
        with open("data.csv") as csv_file:
            csv_data = csv_file.read()
        return csv_data

    def add_menu_data(self):
        """This function appends a new menu display"""
        with open("data.csv", "a") as csv_file:
            csv_line_to_append = input("""Insert the title followed by a comma, then type 
            every option with : for separation""")
            csv_file.write(csv_line_to_append+self.freshId)
        self.freshId = + 1

    # This is the first thing the program does
    add_menu_data
    csv_file = get_menu_data
    print(csv_file)


menu = Menu()
