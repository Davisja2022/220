'''
Jessica Davis
Lab4.py
Using Graphics and strings to create user interactive programs .
This is my work and my work only. - Jessica Davis
'''

from graphics import *

def triangle():
    win = GraphWin('Triangle', 500, 500)
    message_one = Text(Point(250, 25), "Click three points in the window.")
    message_one.draw(win)

    p1 = win.getMouse()
    message_one.undraw()
    p2 = win.getMouse()
    p3 = win.getMouse()

    tri_object = Polygon(p1, p2, p3)
    tri_object.draw(win)

    side_one_x = p1.getX() - p2.getX()
    side_one_y = p1.getY() - p2.getY()
    distance_1 = (side_one_x**2 + side_one_y**2)**0.5

    side_two_x = p2.getX() - p3.getX()
    side_two_y = p2.getY() - p3.getY()
    distance_2 = (side_two_x**2 + side_two_y**2)**0.5

    side_3_x = p3.getX() - p1.getX()
    side_3_y = p3.getY() - p1.getY()
    distance_3 = (side_3_x**2 + side_3_y**2)**0.5

    perimeter = distance_1 + distance_2 + distance_3
    area = (distance_1 + distance_2 + distance_3) / 2

    message_two = Text(Point(250, 425), 'Perimeter: ' + (perimeter))
    message_two.draw(win)
    message_three = Text(Point(250, 450), 'Area: ' + (area))
    message_three.draw(win)

    message_four = Text(Point(250, 25), 'Click to close window.')
    message_four.draw(win)
    win.getMouse()
    win.close()


def color_shape():
    '''Create code to allow a user to color a shape by entering rgb amounts'''

    # create window
    win_width = 400
    win_height = 400
    win = GraphWin("Color Shape", win_width, win_height)
    win.setBackground("white")

    # create text instructions
    msg = "Enter color values between 0 - 255\nClick window to color shape"
    inst = Text(Point(win_width / 2, win_height - 20), msg)
    inst.draw(win)

    # create circle in window's center
    shape = Circle(Point(win_width / 2, win_height / 2 - 30), 50)
    shape.draw(win)

    # redTexPt is 50 pixels to the left and forty pixels down from center
    red_text_pt = Point(win_width / 2 - 50, win_height / 2 + 40)
    red_text = Text(red_text_pt, "Red: ")
    red_text.setTextColor("red")
    user_input = Entry(Point(win_width / 2 - 20, win_height / 2 + 40), 5)
    user_input.draw(win)
    redAmt = user_input.getText()

    # green_text_pt is 30 pixels down from red
    green_text_pt = red_text_pt.clone()
    green_text_pt.move(0, 30)
    green_text = Text(green_text_pt, "Green: ")
    green_text.setTextColor("green")
    user_input_green = Entry(Point(win_width / 2 - 15, win_height / 2 + 70), 5)
    user_input_green.draw(win)
    greenAmt = user_input_green.getText()

    # blue_text_pt is 60 pixels down from red
    blue_text_pt = red_text_pt.clone()
    blue_text_pt.move(0, 60)
    blue_text = Text(blue_text_pt, "Blue: ")
    blue_text.setTextColor("blue")
    user_input_blue = Entry(Point(win_width / 2 - 15, win_height / 2 + 100), 5)
    user_input_blue.draw(win)
    blueAmt = user_input_blue.getText()

    red_text.draw(win)
    green_text.draw(win)
    blue_text.draw(win)

    for i in range(5):
        win.getMouse()
        redAmt = eval(user_input.getText())
        greenAmt = eval(user_input_green.getText())
        blueAmt= eval(user_input_blue.getText())
        shape.setFill(color_rgb(redAmt, greenAmt, blueAmt))

 # Wait for another click to exit
    win.getMouse()
    win.close()


def process_string():
    user_input = input('Enter characters:')
    first_character = user_input[0]
    last_character = user_input[-1]
    output_three = user_input[2:5]
    first_and_last = first_character + last_character
    first_three = user_input[0:3] * 10
    character_count = len(user_input)
    print(first_character)
    print(last_character)
    print(output_three)
    print(first_and_last)
    for i in (user_input):
        print(i)
    print(first_three)
    print(character_count)


def process_list():
    pt = Point(5, 10)
    values = [5, 'hi', 2.5, 'there', pt, '7.2']
    x = values[1] + values[3]
    print(x)
    x = values[0] + values[2]
    print(x)
    x = values[1] * 5
    print(x)
    x = [2.5, 'there', pt]
    print(x)
    x = [2.5, 'there', 5]
    print(x)
    x = [2.5, 5, 7.2]
    print(x)
    x = 5 + 2.5 + 7.2
    print(x)
    x = len(values)
    print(x)


def another_series():
    user_input = eval(input('Enter number of terms: '))
    acc_total = 0
    for i in range(user_input):
        x = 2+ (2 * (i % 3))
        print(x, end=" ")
        acc_total = acc_total + x
    print()
    print('Sum', acc_total)



def target():
    win = GraphWin('Target', 300, 300)
    center = Point(150, 150)

    white_circle = Circle(center, 100)
    white_circle.setFill('white')
    white_circle.draw(win)

    black_circle = Circle(center, 80)
    black_circle.setFill('black')
    black_circle.draw(win)

    blue_circle = Circle(center, 60)
    blue_circle.setFill('blue')
    blue_circle.draw(win)

    red_circle = Circle(center, 40)
    red_circle.setFill('red')
    red_circle.draw(win)

    yellow_circle = Circle(center, 20)
    yellow_circle.setFill('yellow')
    yellow_circle.draw(win)

    win.getMouse()
    win.close()


color_shape()
# triangle()