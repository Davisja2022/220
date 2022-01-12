"""
Name: <Jessica Davis – first and last>
<ProgramName>.py

Problem: <Brief, one or two sentence description of the problem that this program solves, in your own words.>

Certification of Authenticity:
<include one of the following>
I certify that this assignment is entirely my own work.
I certify that this assignment is my own work, but I discussed it with: <Jessica Davis>
"""


def calc_rec_area():
    length = eval(input("enter the length: "))
    width = eval(input("enter the width: "))
    area = length * width
    print("Area =", area)



def calc_volume():
    length = eval(input("enter the length:"))
    width = eval(input("enter the width:"))
    height = eval(input("enter the height:"))
    volume = length * width * height
    print("volume =", volume)





def shooting_percentage():
    attempts_made = eval(input('enter the attempts:'))
    shots_made = eval(input('enter the shots:'))
    shooting_percentage = attempts_made / shots_made
    print("shooting_percentage =", shooting_percentage)



def coffee():
    coffee_weight = eval(input("how many pounds of coffee would you like?:"))
    total = coffee_weight * 10.50 + (coffee_weight * .86) + 1.50
    print("your total is: $", total)


def kilometers_to_miles():
    kilometer = eval(input("how many kilometers did you travel?:"))
    miles = kilometer * .62137
    print("total miles:", miles)


if __name__ == '__main__':
    pass
