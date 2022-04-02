
import random
from graphics import *

def get_words(file_name):
    f = open(file_name, 'r')
    return f.readlines()

def get_random_word(words):
    x = random.randint(0, len(words)-1)
    return str(words[x]).strip()

def letter_in_secret_word(letter, secret_word):
    if letter in secret_word:
        return True
    else:
        return False

def already_guessed(letter, guesses):
    if letter in guesses:
        return True
    else:
        return False

def make_hidden_secret(secret_word, guesses):
    outList = []
    outString = ""
    for i in range(len(secret_word)):
        outList.append("_")

    for ltr in guesses:
        if ltr in secret_word:
            indices = []
            for x in range(len(secret_word)):
                if secret_word[x] == ltr:
                    indices.append(x)
            for ind in indices:
                outList[ind] = ltr

    for ch in outList:
        outString += ch + " "
    return outString.strip()

def won(guessed):
    if "_" in guessed:
        return False
    else:
        return True

def play_graphics(secret_word):
    win = GraphWin('Hangman', 650, 800)
    win.setBackground("white")
    line1 = Line(Point(325, 100), Point(325, 550))
    line2 = Line(Point(325,100), Point(175,100))
    line3 = Line(Point(175, 100), Point(175,200))
    line4 = Line(Point(175, 550), Point(400, 550))
    line1.draw(win), line2.draw(win), line3.draw(win), line4.draw(win)

    figure = []
    head = Circle(Point(175,230), 30)
    body = Line(Point(175,260), Point(175, 460))
    armL = Line(Point(175, 270), Point(125, 240))
    armR = Line(Point(175, 270), Point(225, 240))
    legL = Line(Point(175,460), Point(125, 535))
    legR = Line(Point(175,460), Point(225, 535))
    figure.append(head), figure.append(body), figure.append(armL), figure.append(armR), figure.append(legL), figure.append(legR)

    inputBox = Entry(Point(325, 700), 6)
    inputBox.draw(win)
    instr = Text(Point(230, 700), "Guess a letter: ")
    instr.draw(win)

    numOfGuesses = 6
    guesses = []
    while numOfGuesses != 0 and won(make_hidden_secret(secret_word, guesses)) == False:
        bound = Text(Point(500, 110), "Already guessed: {}".format(guesses))
        restr = Text(Point(175, 600), "Guesses Remaining: {}".format(numOfGuesses))
        output = make_hidden_secret(secret_word, guesses)
        res = Text(Point(325, 675), output)
        bound.draw(win), restr.draw(win), res.draw(win)

        #newLetter = inputBox.getText()
        newLetter = win.getKey()

        if already_guessed(newLetter, guesses) == False:
            guesses.append(newLetter)
        else:
            err = Text(Point(325,650),"Letter already guessed, enter another letter.")
            err.draw(win)
            inputBox.setText("")
            newLetter = win.getKey()
            err.undraw()
            guesses.append(newLetter)

        if letter_in_secret_word(newLetter, secret_word) == False:
            figure[0].draw(win)
            figure.pop(0)
            numOfGuesses -= 1
            inputBox.setText("")

        else:
            inputBox.setText("")
            #continue
        bound.undraw(), restr.undraw(), res.undraw()

    final = Text(Point(325, 650), "")
    sec = Text(Point(325, 665), "")
    if won(make_hidden_secret(secret_word, guesses)) == True:
        final.setText("Winner!")
        sec.setText(secret_word)
    elif won(make_hidden_secret(secret_word, guesses)) == False or numOfGuesses == 0:
        final.setText("Sorry, you did not guess the word correctly.")
        sec.setText("The secret word is '{}'".format(secret_word))
    inputBox.undraw()
    instr.undraw()
    final.draw(win)
    sec.draw(win)

    win.getMouse()
    win.close


def play_command_line(secret_word):
    numOfGuesses = 6
    guesses = []
    while numOfGuesses != 0 and won(make_hidden_secret(secret_word, guesses)) == False:
        print("Already guessed: {}".format(guesses))
        print("Guesses Remaining: {}".format(numOfGuesses))
        print(make_hidden_secret(secret_word, guesses))
        newLetter = input("Guess a letter: ")

        if already_guessed(newLetter, guesses) == False:
            guesses.append(newLetter)
        else:
            newLetter = input("Letter already guessed, enter another letter.")
            guesses.append(newLetter)

        if letter_in_secret_word(newLetter, secret_word) == False:
            numOfGuesses -= 1
            print()
        else:
            print()
            continue

    if won(make_hidden_secret(secret_word, guesses)) == True:
        print("Winner!")
        print(secret_word)
    else:
        print("Sorry, you did not guess the word correctly.")
        print("The secret word is '{}'".format(secret_word))

if __name__ == '__main__':
    listOfWords = get_words("words.txt")
    ranWord = get_random_word(listOfWords)
    #play_command_line(ranWord)
    play_graphics(ranWord)
