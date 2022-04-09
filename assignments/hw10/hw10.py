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
    listOfPrimes = []
    x = 3
    while x < 150:
        y = 1
        while y < x:
            if x % y == 0:
                y += 1
                continue
        else:
            listOfPrimes.append(x)
        x += 2

    print(listOfPrimes)

    output = []
    if n % 2 == 1:
        return None
    elif n <= 2:
        return "Not greater than 2"
    else:
        i = 2
        dif = 0
        success_1 = False
        while i < n:
            l = 1
            while l < i:
                if i % l == 0:
                    i += 1
                    break
                else:
                    l += 1
            else:
                success_1 = True
                output.append(i)
                print(i)

            if success_1 == False:
                continue
            print(output)
            dif = n - i
            l = 1
            while l < dif:
                if dif % l == 0:
                    i += 1
                    break
                else:
                    l += 1
                    continue
            else:
                output.append(dif)

        print(output)


if __name__ == '__main__':

    def main():
        fibonacci(5)
        double_investment(250, .50)
        syracuse(7)
        goldbach(38)
        win = GraphWin("My Face", 600, 600)
        cen = Point(300, 300)
        siz = 250
        item = Face(win, cen, siz)
        win.getMouse()
        item.smile(win, cen, siz)
        win.getMouse()
        item.shock(win, cen, siz)
        win.getMouse()
        item.wink(win, cen, siz)
        win.getMouse()
        win.close()


        main()