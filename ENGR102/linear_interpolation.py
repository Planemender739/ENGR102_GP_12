from math import *

def printresult(shape, side, area):
    '''Print the result of the calculation'''
    print(f'A {shape} with side {side:.2f} has area {area:.3f}')

side = float(input("Please enter the side length: "))
shape = input("What shape? (triangle, square, pentagon, hexagon, dodecagon): ").lower()

if shape == "triangle":
    area = (sqrt(3)/4) * side**2
elif shape == "square":
    area = side**2
elif shape == "pentagon":
    area = 0.25 * sqrt(5 * (5 + 2 * sqrt(5))) * side**2
elif shape == "hexagon":
    area = 3 * (sqrt(3)/2) * side**2
elif shape == "dodecagon":
    area = 3 * (2 + sqrt(3)) * side**2
else:
    print("Unknown shape!")
    area = None

if area is not None:
    printresult(shape, side, area)

