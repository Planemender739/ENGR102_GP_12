# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Lane Mack
# Section: Engr 102-511
# Assignment: Lab Topic 1
# Date: 27 August 2025
#
#
#
#Follow_Directions.py


print("This shows the evaluation of (1-cos(x))/x^2 evaluated close to x=0")
print("My guess is that the answer will be 1")
from math import *   #This is used to make sure that all the math functions are brought forward and are ready to be used.
x=1                               #Now we will evaluate the function as values get progressively closer to zero, but never reach zero.
f=(1-cos(x))/x**2
print(f)

x=.1
f=(1-cos(x))/x**2
print(f)

x=.01
f=(1-cos(x))/x**2
print(f)

x=.001
f=(1-cos(x))/x**2
print(f)

x=.0001
f=(1-cos(x))/x**2
print(f)

x=.00001
f=(1-cos(x))/x**2
print(f)

x=.000001
f=(1-cos(x))/x**2
print(f)

x=.0000001
f=(1-cos(x))/x**2
print(f)
print()
print("I suppose my guess wasn't very good.")