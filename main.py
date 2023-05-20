from random import randint as r

# This variables will be accesible and editable in the program but i put some of them for testing

items = [[[""],[""],[1]]]
electronics = ["capacitor","Resistor","mcu","transistor","relay"]
wiring = ["singlecore","multicore"]
tools = []
pchardware = ["fans","cpu","ram","hdd","ssd","psu","gpu","pccase"]
documents = ["manuals","studies"]
printer = []
Item_types = [electronics,wiring,tools,pchardware,documents,printer]
#silly function to clear the terminal and make a new "display"
def clear_display():
  print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")  

#function to use within every menu function to display the selectable options
def display_options(options):
  n = 1
  for option in options:
    print(n,option + "\n")
    n += 1
  answer = input("Select typing any option number.")  
  print("you selected",answer)
  return answer
  

#start menu page options
start_options = ["Add an Item","Search an Item","Remove an Item","Settings",]
#Principal menu of the program, simple but not ugly, perfect.


def display_menu():

  img_logo =  '''
  _   _   _  
 / \ / \ / \ 
( I | M | S )
 \_/ \_/ \_/  \n \n \n \n \n 

 Welcome to Inventory Management Software
 What do you want to do?\n \n \n
'''
  #prints the logo
  print(img_logo)
  #scans the user input and saves it
  answer = display_options(start_options)
  return answer
  
  
  
def search_menu():
  search_title = '''
    _   _   _   _     _   _   _   _   _   _   _   _   _     _   _   _   _   _   _  
 / \ / \ / \ / \   / \ / \ / \ / \ / \ / \ / \ / \ / \   / \ / \ / \ / \ / \ / \ 
( I | T | E | M ) ( S | E | A | R | C | H | I | N | G ) ( E | N | G | I | N | E )
 \_/ \_/ \_/ \_/   \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/   \_/ \_/ \_/ \_/ \_/ \_/ 
 '''
  print(search_title)
  for item in items:
    print(item)  






answer = display_menu()
if answer == 1:
  pass
elif answer == 2:
  search_menu()
  





    

