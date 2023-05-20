from random import randint as r

class menu(title = [""],options = [[""]]):
    displayed_page = [title[0],options[0]]
    def display_title():
        pass
    def clear():
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    def page(int):
        self.displayed_page = [title[int],options[int]]
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
    def user_input():
        answer = input("Type a number to select")
        return answer
pass

