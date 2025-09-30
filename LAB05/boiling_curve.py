# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Thomas Tang
# Section: ENGR 102 511
# Assignment: Lab Topic 5 Individual
# Date: September 22nd, 2025

from math import *

# get input
excess_temp = float(input("Enter the excess temperature: "))

# determine the range
if 1.3 <= excess_temp < 5:
    X0 = 1.3
    X1 = 5.0
    Y0 = 1000
    Y1 = 7000
elif 5 <= excess_temp < 30:
    X0 = 5.0
    X1 = 30.0
    Y0 = 7000
    Y1 = 1500000
elif 30 <= excess_temp < 120:
    X0 = 30
    X1 = 120
    Y0 = 1500000
    Y1 = 25000
elif 120 <= excess_temp <= 1200:
    X0 = 120
    X1 = 1200
    Y0 = 25000
    Y1 = 1500000
else: # out of range
    print("Surface heat flux is not available")
    exit()


# linear reg
m = (log(Y1 / Y0)) / log(X1 / X0)

# calculate y
y = Y0 * (excess_temp / X0) ** m

# output
print(f"The surface heat flux is approximately {y:.0f} W/m^2")


#
#
#
##
#
#
####
#
#
#
###
