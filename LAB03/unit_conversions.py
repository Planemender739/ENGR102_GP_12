# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Thomas Tang
# Section: 511
# Assignment: Lab 03
# Date: September 9th, 2025

"""
Please enter the quantity to be converted: 1
1.00 pounds force is equivalent to 4.45 newtons
1.00 meters is equivalent to 3.28 feet
1.00 atmospheres is equivalent to 101.33 kilopascals
1.00 watts is equivalent to 3.41 BTU per hour
1.00 liters per second is equivalent to 15.85 US gallons per minute
1.00 degrees Celsius is equivalent to 33.80 degrees Fahrenheit
"""

# get input
qty = float(input("Please enter the quantity to be converted: "))

N = qty * 4.44822
ft = qty * 3.28084
kP = qty * 101.325
btuph = qty * 3.41214163
galpm = qty * 15.850323140625
fahrenheit = (qty * 9 / 5) + 32

print(f"{qty:.2f} pounds force is equivalent to {N:.2f} newtons")
print(f"{qty:.2f} meters is equivalent to {ft:.2f} feet")
print(f"{qty:.2f} atmospheres is equivalent to {kP:.2f} kilopascals")
print(f"{qty:.2f} watts is equivalent to {btuph:.2f} BTU per hour")
print(f"{qty:.2f} liters per second is equivalent to {galpm:.2f} US gallons per minute")
print(f"{qty:.2f} degrees Celsius is equivalent to {fahrenheit:.2f} degrees Fahrenheit")
