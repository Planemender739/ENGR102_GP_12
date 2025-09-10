# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Names: Ashrith Talluri
# 
# 
# 
# 
# Section: 511
# Assignment: Lab Topic 3 part 1
# Date: 2/9/2025
#
#
# YOUR CODE HERE
#
import math

time1 = float(input("Enter time 1: "))    #these are for all the times/positions - putting them into variables
x1 = float(input("Enter the x position of the object at time 1: "))
y1 = float(input("Enter the y position of the object at time 1: "))
z1 = float(input("Enter the z position of the object at time 1: "))
time2 = float(input("Enter time 2: "))
x2 = float(input("Enter the x position of the object at time 2: "))
y2 = float(input("Enter the y position of the object at time 2: "))
z2 = float(input("Enter the z position of the object at time 2: "))

positionx = x1 + (time1 - time1) * (x2 - x1) / (time2 - time1)
positiony = y1 + (time1 - time1) * (y2 - y1) / (time2 - time1)
positionz = z1 + (time1 - time1) * (z2 - z1) / (time2 - time1)
print("")
print(f"At time {time1 * 1:.2f} seconds the object is at ({positionx:.3f}, {positiony:.3f}, {positionz:.3f})")

positionx2 = x1 + ( (time1 + (time2 - time1)/4) - time1 ) * (x2 - x1) / (time2 - time1)  #I just kinda repeated that as the code went on
positiony2 = y1 + ( (time1 + (time2 - time1)/4) - time1 ) * (y2 - y1) / (time2 - time1)
positionz2 = z1 + ( (time1 + (time2 - time1)/4) - time1 ) * (z2 - z1) / (time2 - time1)

print(f"At time {time1 + ((time2 - time1)/4):.2f} seconds the object is at ({positionx2:.3f}, {positiony2:.3f}, {positionz2:.3f})")

positionx3 = x1 + ( (time1 + (2*(time2 - time1)/4)) - time1 ) * (x2 - x1) / (time2 - time1)  #I just kinda repeated that as the code went on
positiony3 = y1 + ( (time1 + (2*(time2 - time1)/4)) - time1 ) * (y2 - y1) / (time2 - time1)
positionz3 = z1 + ( (time1 + (2*(time2 - time1)/4)) - time1 ) * (z2 - z1) / (time2 - time1)

print(f"At time {time1 + (2 *((time2 - time1)/4)):.2f} seconds the object is at ({positionx3:.3f}, {positiony3:.3f}, {positionz3:.3f})")

positionx4 = x1 + ( (time1 + (3*(time2 - time1)/4)) - time1 ) * (x2 - x1) / (time2 - time1)  #I just kinda repeated that as the code went on
positiony4 = y1 + ( (time1 + (3*(time2 - time1)/4)) - time1 ) * (y2 - y1) / (time2 - time1)
positionz4 = z1 + ( (time1 + (3*(time2 - time1)/4)) - time1 ) * (z2 - z1) / (time2 - time1)

print(f"At time {time1 + (3 *((time2 - time1)/4)):.2f} seconds the object is at ({positionx4:.3f}, {positiony4:.3f}, {positionz4:.3f})")

positionx5 = x1 + ( (time1 + (4*(time2 - time1)/4)) - time1 ) * (x2 - x1) / (time2 - time1)  #I just kinda repeated that as the code went on
positiony5 = y1 + ( (time1 + (4*(time2 - time1)/4)) - time1 ) * (y2 - y1) / (time2 - time1)
positionz5 = z1 + ( (time1 + (4*(time2 - time1)/4)) - time1 ) * (z2 - z1) / (time2 - time1)

print(f"At time {time1 + (4 *((time2 - time1)/4)):.2f} seconds the object is at ({positionx5:.3f}, {positiony5:.3f}, {positionz5:.3f})")