# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Thomas Tang
# Section: 511
# Assignment: Lab 07 (Bonus)
# Date: October 8th, 2025

def kaprekar_steps(n):
    iterations = 0
    current = n
    while current != 6174 and current != 0:
        num_str = f"{current:04d}"
        digits = sorted(num_str)
        small = int("".join(digits))
        large = int("".join(digits[::-1]))
        current = large - small
        iterations += 1
    return iterations

total_iterations = 0

# cover all numbers
for i in range(10000):
    total_iterations += kaprekar_steps(i)

print(f"Kaprekar's routine takes {total_iterations} total iterations for all four-digit numbers")
