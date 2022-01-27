"""
Jessica Davis
lab2.py
the problem being solved is calculating the root mean, harmonic mean, and geometric mean. The input and outputs are variable values and the output
is the mean of those values. the program must calculate ask the user for input (values) and either add or multiply and find the root if needed.
This is my work and my work only - Jessica Davis
"""

def means():
    means_value = int(input("how many numbers do you have?"))
    rms_acc = 0.0
    harmonic_acc = 0.0
    geometric_acc = 1
    for i in range(means_value):
        value_number = float(input("enter a number>>"))
        rms_acc = rms_acc + value_number**2
        harmonic_acc = harmonic_acc + (1 / value_number)
        geometric_acc = geometric_acc * value_number
    rms = (rms_acc / means_value) ** 0.5
    geo_mean = geometric_acc ** (1/means_value)
    print("\nthe root mean square is", rms)
    print("\n the harmonic mean is", means_value / harmonic_acc)
    print("\n the geometric mean is", geo_mean)












