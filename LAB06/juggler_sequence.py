# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Thomas Tang
# Section: 511
# Assignment: Lab 06
# Date: September 29th, 2025

import math

n = int(input("Enter a positive integer: "))
original = n
sequence = [n]
iterations = 0

while n != 1:
    if n % 2 == 0:
        n = math.floor(math.sqrt(n))
    else:
        n = math.floor(n ** 1.5)
    sequence.append(n) # add to sequence
    iterations += 1

print(f"The Juggler sequence starting at {original} is:")
print(", ".join(map(str, sequence)))
print(f"It took {iterations} iteration{'s' if iterations != 1 else ''} to reach 1")