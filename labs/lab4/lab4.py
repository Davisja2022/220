'''
Jessica Davis
Lab4.py
The problem being solved is to create a valentine with an animation.
This work is mine and no one elses. - Jessica Davis
'''
import time

from graphics import *


def greeting_card():
    width = 500
    height = 500
    win = GraphWin("greeting", width, height)
    shape = Polygon(Point(250, 400), Point(150, 120), Point(350, 120))
    shape.draw(win)
    shape.setOutline("red")
    shape.setFill("red")
    circle_one = Circle(Point(200,120), 50)
    circle_one.setOutline("red")
    circle_one.setFill("red")

    c_2 = Circle(Point(300,120), 50)
    c_2.setOutline("red")
    c_2.setFill("red")
    circle_one.draw(win)
    c_2.draw(win)

    inst_pt = Point(width / 2, height - 10)
    message = Text(inst_pt, "Happy Valentines Day from my heart to yours!")
    message.setTextColor("white")
    message.draw(win)

    arrow = Line(Point(0, 120), Point(120, 250))
    arrow.draw(win)
    arrow.setArrow('last')
    for i in range(5):
        arrow.move(200, 120)
        time.sleep(0.50)

    end_message = Text(Point(250,420),'Click to close anywhere')
    end_message.draw(win)
    win.getMouse()
    win.close()















'''
'''
greeting_card()





