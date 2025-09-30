# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Thomas Tang
# Section: 511
# Assignment: Lab 06
# Date: September 29th, 2025

"""
Enter the side length in meters: 1
Enter the number of layers: 5
You need 85.00 m^2 of gold foil to cover the pyramid
"""

print("Enter the side length in meters: ", end="")

s = float(input())

print("Enter the number of layers: ", end="")

n = int(input())

# arithmetic progression
print(f"You need {n * (3 * n + 2) * s**2:.2f} m^2 of gold foil to cover the pyramid")