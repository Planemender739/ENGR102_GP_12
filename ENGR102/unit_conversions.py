# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Names: Lane Mack
# Ashi Talluri
# Thomas Tang
#
# Section: 511
# Assignment: Lab 3 team
# Date: 6 Sept 2025
#
#
# unit_conversions.py
#
#---------------------------------------------

quantity_tbc=(float(input("Please enter the quantity to be converted: ")))   #Asking for what value we want to conver with, Where quantity_TBC is the quantity to be converted

#This gives us the conversion for pounds --> Newtons
    #We use the f"{quantity_tbc:.2f}" command to make sure that we use 1.00 instead of 1.0 or 1.
    #This is the case for all the functions below

newtons=(quantity_tbc*4.4482216153)
print((f"{quantity_tbc:.2f}"), "pounds force is equivalent to",(f"{newtons:.2f}"),"newtons")

#----------------------------------------------
#This gives us the covnersion for meters --> Feet

feet=(quantity_tbc*3.28084)
print((f"{quantity_tbc:.2f}"), "meters is equivalent to",(f"{feet:.2f}"),"feet")

#-----------------------------------------------
#This gives us the conversion for atmospheres --> Kilopascals

kilopascals=(quantity_tbc*101.325)
print((f"{quantity_tbc:.2f}"),"atmospheres is equivalent to",(f"{kilopascals:.2f}"),"kilopascals")

#----------------------------------------------
#This gives us the conversion for Watts --> BTU

BTU_per_hour=(quantity_tbc*3.41214163)
print((f"{quantity_tbc:.2f}"),"watts is equivalent to",(f"{BTU_per_hour:.2f}"),"BTU per hour")

#----------------------------------------------
#This gives us the conversion for Liters -->US Gallons per Minute

US_GPM=(quantity_tbc*15.85033)
print((f"{quantity_tbc:.2f}"),"liters per second is equivalent to",(f"{US_GPM:.2f}"),"US gallons per minute")

#-----------------------------------------------
#This gives us the conversion for Degrees C --> Degrees Fahrenheit

Deg_Fahr=(float((9/5)*quantity_tbc)+32)
print((f"{quantity_tbc:.2f}"),"degrees Celsius is equivalent to",(f"{Deg_Fahr:.2f}"),"degrees Fahrenheit")