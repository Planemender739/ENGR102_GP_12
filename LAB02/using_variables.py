# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Thomas Tang
# Section: 511
# Assignment: Lab 02
# Date: September 3rd, 2025

from math import *

velocity = 9.0 # m/s
kinematic_viscosity = 0.0015 # m^2/s
characteristic_length = 0.875 # m

print("Reynolds number is", (velocity * characteristic_length) / kinematic_viscosity)

layer_distance = 0.029 # nm
scattering_angle = 35 # degrees

print("Wavelength is", 2 * layer_distance * sin(scattering_angle * (pi / 180)), "nm") # converting degrees to radians

days = 10
initial_rate = 100 # /day
initial_decline = 2 # /day
hyperbolic_constant = 0.8

print("Production rate is", initial_rate / (1 + hyperbolic_constant * initial_decline * days) ** (1 / hyperbolic_constant), "barrels/day")

initial_mass = 11000 # kg
final_mass = 8300 # kg
exhaust_velocity = 2029 # m/s

print("Change of velocity is", exhaust_velocity * log(initial_mass / final_mass), "m/s")