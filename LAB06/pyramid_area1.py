# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Thomas Tang
# Section: 511
# Assignment: Lab 06
# Date: September 29th, 2025

print("Enter the side length in meters: ", end="")

s = float(input())

print("Enter the number of layers: ", end="")

n = int(input())

exposed_faces = 0
    
for z in range(n):
    size = n - z 
    for x in range(size):
        for y in range(size):
            if x == size - 1:  
                exposed_faces += 1
            if x == 0:  
                exposed_faces += 1
            if y == size - 1:  
                exposed_faces += 1
            if y == 0:  
                exposed_faces += 1
            if z == n - 1:  
                exposed_faces += 1
            else:
                if x >= n - (z + 1) or y >= n - (z + 1): # check top
                    exposed_faces += 1


print(f"You need {exposed_faces * (s**2):.2f} m^2 of gold foil to cover the pyramid")