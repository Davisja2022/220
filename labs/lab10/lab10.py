'''
Jessica Davis
Lab10.py
Creating a window that is user interactive and utilizes user-defined classes and list of objects
This is my work and my work only. - Jessica Davis
'''

from graphics import *
from button import Button
from door import Door
def main():
    switch = False
    terminate = False
    win = GraphWin('Test', 700, 700)
    square = Button(Rectangle(Point(75,75),Point(575,150)), "Exit.")
    square.draw(win)
    square.color_button("red")

    door = Door(Rectangle(Point(175,500),Point(5,585)), "Closed")
    door.draw(win)
    door.color_door("orange")

    while not terminate:
        select = win.getMouse()
        if square.is_clicked(select) == True:
            terminate = True
        if door.is_clicked(select) and switch == False:
            door.open("white", "open")
            switch = True
        elif door.is_clicked(select) and switch == True:
            door.open("orange", "Closed")
            switch = False
    else:
        win.close()



main()