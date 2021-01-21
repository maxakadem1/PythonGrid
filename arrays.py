#importing libraries
from tkinter import *
import random

#global variables
numGrid = 3

#main window
master = Tk()
master.configure(background='white')

#title
master.title("Title of window")

#metod for click
col = 0
row = 1
active = False
color2 = ""
def color():
    global col
    global row
    global active
    global color2
    

    if col>numGrid-1 :
        row+=1
        col=0

    if row>numGrid-1:
        active=False
        row=1
        col=0

    if not active:
        color2 ="#" + "%06x" % random.randint(0, 0xFFFFFF)
        active = True
    btn_column = Canvas(master,bd=12, bg = color2,width = 30, height = 30, relief = 'groove', highlightcolor = "black")
    btn_column.grid(column=col, row=row)
    col += 1


#button on top
for i in range (numGrid):
    btn_column = Button(master, text="Tran", activebackground = "grey", command = color)
    btn_column.grid(column=i, row=0)

#grid layout
for i in range (numGrid):
    for g in range (1,numGrid):
        btn_column = Canvas(master,bd=12, bg = "grey",width = 30, height = 30, relief = 'groove', highlightcolor = "black")
        btn_column.grid(column=i, row=g)


# infinite loop which can be terminated by keyboard 
# or mouse interrupt 
mainloop()
