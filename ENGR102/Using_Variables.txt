# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Lane Mack
# Section: Engr 102-511
# Assignment: Lab Topic 2 individual
# Date: 30 August 2025
#
#using_variables
#
#
#
#
#
#REYNOLDS

#Reynolds Number , Defined by 'Re'= (Fluid Velocity * Linear Dimension)/ Kinematic Viscosity

u=9 #Where 'u'' is the Fluid velocity, with units in m/s
v=0.0015 #Where 'v' is the Kinematic Viscosity with units in m^2/s
L=.875 #And where 'L' is the linear dimension

Re=(u*L)/v    #This will be the quick equation we use to calculate the Reynold's number,
                #Then we will assign it to the "Re" name
print("Reynolds number is",Re,)    #This will print the Reynold's number. And there are no units on the Reynold's number.




#X-RAY SCATTERING
from math import *  

#Since we are using sin and pi in this equation and future equations, we want to make sure
#to import all the math tools that we will use. It is done by the "from math import *"" line

n=1 #Where n is the order of diffraction, which was given to us to be 1
d=0.029  #Where d is the distance between crystal lattice layers measured in nm
theta=((35/180)*pi) #Here, we are converting the previous degree measurement into radians, and defining it as theta.

nλ=2*d*sin(theta) #This will be the quick equation we use to calculate the wavelength in nm
print("Wavelength is",nλ,"nm") #This will print the length of the waves and some phrasing to make it understandable including units.


#ARPS EQUATION
#This will be used to forecast the future production of oil and gas wells.

#q is the rate at which barrels of oil will be produced at any given day.
qi= 100 #This is the initial rate of oil production measured in barrels per day
Di= 2  #This is the rate of decline of oil production measured in barrels per day
t=10  #t is in reference to time, measured in days. We are calculating for 10 days after initial measurement, so 10 is correct.
b=0.8 #b is the hyperbolic constant

q = (qi)/ ((1+b*Di*t)**(1/b))   #This is the quick equation we use to find the production rate at day t
print('Production rate is', q,'barrels/day')


#TSIOLKOVSKY ROCKET EQUATION
#This describes the motion of a device that can apply acceleration to itself 
#by expelling part of its mass at high velocity.

import math  #Initally, sometimes the "from math import *" tool doesn't always work ,so we have to try another way

#Next, lets define the variables.

v=2029 #Where v is the exhaust velocity, measured in m/s
Mo=11000 #Where Mo is the initial mass of the aircraft measured in kg
Mf=8300 #where Mf is the final mass of the aircraft measured in kg
#DeltaV is going to be the change in the velocity.


deltaV=v*(math.log(Mo/Mf)) #This will be the quick equation we use to find the velocity based on initial and final masses,and exhaust velocity

print('Change of velocity is', deltaV, "m/s")  #This prints a quick message with delta V, and some simple english to explain, not just a number
#
#
#
#
#


