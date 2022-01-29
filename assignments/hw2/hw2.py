"""
Name: <Jessica Davis>
<ProgramName>.py

Problem: <Brief, one or two sentence description of the problem that this program solves, in your own words.>

Certification of Authenticity:
<include one of the following>
I certify that this assignment is entirely my own work.
I certify that this assignment is my own work, but I discussed it with: <Jessica Davis>
"""
import math
import pprint


def sum_of_threes():
    upper_bound = int(input("what is the upper bound?"))
    upper_values = upper_bound * 3
    print("sum of threes is", upper_values)




def multiplication_table():
  for row in range(1,11):
      for col in range(1,11):
          values = row * col
          print(values, end='\t')
      print()


def triangle_area():
    side_a = eval(input('enter the side length of a:'))
    side_b = eval(input('enter the side length of b:'))
    side_c = eval(input('enter the side length of c:'))
    side_sum = (side_a + side_b + side_c) / 2
    area_1 = (side_sum * (side_sum - side_a) * (side_sum - side_b) * (side_sum - side_c))
    area_final = math.sqrt(area_1)
    print('area is:', area_final)


def sum_squares():
   sum_of_squares = int(input(How many numbers you have?))
   s



def power():
    base = int(input('enter base:'))
    exponent = int(input('enter exponent:'))
    ans = 1
    for i in range(exponent):
        ans=ans*base
print(base,'^', exponent,'=', ans)






    if __name__ == '__main__':
        pass