#importing libraries
from tkinter import *
import random

#main window
master = Tk()
master.configure(background='white')

#title
master.title("Title of window")

#metod for click
col = 0
row = 1
def color():
    global col
    global row
    if col>9 :
        row+=1
        col=0
    btn_column = Canvas(master,bd=12, bg = "black",width = 30, height = 30, relief = 'groove', highlightcolor = "black")
    btn_column.grid(column=col, row=row)
    col += 1
    

#button on top
for i in range (10):
    btn_column = Button(master, text="Tran", activebackground = "grey", command = color)
    btn_column.grid(column=i, row=0)

#grid layout
for i in range (10):
    for g in range (1,10):    
        btn_column = Canvas(master,bd=12, bg = "grey",width = 30, height = 30, relief = 'groove', highlightcolor = "black")
        btn_column.grid(column=i, row=g)


# infinite loop which can be terminated by keyboard 
# or mouse interrupt 
mainloop() 