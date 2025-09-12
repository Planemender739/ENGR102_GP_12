# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Thomas Tang
# Section: 511
# Assignment: Lab 04
# Date: September 12th, 2025

print("Please enter the coefficient A: ", end="")
A = int(input())
print("Please enter the coefficient B: ", end="")
B = int(input())
print("Please enter the coefficient C: ", end="")
C = int(input())

# build string
str = ""

if A != 0:
    if A < 0:
        str += " - "
    elif str != "":
        str += " + "
    elif str == "":
        str += " "
    if abs(A) == 1:
        str += "x^2"
    else:
        str += f"{abs(A)}x^2"

if B != 0:
    if B < 0:
        str += " - "
    elif str != "":
        str += " + "
    elif str == "":
        str += " "
    if abs(B) == 1:
        str += "x"
    else:
        str += f"{abs(B)}x"

if C != 0:
    if C < 0:
        str += " - "
    elif str != "":
        str += " + "
    elif str == "":
        str += " "
    str += f"{abs(C)}"

print(f"The quadratic equation is{str} = 0")