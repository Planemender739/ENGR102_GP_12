# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Lane Mack
# Section: Engr 102-511
# Assignment: Lab Topic 3 Individual
# Date: 6 September 2025
#
#writing_functions


from math import *

def printresult(shape, side, area):
    shape=str(input("Enter the shape:"))
    side=float(input("Please enter the side length:"))
    area_of_triangle=((sqrt(3)/4)*(side**2))
    print("A triangle with side length",side,"has area",f"{area_of_triangle:.3f}")
    area_of_square=((side**2))
    print("A square with side length",side,"has area",f"{area_of_square:.3f}")
    area_of_pentagon=.25*(sqrt((5*(5+2*sqrt(5)))))*side**2
    print("A pentagon with side length",side,"has area",f"{area_of_pentagon:.3f}")
    area_of_hexagon=3*((sqrt(3))/2)*side**2
    print("A hexgon with side length",side,"has area",f"{area_of_hexagon:.3f}")
    area_of_dodecagon=(3*(2+sqrt(3)))*side**2
    print("A dodecagon with side length",side,"has area",f"{area_of_dodecagon:.3f}")
    

# example function call:
# printresult(<string of shape name>, <float of side>, <float of area>)
# printresult('square', 2.236, 5)
