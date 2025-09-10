# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Lane Mack
# Section: Engr 102-511
# Assignment: Lab Topic 2 (Individual)
# Date: 30 August 2025
#


from math import *    #Importing the math functions, should we need to use them
import math
init_time=12         #Defining some of the positions of X,Y, and Z.
init_posX=8          #Init meaning initial
init_posY=6
init_posZ=7
fin_posX=-5          #Fin being final
fin_posY=30
fin_posZ=9
fin_time=85


print("At time 30.0 seconds:")
Slope_x=((fin_posX-init_posX)/(fin_time-init_time))      #Slope= (X2-X1)/(T2-T1), The three slope functions are identical, but they just use the new values
Pos_x=(init_posX+((30-init_time)*Slope_x))               #the position of X at time t is the intial position +(30-18 (where 18 was the initial time multiplied by the slope of X)
print("x1 =",Pos_x, "m")       #Print X1 and the units

Slope_y=((fin_posY-init_posY)/(fin_time-init_time))
Pos_y=(init_posY+((30-init_time)*Slope_y))
print("y1 =",Pos_y, "m")

Slope_z=((fin_posZ-init_posZ)/(fin_time-init_time))
Pos_z=(init_posZ+((30-init_time)*Slope_z))
print("z1 =",Pos_z, "m")
print("-----------------------")

print("At time 37.5 seconds:")

Slope_x=((fin_posX-init_posX)/(fin_time-init_time))      #Slope= (X2-X1)/(T2-T1), The three slope functions are identical, but they just use the new values
Pos_x=(init_posX+((37.5-init_time)*Slope_x))               #the position of X at time t is the intial position +(t-18 (where 18 was the initial time multiplied by the slope of X)
print("x2 =",Pos_x, "m")       #Print X1 and the units

Slope_y=((fin_posY-init_posY)/(fin_time-init_time))
Pos_y=(init_posY+((37.5-init_time)*Slope_y))
print("y2 =",Pos_y, "m")

Slope_z=((fin_posZ-init_posZ)/(fin_time-init_time))
Pos_z=(init_posZ+((37.5-init_time)*Slope_z))
print("z2 =",Pos_z, "m")

print("-----------------------")

print("At time 45.0 seconds:")
Slope_x=((fin_posX-init_posX)/(fin_time-init_time))      #Slope= (X2-X1)/(T2-T1), The three slope functions are identical, but they just use the new values
Pos_x=(init_posX+((45-init_time)*Slope_x))               #the position of X at time t is the intial position +(t-18 (where 18 was the initial time multiplied by the slope of X)
print("x3 =",Pos_x, "m")       #Print X1 and the units

Slope_y=((fin_posY-init_posY)/(fin_time-init_time))
Pos_y=(init_posY+((45-init_time)*Slope_y))
print("y3 =",Pos_y, "m")

Slope_z=((fin_posZ-init_posZ)/(fin_time-init_time))
Pos_z=(init_posZ+((45-init_time)*Slope_z))
print("z3 =",Pos_z, "m")

print("-----------------------")

print("At time 52.5 seconds:")

Slope_x=((fin_posX-init_posX)/(fin_time-init_time))      #Slope= (X2-X1)/(T2-T1), The three slope functions are identical, but they just use the new values
Pos_x=(init_posX+((52.5-init_time)*Slope_x))               #the position of X at time t is the intial position +(t-18 (where 18 was the initial time multiplied by the slope of X)
print("x4 =",Pos_x, "m")       #Print X1 and the units

Slope_y=((fin_posY-init_posY)/(fin_time-init_time))
Pos_y=(init_posY+((52.5-init_time)*Slope_y))
print("y4 =",Pos_y, "m")

Slope_z=((fin_posZ-init_posZ)/(fin_time-init_time))
Pos_z=(init_posZ+((52.5-init_time)*Slope_z))
print("z4 =",Pos_z, "m")

print("-----------------------")

print("At time 60.0 seconds:")

Slope_x=((fin_posX-init_posX)/(fin_time-init_time))      #Slope= (X2-X1)/(T2-T1), The three slope functions are identical, but they just use the new values
Pos_x=(init_posX+((60-init_time)*Slope_x))               #the position of X at time t is the intial position +(t-18 (where 18 was the initial time multiplied by the slope of X)
print("x5 =",Pos_x, "m")       #Print X1 and the units

Slope_y=((fin_posY-init_posY)/(fin_time-init_time))
Pos_y=(init_posY+((60-init_time)*Slope_y))
print("y5 =",Pos_y, "m")

Slope_z=((fin_posZ-init_posZ)/(fin_time-init_time))
Pos_z=(init_posZ+((60-init_time)*Slope_z))
print("z5 =",Pos_z, "m")