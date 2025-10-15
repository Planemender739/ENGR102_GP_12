# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Thomas Tang
# Section: 511
# Assignment: 
# Date: October 8th, 2025

import math

# Ask the user for number of digits
digits = int(input("Please enter the number of digits of precision for tau: "))

tau = 2 * math.pi

factor = 10 ** digits
tau_rounded = int(tau * factor + 0.5) / factor

# Format the output with exactly 'digits' decimal places
if digits == 0:
    output = f"{int(tau_rounded)}"
else:
    output = f"{tau_rounded:.{digits}f}"

print(f"The value of tau to {digits} digits is: {output}")
