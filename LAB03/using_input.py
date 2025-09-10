# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Thomas Tnag
# Section: 511
# Assignment: Lab 03
# Date: September 9th, 2025


#REYNOLDS

#Reynolds Number , Defined by 'Re'= (Fluid Velocity * Linear Dimension)/ Kinematic Viscosity
print("This program calculates the Reynolds number given velocity, length, and viscosity")
u=float(input("Please enter the velocity (m/s): "))          #Where 'u'' is the Fluid velocity, with units in m/s

L=float(input("Please enter the length (m): "))          #And where 'L' is the linear dimension in meters

v=float(input("Please enter the viscosity (m^2/s): "))   #Where 'v' is the Kinematic Viscosity with units in m^2/s

Re=(u*L)/v    #This will be the quick equation we use to calculate the Reynold's number,
                #Then we will assign it to the "Re" name
print(f"Reynolds number is {Re:.0f}")    #This will print the Reynold's number. And there are no units on the Reynold's number.
print()

#--------------------------------------------------------------

#X-RAY SCATTERING
from math import *  

#Since we are using sin and pi in this equation and future equations, we want to make sure
#to import all the math tools that we will use. It is done by the "from math import *"" line
print("This program calculates the wavelength given distance and angle")

d=float(input("Please enter the distance (nm): "))          #Where d is the distance between crystal lattice layers measured in nm

theta=float(input("Please enter the angle (degrees): "))

theta=(theta/180)*pi 

#theta=((35/180)*pi) #Here, we are converting the previous degree measurement into radians, and defining it as theta.

nλ=2*d*sin(theta) #This will be the quick equation we use to calculate the wavelength in nm
print(f"Wavelength is {nλ:.4f} nm") #This will print the length of the waves and some phrasing to make it understandable including units.
print()
#---------------------------------------------------------------------


#ARPS EQUATION
#This will be used to forecast the future production of oil and gas wells.

#q is the rate at which barrels of oil will be produced at any given day.
print("This program calculates the production rate given time, initial rate, and decline rate")

t=float(input("Please enter the time (days): "))    #t is in reference to time, measured in days.

qi=float(input("Please enter the initial rate (barrels/day): "))       #This is the initial rate of oil production measured in barrels per day   

Di=float(input("Please enter the decline rate (1/day): "))          #This is the rate of decline of oil production measured in barrels per day         

b=0.8 #b is the hyperbolic constant

q = (qi)/ ((1+b*Di*t)**(1/b))   #This is the quick equation we use to find the production rate at day t

print(f'Production rate is {q:.2f} barrels/day')

print()
#----------------------------------------------------------------------------------

#TSIOLKOVSKY ROCKET EQUATION
#This describes the motion of a device that can apply acceleration to itself 
#by expelling part of its mass at high velocity.

import math  #Initally, sometimes the "from math import *" tool doesn't always work ,so we have to try another way

#Next, lets define the variables.
print("This program calculates the change of velocity given initial mass, final mass, and exhaust velocity")


Mo=float(input("Please enter the initial mass (kg): "))    #Where Mo is the initial mass of the aircraft measured in Kg           

Mf=float(input("Please enter the final mass (kg): "))        #where Mf is the final mass of the aircraft measured in kg

v=float(input("Please enter the exhaust velocity (m/s): "))       #Where v is the exhaust velocity, measured in m/s  
#DeltaV is going to be the change in the velocity.

deltaV=v*(math.log(Mo/Mf)) #This will be the quick equation we use to find the velocity based on initial and final masses,and exhaust velocity

print(f'Change of velocity is {deltaV:.1f} m/s')  #This prints a quick message with delta V, and some simple english to explain, not just a number



