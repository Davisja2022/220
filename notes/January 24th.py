'''
find the root if the quadratic
1. analysis
2. specifications
3. design
4. impl
5. test
6. maintain
strings, ints, floats are the 3 data types
inputs are, a,b,c
outputs are root 1 and root 2
get the inputs, solve for + case and solve for - case , print both solutions
'''
import math

a, b, c = eval(input("enter a, b, and c:"))
root_1 = (-b + math.sqrt(b * b - 4 * a * c)) / (2 * a)
print("root 1:" , root_1 )



'''
