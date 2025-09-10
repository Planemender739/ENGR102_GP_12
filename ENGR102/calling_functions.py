# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Lane Mack
# Section: Engr 102-511
# Assignment: Lab Topic 3 Individual
# Date: 6 September 2025
#
#calling_functions

from math import *

def printresult(shape, side, area):
    '''Print the result of the calculation'''
    print(f'A {shape} with side {side:.2f} has area {area:.3f}')

side =float(input("Please enter the side length: "))

#shape = str(input("What shape? (triangle, square, pentagon, hexagon, dodecagon): "))

#area_equations = {   #These equations are defining what each of the equations uses for the area
triangle_area=(sqrt(3)/4)*side**2
square_area= side**2
pentagon_area= .25*(sqrt(5*(5+2*sqrt(5))))*(side**2)
hexagon_area= (3*(sqrt(3)/2)*side**2)
dodecagon_area= (3*(2+sqrt(3))*side**2)


printresult("triangle",side,triangle_area)

printresult("square",side,square_area)

printresult("pentagon",side,pentagon_area)

printresult("hexagon",side,hexagon_area)

printresult("dodecagon",side,dodecagon_area)






























#if shape == "triangle":               #This is statement lets the function depend its calculation on which string shape the user entered to begin with.
  #  printresult(shape, side, area_of_triangle)
#elif shape == "square":
#    printresult(shape, side, area_of_square)
#elif shape == "pentagon":
#    printresult(shape, side, area_of_pentagon)
#elif shape == "hexagon":
#    printresult(shape, side, area_of_hexagon)
#elif shape == "dodecagon":
#    printresult(shape, side, area_of_dodecagon)






























#    side=float(input("Please enter the side length:"))
#shape=str(input("What shape? (lowercase only)"))


#(triangle)=
#print(triangle)



#square=


#pentagon=


#hexagon=


#dodecagon=

#printresult(shape,side,area)