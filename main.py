"""Module providingFunction printing python version."""
class Menu():
    """Class representing a person"""
    title = []
    options = [[]]
    index = 0
    def __init__(self,title,options,index):
        self.title = title
        self.options = options
        self.index = index
    def clear(self):

        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

    def display_page(self):
        def page(self):
            self.index = input("Insert the option typing their number")
        def display_title(self):
            print(self.title[self.index])
        def display_options(self):
            n = 1
        for option in self.options[self.index]:
            print(n,option + "\n")
            n += 1
        display_title(self)
        display_options(self)
        page(self)


