'''
Jessica Davis
Lab4.py
Using Graphics, strings, loops, and encoding to create user interactive program.
This is my work and my work only. - Jessica Davis
'''

from graphics import *

def vigenere():
    win_width = 500
    win_height = 500
    win = GraphWin("Vignere", win_width, win_height)
    win.setBackground("white")

    message_pos = Point(win_width / 2 - 100, win_height / 2 - 100)
    message_input = Entry(Point(win_width / 2 + 30, win_height / 2 - 100), 20)
    message = Text(message_pos, 'Message to code:')
    message_input.draw(win)

    key_pos = message_pos.clone()
    key_pos.move(0, 40)
    key_input = Entry(Point(win_width / 2 + 20, win_height / 2 - 60), 20)
    key = Text(key_pos, "Enter Keyword: ")
    key_input.draw(win)

    rectangle_shape = Rectangle(Point(150, 300), Point(350, 400))
    rectangle_text = Text(Point(250, 350), 'Encode')
    rectangle_shape.draw(win)

    key.draw(win)
    message.draw(win)
    rectangle_text.draw(win)

    win.getMouse()
    message_text = message_input.getText().upper()
    key_text = key_input.getText().upper()
    rectangle_shape.undraw()
    rectangle_text.undraw()



    answer = ''



    for i in range(len(message_text)):
        x = ord(message_text[i]) - 65
        y = ord(key_text[i % len(key_text)]) - 65
        shift_code = (x + y) % 26
        character = chr(shift_code + 65)
        answer = answer + character


    resulting_message = Text(Point(250, 300), 'Resulting Message')
    resulting_message.draw(win)
    message_one = Text(Point(250, 350), answer)
    message_one.draw(win)

    message_two = Text(Point(250, 400), 'Click to close window')
    message_two.draw(win)
    win.getMouse()
    win.close()


vigenere()




