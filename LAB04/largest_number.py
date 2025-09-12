# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Thomas Tang
# Section: 511
# Assignment: Lab 04
# Date: September 12th, 2025

print("Enter number 1: ", end="")
num1 = float(input())
print("Enter number 2: ", end="")
num2 = float(input())
print("Enter number 3: ", end="")
num3 = float(input())

# maths
largest = num1

if num2 > largest:
    largest = num2
if num3 > largest:
    largest = num3

print(f"The largest number is {largest}")

"""
Enter number 1: 1
Enter number 2: 2
Enter number 3: 3
The largest number is 3.0
"""