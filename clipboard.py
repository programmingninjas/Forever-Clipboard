from tkinter import Tk
from time import sleep

# This program will save everything that you copy and save it in a text file
# And quit when you copy exit, if its exiting as soon as you run the code that means
# exit is saved in your clipboard, copy something else to fix.

clipboard =  Tk()
clipboard.withdraw()

while not clipboard.selection_get(selection='CLIPBOARD'):
    sleep(0.1)

data = set()

while True:

    result  = clipboard.selection_get(selection='CLIPBOARD')
    if result.lower() != 'exit':
        data.add(result)
        sleep(1)
    else:
        print('Program Closed!')
        break
data = list(data)
with open('data.txt','a') as file:

    for words in data[::-1]:

        file.write(words)
        file.write('\n')





























       
