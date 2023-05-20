
class Menu():
    title = []
    options = [[]]
    index = 0
    def __init__(self,title,options,index):
        self.title = title
        self.options = options
        self.index = index
    def clear():
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    def page(self):
        self.index = input("Insert the option typing their number")
    def display_page():
        def display_title():
            pass
        def display_options():
            pass
        Menu.page()            