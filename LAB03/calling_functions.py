# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Thomas Tang
# Section: 511
# Assignment: Lab 03
# Date: September 9th, 2025

from math import *

def printresult(shape, side, area):
    '''Print the result of the calculation'''
    print(f'A {shape} with side {side:.2f} has area {area:.3f}')

"""
Please enter the side length: 1.25
A triangle with side 1.25 has area 0.677
A square with side 1.25 has area 1.562
A pentagon with side 1.25 has area 2.688
A hexagon with side 1.25 has area 4.059
A dodecagon with side 1.25 has area 17.494
"""

# get input
side = float(input("Please enter the side length: "))
triangle_area = (sqrt(3) / 4) * side ** 2
printresult("triangle", side, triangle_area)
square_area = side ** 2
printresult("square", side, square_area)
pentagon_area = (1 / 4) * sqrt(5 * (5 + 2 * sqrt(5))) * side ** 2
printresult("pentagon", side, pentagon_area)
hexagon_area = (3 * sqrt(3) / 2) * side ** 2
printresult("hexagon", side, hexagon_area)
dodecagon_area = 3 * (2 + sqrt(3)) * side ** 2
printresult("dodecagon", side, dodecagon_area)