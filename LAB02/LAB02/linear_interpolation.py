# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Thomas Tang
# Section: 511
# Assignment: Lab 02
# Date: September 3rd, 2025

from math import *

first_time = 10
second_time = 55
first_dist = 2029
second_dist = 23029

time = 25

interpolated_dist = first_dist + (time - first_time) * (second_dist - first_dist) / (second_time - first_time)

print("Part 1:")
print("For t = 25 minutes, the position p =", interpolated_dist, "kilometers")

radius = 6745
circumference = 2 * pi * radius

time = 300

# use % to find extrapolated distance within one circumference
extrapolated_dist =  first_dist + (time - first_time) * (second_dist - first_dist) / (second_time - first_time) % circumference

print("Part 2:")
print("For t = 300 minutes, the position p =", extrapolated_dist, "kilometers")