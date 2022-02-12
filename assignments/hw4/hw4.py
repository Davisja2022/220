"""
Name: <jessica davis>
<hw4>.py

Problem: < These programs create graphics that are interactive with the user and also calculate PI Approximation>

Certification of Authenticity:
<include one of the following>
I certify that this assignment is entirely my own work.
I certify that this assignment is my own work, but I discussed it with: <Jessica Davis>
"""
import math

from graphics import *


def squares():
    # Creates a graphical window
    width = 400
    height = 400
    win = GraphWin("Clicks", width, height)

    # number of times user can move circle
    num_clicks = 5

    # create a space to instruct user
    inst_pt = Point(width / 2, height - 10)
    instructions = Text(inst_pt, "Click to move square")
    instructions.draw(win)


    # builds a circle
    shape = Rectangle(Point(50, 50), Point(50, 50))
    shape.setWidth(50)
    shape.setOutline("red")
    shape.setFill("red")
    shape.draw(win)

    # allows the user to click multiple times to move the circle
    for i in range(num_clicks):
        click = win.getMouse()
        center = shape.getCenter()  # center of circle
        clone = shape.clone()
        clone.draw(win)
        # move amount is distance from center of circle to the
        # point where the user clicked
        change_x = click.getX() - center.getX()
        change_y = click.getY() - center.getY()
        shape.move(change_x, change_y)

    end_message = Text(Point(200, 300), 'Click again to close')
    end_message.draw(win)
    win.getMouse()
    win.close()


def rectangle():
    win = GraphWin('My Square', 500,500)
    message_one = Text(Point(250, 25), "Click two points in the window.")
    message_one.draw(win)

    p1 = win.getMouse()
    message_one.undraw()
    p2 = win.getMouse()

    rect_object = Rectangle(Point(p1.getX(),p1.getY()), Point(p2.getX(),p2.getY()))
    rect_object.draw(win)
    rect_object.setFill("red")

    message_two = Text(Point(250, 25),'Click to close window.')
    message_two.draw(win)
    win.getMouse()
    win.close()






def circle():
    win = GraphWin("My Space", 700, 700)
    message_one = Text(Point(350,25), "Click two point in the window.")
    message_one.draw(win)

    p1 = win.getMouse()
    message_one.undraw()
    p2 = win.getMouse()

    rad = math.sqrt(pow(p1.getX() - p2.getX(), 2) + pow(p1.getY() - p2.getY(), 2))

    cir = Circle(Point(p1.getX(), p1.getY()), r)
    cir.draw(win)
    cir.setFill("green")

    message = 'Radius: ' + str(rad)
    message_two = Text(Point(350, 45), message)
    message_two.draw(win)

    message_three = Text(Point(350, 25), 'Click to close window.')
    message_three.draw(win)
    win.getMouse()
    win.close()


def pi2():
    n = int(input('Enter the number of terms to sum:'))
    approx = 0
    num = 4
    denominator = 1
    approx += num / denominator

    for i in range(1, n):
        denominator += 2
        num *= -1
        approx += num / denominator

    print('PI Approximation:' + str(approx))
    print('Accuracy: ' + str(abs(approx - math.pi)))


if __name__ == '__main__':
    squares()
