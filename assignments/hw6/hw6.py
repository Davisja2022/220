"""
Name: <Jessica Davis>
<Hw4>.py

Problem: <Brief, one or two sentence description of the problem that this program solves, in your own words.>

Certification of Authenticity:
<include one of the following>
I certify that this assignment is entirely my own work.
I certify that this assignment is my own work, but I discussed it with: <Jessica Davis>
"""
import math

def cash_converter():
    user_input = eval(input('enter an integer: '))
    print('that is ${:.2f}'.format(user_input))

def encode():
    user_input = (input('Enter a message: '))
    user_input2 = eval(input('Enter a key: '))
    answer = "".join(chr(ord(c)+user_input2) for c in user_input)
    print(answer)

def sphere_area(radius):
    area = float(4 * math.pi * radius **2)
    return area

def sphere_volume(radius):
    volume = float((4/3) * math.pi * radius**3)
    return volume

def sum_n(number):
    sum = 0
    for i in range(1, number+1):
        sum += i
    return sum

def sum_n_cubes(number):
    sum = 0
    for i in range(1, number+1):
        sum += (i**3)
    return sum


def encode_better():
    user = input("Enter word: ")
    user2nd = input("Enter key: ")
    shift_list = []
    ch_list = []

    answer = ""

    for keys in user2nd:
        shift_list.append(keys)
    for ch in user:
        ch_list.append(ch)

    for i in range(len(user)):
        shift = (ord(shift_list[i % len(shift_list)]) - 65) % 58
        answer += chr((ord(ch_list[i]) + shift - 58))


    print(answer)



if __name__ == '__main__':
     #cash_converter()
     # res = sphere_area(13)
     # print(res)
     # res = sphere_volume(13)
     # print(res)
     # res = sum_n(100)
     # print(res)
     # res = sum_n_cubes(13)
     # print(res)
    # encode_better()


    encode()
