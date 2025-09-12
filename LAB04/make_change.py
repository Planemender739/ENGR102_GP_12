# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Thomas Tang
# Section: 511
# Assignment: Lab 04
# Date: September 12th, 2025

print("How much did you pay? ", end="")

cost = float(input())

print("How much did it cost? ", end="")

tendered = float(input())

print(f"You received ${cost - tendered:.2f} in change. That is...")

change = (100 * cost) - (100 * tendered) # convert to cents

quarters = int(change // 25)
change = change - (quarters * 25)
dimes = int(change // 10)
change = change - (dimes * 10)
nickels = int(change // 5)
change = change - (nickels * 5)
pennies = int(change // 1)
change = change - (pennies * 1)

if quarters:
    print(f"{quarters} quarter{'' if quarters == 1 else 's'}")
if dimes:
    print(f"{dimes} dime{'' if dimes == 1 else 's'}")
if nickels:
    print(f"{nickels} nickel{'' if nickels == 1 else 's'}")
if pennies:
    print(f"{pennies} penn{'y' if pennies == 1 else 'ies'}")