# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Thomas Tang
# Section: 511
# Assignment: Lab 06
# Date: September 29th, 2025


a = int(input("Enter an integer: "))
b = int(input("Enter another integer: "))

s = 0

for i in range(a, b + 1):
    s += i # add to sum

print("The sum of all integers from", a, "to", b, "is", s)