# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Thomas Tang
# Section: 511
# Assignment: Lab 04
# Date: September 12th, 2025

############ Part A ############

a = 1/7
print(f"a = {a}")
b = a * 7
print(f"b = a * 7 = {b}") # 1.0

c = 2 * a
d = 5 * a
f = c + d
print(f"f = 2 * a + 5 * a = {f}") # 0.999...

from math import sqrt
x = sqrt(1/3)
print(f"x = {x}")
y = x * x * 3
print(f"y = x * x * 3 = {y}") # 1.0
z = x * 3 * x
print(f"z = x * 3 * x = {z}") # 0.999...

############ Part B ############

TOL = 1e-10

if abs(b - f) < TOL:
    print(f"b and f are equal within tolerance of {TOL}")
else:
    print(f"b and f are NOT equal within tolerance of {TOL}")

if abs(y - z) < TOL:
    print(f"y and z are equal within tolerance of {TOL}")
else:
    print(f"y and z are NOT equal within tolerance of {TOL}")

############ Part C ############

m = 0.1
print(f"m = {m}")
n = 3 * m
print(f"n = 3 * m = 0.3 {n == 0.3}")
p = 7 * m
print(f"p = 7 * m = 0.7 {p == 0.7}")
q = n + p
print(f"q = n + p = 1 {q == 1}")