# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Thomas Tang
# Section: 511
# Assignment: Lab 06
# Date: September 29th, 2025

"""
Enter an integer: 2
Enter another integer: 3
1
Howdy
Whoop
...
Whoop
Howdy
"""

a = int(input("Enter an integer: "))
b = int(input("Enter another integer: "))

for i in range(1, 101):
    if i % a == 0 and i % b == 0: # both
        print("Howdy Whoop")
    elif i % a == 0:
        print("Howdy")
    elif i % b == 0:
        print("Whoop")
    else:
        print(i)