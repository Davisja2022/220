import math
from graphics import *
from face import Face

def fibonacci(n):
    i = 2
    seq = [1, 1]
    if n < 1:
        return None
    elif n == 1:
        return 1
    elif n == 2:
        return 1
    while n != i:
        seq.append(seq[i-1] + seq[i-2])
        i += 1
    else:
        return seq[-1]

def double_investment(principle,rate):
    a = principle * (1 + rate)
    year = 1
    while a < principle * 2:
        a = a * (1 + rate)
        year += 1
    else:
        return year

def syracuse(n):
    seq = [n]
    while seq[-1] != 1:
        if seq[-1] % 2 == 1:
            seq.append(3 * seq[-1] + 1)
        elif seq[-1] % 2 == 0:
            seq.append(int(seq[-1] / 2))
    else:
        return seq

def goldbach(n):
    if n % 2 == 1:
        return None


def main():
    win = GraphWin("My Face", 600, 600)
    cen = Point(300, 300)
    siz = 250
    item = Face(win,cen,siz)
    item.smile()
    win.getMouse()
    win.close()

main()
