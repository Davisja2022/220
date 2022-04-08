from lab10.door import Door
from lab10.button import Button
from graphics import*
from random import randint

def three_door_game():
    win = GraphWin('Three Door Game', 700, 700)
    win.setBackground('blue')
    door = Door(Rectangle(Point(175, 350),Point(215,600)), 'door 1')
    door.color_door('brown')
    door.draw(win)
    door_two = Door(Rectangle(Point(350, 350), Point(390, 600)), 'door 2')
    door_two.color_door('brown')
    door_two.draw(win)
    door_three = Door(Rectangle(Point(525, 350), Point(565, 600)), 'door 3')
    door_three.color_door('brown')
    door_three.draw(win)
    button = Button(Rectangle(Point(450,50), Point(450,125)), 'Quit')
    button.draw(win)

    keep_wins = Rectangle(Point(50, 50), Point(125, 125))
    wins = Text(Point(90, 45), "Wins")
    keep_wins.draw(win)
    wins.draw(win)
    win_count = 0
    win_text = Text(keep_wins.getCenter(), str(win_count))
    win_text.draw(win)
    keep_loss = Rectangle(Point(125, 50), Point(200, 125))
    loss = Text(Point(150, 45), "Losses")
    keep_loss.draw(win)
    loss.draw(win)
    loss_count = 0
    loss_text = Text(keep_loss.getCenter(), str(loss_count))
    loss_text.draw(win)

    instructions = Text(Point(350, 270), "I have a secret door!")
    instructions.draw(win)

    interact = Text(Point(350,650), 'Click to guess where the secret door is')
    interact.draw(win)

    random_door = [door, door_two, door_three]
    #use a list so it pull 0,1,2 and not object
    random_door[randint(0, len(random_door)-1)].set_secret(True)
    user_click = win.getMouse()
    while not button.is_clicked(user_click):
        for doors in random_door:
            if doors.is_secret():
                doors.color_door('light green')
                win_count += 1
                win_text.setText(str(win_count))
                instructions.setText('You Win!')
                interact.undraw()
            else:
                interact.undraw()
                doors.color_door('pink')
                loss_count += 1
                loss_text.setText(str(loss_count))
                if door.is_secret():
                    door.color_door('green')
                elif door_two.is_secret():
                    door_two.color_door('green')
                elif door_three.is_secret():
                    door_two.color_door('green')
                instructions.setText('Sorry, Incorrect!')
        play_again = Text(Point(250, 500), 'Click anywhere to play again')
        play_again.draw(win)
        user_click = win.getMouse()
        if button.is_clicked(user_click):
            break
        for doors in random_door:
            door.color_door('grey')
            doors.set_secret(False)
        random_door[randint(0, len(random_door) - 1)].set_secret(True)
        play_again.undraw()
        interact.setText('Click to guess')
        instructions.setText('I have a secret door!')

    win.getMouse()

    win.close()


three_door_game()





