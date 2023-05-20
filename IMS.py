from random import randint as r

class Menu():
    options = [[""]]
    title = [""]
    page_index = 0
    def __init__(self,options,title,page_index):
        self.options = options
        self.title = title
        self.page_index = page_index
        
        
    def display_title(title):
        print(self.title[self.page_index])
    
    def clear():
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    def page():
        
        page_index = input("Type a number to select")
    def display_options():
        n = 1
        for option in options:
            print(n,option + "\n")
            n += 1
  
    def add_page():
        title.append(input("Insert a title for the menu section:"))
        while True:
            user_input = input("Insert one option of the menu")
            if user_input == -1:
                break
            options[-1].append(user_input)
    def remove_page():
        pass
    

menu = Menu()
Menu.add_page()
Menu.page(1)
Menu.display_title()




