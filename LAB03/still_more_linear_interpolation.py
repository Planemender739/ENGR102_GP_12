# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Thomas Tang
# Section: 511
# Assignment: Lab 03
# Date: September 9th, 2025

"""
Enter time 1: 1
Enter the x position of the object at time 1: 1
Enter the y position of the object at time 1: 1
Enter the z position of the object at time 1: 1
Enter time 2: 2
Enter the x position of the object at time 2: 2
Enter the y position of the object at time 2: 2
Enter the z position of the object at time 2: 2

At time 1.00 seconds the object is at (1.000, 1.000, 1.000)
At time 1.25 seconds the object is at (1.250, 1.250, 1.250)
At time 1.50 seconds the object is at (1.500, 1.500, 1.500)
At time 1.75 seconds the object is at (1.750, 1.750, 1.750)
At time 2.00 seconds the object is at (2.000, 2.000, 2.000)
"""

# get input
print("Enter time 1: ", end="")
t1 = float(input())
print("Enter the x position of the object at time 1: ", end="")
x1 = float(input())
print("Enter the y position of the object at time 1: ", end="")
y1 = float(input())
print("Enter the z position of the object at time 1: ", end="")
z1 = float(input())
print("Enter time 2: ", end="")
t2 = float(input())
print("Enter the x position of the object at time 2: ", end="")
x2 = float(input())
print("Enter the y position of the object at time 2: ", end="")
y2 = float(input())
print("Enter the z position of the object at time 2: ", end="")
z2 = float(input())
dt = t2 - t1
dx = x2 - x1
dy = y2 - y1
dz = z2 - z1
vx = dx / dt
vy = dy / dt
vz = dz / dt
print(f"\nAt time {t1:.2f} seconds the object is at ({x1:.3f}, {y1:.3f}, {z1:.3f})")

step = (t2 - t1) / 4

t = t1 + 0.25

x_025 = x1 + vx * step
y_025 = y1 + vy * step
z_025 = z1 + vz * step
print(f"At time {t1+step:.2f} seconds the object is at ({x_025:.3f}, {y_025:.3f}, {z_025:.3f})")

x_050 = x1 + vx * step * 2
y_050 = y1 + vy * step * 2
z_050 = z1 + vz * step * 2
print(f"At time {t1+step * 2:.2f} seconds the object is at ({x_050:.3f}, {y_050:.3f}, {z_050:.3f})")

x_075 = x1 + vx * step * 3
y_075 = y1 + vy * step * 3
z_075 = z1 + vz * step * 3
print(f"At time {t1+step*3:.2f} seconds the object is at ({x_075:.3f}, {y_075:.3f}, {z_075:.3f})")

print(f"At time {t2:.2f} seconds the object is at ({x2:.3f}, {y2:.3f}, {z2:.3f})")

