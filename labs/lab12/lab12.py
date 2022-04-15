'''
Jessica Davis
Lab12.py
this work is mine and mine only - Jessica Davis
'''

from random import randint

def find_and_remove(list, value):
# find value and insert name
    find = list.index(value)
    list.remove(value)
    list.insert(find, 'Jessica')
    print(list)


def good_input():
    user = eval(input('Enter a number 1-10: '))
    while user >= 0 and user <= 11:
        if user < 1:
            print('Too Low!')
            user = eval(input('Enter a number 1-10: '))
        elif user > 10:
            print('Too High!')
            user = eval(input('Enter a number 1-10: '))
        else:
            return user

#OUTPUTS A NUMBER
#USER INSTRUCTIONS REQUIRED

def num_digits():
    user = eval(input('Enter a positive integer: '))
    acc = 0
    while user != 0:
    #is not violates syntax
        acc = acc + 1
        user //= 10
    print('Number of digits: ', acc)


#USER INTERS NUMBER ID O OR -, END.
#INTEGER DIVISION

def hi_lo_game():
    random = randint(1, 100)
    print(random)
    guesses = 0
    switch = False
    while guesses != 7 and switch == False:
        user = eval(input("Enter a Number: "))
        if user > random:
            guesses += 1
            print('too high')
        elif user < random:
            guesses += 1
            print('Too Low')
        else:
            switch = True
            guesses += 1
            print("you win in {} guesses".format(guesses))
    else:
        if guesses == 7:
            print("Sorry, you lose. The number was {}".format(random))

#RANDOM NUMBER 1-10, 7 GUESSES ONLY, IF RIGHT END GAME.
# define i first before while loop
# while loop has to change while inside the loop



