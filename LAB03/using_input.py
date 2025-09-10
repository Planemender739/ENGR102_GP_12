# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Thomas Tang
# Section: 511
# Assignment: Lab 03
# Date: September 9th, 2025

from math import *

# Reynolds number calculation
print("This program calculates the Reynolds number given velocity, length, and viscosity")
velocity = float(input("Please enter the velocity (m/s): "))
characteristic_length = float(input("Please enter the length (m): "))
kinematic_viscosity = float(input("Please enter the viscosity (m^2/s): "))
reynolds_number = int((velocity * characteristic_length) / kinematic_viscosity)
print(f"Reynolds number is {reynolds_number:.0f}")

# Wavelength calculation
print("\nThis program calculates the wavelength given distance and angle")
layer_distance = float(input("Please enter the distance (nm): "))
scattering_angle = float(input("Please enter the angle (degrees): "))
wavelength = 2 * layer_distance * sin(scattering_angle * (pi / 180))
print(f"Wavelength is {wavelength:.4f} nm")

# Production rate calculation
print("\nThis program calculates the production rate given initial rate, decline, and days")
days = float(input("Please enter the number of days: "))
initial_rate = float(input("Please enter the initial rate (/day): "))
initial_decline = float(input("Please enter the initial decline (/day): "))
hyperbolic_constant = float(input("Please enter the hyperbolic constant: "))
production_rate = initial_rate / (1 + hyperbolic_constant * initial_decline * days) ** (1 / hyperbolic_constant)
print(f"Production rate is {production_rate:.2f} barrels/day")

# Rocket velocity change calculation
print("\nThis program calculates the change of velocity given initial mass, final mass, and exhaust velocity")
initial_mass = float(input("Please enter the initial mass (kg): "))
final_mass = float(input("Please enter the final mass (kg): "))
exhaust_velocity = float(input("Please enter the exhaust velocity (m/s): "))
delta_v = exhaust_velocity * log(initial_mass / final_mass)
print(f"Change of velocity is {delta_v:.2f} m/s")
