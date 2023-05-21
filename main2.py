class Menu():
    with open(data.csv) as csvfile:
        file_title = csvfile.readline()
    title = file_title
    print(title)



menu = Menu()    
