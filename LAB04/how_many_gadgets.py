# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Thomas Tang
# Section: 511
# Assignment: Lab 04
# Date: September 12th, 2025

s = input("Please enter a positive value for day: ")

try:
    day = int(s)
    
    if day <= 0:
        print("You entered an invalid number!")
    else:
        if day <= 10:
            total = 10 * day
        elif day <= 49:
            total = (day * (day + 1)) // 2 + 45
        else:
            # total up through day 49 is 1270, then add 50 for each day from 50..day
            total = 50 * min(100, day) - 1180

        print(f"The sum total number of gadgets produced on day {day} is {total}")
except ValueError:
    print("You entered an invalid number!")
