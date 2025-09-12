# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Thomas Tang
# Section: 511
# Assignment: Lab 04
# Date: September 12th, 2025

from math import *

print("Please enter the coefficient A: ", end="")
A = int(input())
print("Please enter the coefficient B: ", end="")
B = int(input())
print("Please enter the coefficient C: ", end="")
C = int(input())

if A == 0 and B == 0:
    if C != 0:
        print("You entered an invalid combination of coefficients!")
    else:
        pass
elif A == 0:
    root = -C / B
    print(f"The root is x = {root}")
else:
    D = B**2 - 4 * A * C # discriminant

    if D < 0:
        i = sqrt(abs(D))
        real = -B / (2 * A)
        imag = i / (2 * A)
        print(f"The roots are x = {real} + {imag}i and x = {real} - {imag}i")
    else:
        root1 = (-B + sqrt(D)) / (2 * A)
        root2 = (-B - sqrt(D)) / (2 * A)

        if D == 0:
            print(f"The root is x = {root1}")
        else:
            print(f"The roots are x = {root1} and x = {root2}")

"""
Please enter the coefficient A: 1
Please enter the coefficient B: 2
Please enter the coefficient C: 1
The root is x = -1.0
"""