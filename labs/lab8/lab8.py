import math
from random import randint
from graphics import *

def get_random(move_amount):
    return randint(-move_amount, move_amount)

def did_collide(ball, ball_2):
    x_form = abs((ball.getCenter().getX() - ball_2.getCenter().getX())**2)
    y_form = abs((ball.getCenter().getY() - ball_2.getCenter().getY())**2)
    distance = math.sqrt((y_form) + (x_form))
    if distance > ball.getRadius() + ball_2.getRadius():
        return False
    else:
        return True

def hit_vertical(ball, win):
    bottom = win.getHeight()
    top_form = ball.getCenter().getY() - ball.getRadius()
    bottom_form = ball.getCenter().getY() + ball.getRadius()
    if top_form< 0 or bottom_form > bottom:
        return True
    else:
        return False

def hit_horizontal(ball, win):
    right = win.getWidth()
    left_form = ball.getCenter().getx() - ball.getRadius()
    right_form = ball.getCenter().getX() + ball.getRadius()
    if left_form < 0 or right_form > right:
        return True
    else:
        return False

def get_random_color():
    r_value= randint(0,255)
    g_value = randint(0,255)
    b_value = randint(0,255)
    return color_rgb(r_value, g_value, b_value)

def bumper():
    win_width = 400
    win_height = 400
    win = GraphWin("bumper",win_width,win_height)

    circle_1= Circle(Point(randint(0,400), randint (0,400)), 25)
    circle_2 = Circle(Point (randint (0, 400), randint(0,400)),25)
    circle_1.setFill(get_random_color())
    circle_2.setFill(get_random_color())
    circle_1.draw(win)
    circle_2.draw(win)

    move_x_1=get_random(20)
    move_y_1=get_random(35)
    move_x_2=get_random(20)
    move_y_2=get_random(35)
    while not win.checkMouse():
        time.sleep(0.2)

        if hit_vertical(circle_1,win):
            move_y_1=-move_y_1
        if hit_vertical(circle_2,win):
            move_y_2= -move_y_2
        if hit_horizontal(circle_1.win):
            move_x_1=-move_x_1
        if hit_horizontal(circle_2,win):
            move_x_2=-move_x_2
        if did_collide(circle_1,circle_2):
            move_x_1=-move_x_1
            move_x_2=-move_x_2
            move_y_1=-move_y_1
            move_y_2=-move_y_2
        else:

            win.close()


bumper()