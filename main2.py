"""menu manager"""


class Menu():
    """this class is for displaying the menu and managing the user input only"""
    freshId = 0

    def __init__(self, freshId=0):
        self.freshId = freshId

    with open("data.txt") as data_file:
        data_headers = data_file.readline()
        data = data_file.read()
    
    

    

    # This is the first thing the program does
    
    print(data_headers)
    print(data)
menu = Menu()
