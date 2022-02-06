"""
Name: <Jessica Davis>
<ProgramName>.py

Problem: <Brief, one or two sentence description of the problem that this program solves, in your own words.>

Certification of Authenticity:
<include one of the following>
I certify that this assignment is entirely my own work.
I certify that this assignment is my own work, but I discussed it with: <Name(s)>
"""


def average():
    grades = int(input('how many grades will you enter?:'))
    grades_acc = 0.0
    for i in range(grades):
        print('enter grade:')
        grades_entered = eval(input(' '))
        grades_acc = grades_acc + grades_entered
    print('average is: ', grades_acc / grades)


def tip_jar():
    tip_acc = 0.0
    for i in range(5):
        print('how much would you like to donate?:')
        donation_input = eval(input(' '))
        tip_acc = tip_acc + donation_input
    print('total tips:', tip_acc)


def newton():
    x_input = int(input('what number do you want to square root?: '))
    approximation_input = int(input('how many times would you like to improve the approximation?:'))
    for i in range(approximation_input):
        square_root = approximation_input + (x_input/approximation_input)
        final_approx = square_root / 2
    print('the approximation of the square root is', final_approx)



def sequence():
    terms = eval(input('how many terms would you like?:'))
    for i in range(1, terms + 1):







def pi():
    pi_terms = eval(input('how many terms in the series?:'))
    pi_acc = 0.0

    print(pi_result)





if __name__ == '__main__':
    pass
