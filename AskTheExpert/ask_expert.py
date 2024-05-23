#Topic: FILE IO, Tkinter tools module
#simpledialog and messagebox is part of Tkinter tools
from tkinter import Tk, simpledialog, messagebox

#Creating funtion
def read_from_file():
    with open('capital_data.txt') as file:
        for line in file:
            line = line.rstrip('\n')
            country, city = line.split('/')
            the_world[country] = city #add data to the dictionary. [country] -> this is the key, city -> this is the value
            
#File Output
def write_to_file(country_name, city_name):
    with open('capital_data.txt', 'a') as file: #'a' means append
        file.write('\n' + country_name + '/' + city_name)

print('Ask the Exper - Capital Cities of the World')
root = Tk() #create an empty Tkinter window
root.withdraw() #hide the Tkinter window

#Creates an empty dictionary
the_world = {} #use curly braces
read_from_file()

while True:
    query_country = simpledialog.askstring('Country', 'Type the name of a country: ')
    if query_country in the_world:
        result = the_world[query_country]
        messagebox.showinfo('Answer ',
                            'The capital city of ' + query_country + ' is ' + result + '!')
    else:
        new_city = simpledialog.askstring('Teach Me ',
                                          'I don\'t know! ' + 
                                          'What is the capital city of ' + query_country + '?')
        the_world[query_country] = new_city
        write_to_file(query_country, new_city)

root.mainloop()