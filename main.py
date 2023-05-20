from random import randint as r


electronics = ["capacitor","Resistor","mcu","transistor","relay"]
wiring = ["singlecore","multicore"]
tools = []
pchardware = ["fans","cpu","ram","hdd","ssd","psu","gpu","pccase"]
documents = ["manuals","studies"]
printer = []
Item_types = [electronics,wiring,tools,pchardware,documents,printer]

def display_options(options):
  n = 1
  for option in options:
    print(n,option + "\n")
    n += 1
  if input in range(1,n):
      answer = input
      return answer   

def display_menu():
  img_logo =  '''
  _   _   _  
 / \ / \ / \ 
( I | M | S )
 \_/ \_/ \_/  \n \n \n \n \n 

 Welcome to Inventory Management Software
 What do you want to do?\n \n \n
'''
  print(img_logo)
  





start_options = ["Add an Item","Search an Item","Remove an Item","Settings",]
display_menu()
display_options(start_options)




    

