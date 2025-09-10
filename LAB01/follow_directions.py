# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Thomas Tang
# Section: 511
# Assignment: Lab 01
# Date: August 27th, 2025

from math import cos

print("This shows the evaluation of (1-cos(x))/x^2 evaluated close to x=0")
print("my guess: 0.5")

# def f(x):
#     return (1 - cos(x)) / (x ** 2)

# x = 1.0

# while x > 0.000000001:
#     print(f(x))
#     x /= 10

print((1 - cos(1.0)) / (1.0 ** 2))
print((1 - cos(0.1)) / (0.1 ** 2))
print((1 - cos(0.01)) / (0.01 ** 2))
print((1 - cos(0.001)) / (0.001 ** 2))
print((1 - cos(0.0001)) / (0.0001 ** 2))
print((1 - cos(0.00001)) / (0.00001 ** 2))
print((1 - cos(0.000001)) / (0.000001 ** 2))
print((1 - cos(0.0000001)) / (0.0000001 ** 2))
print()
print("my guess was spot on!")
