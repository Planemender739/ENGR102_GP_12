# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Thomas Tang
# Section: 511
# Assignment: Lab 04
# Date: September 12th, 2025

############ Part A ############ 

print("Enter True or False for a: ", end="")
a = input().lower()[0] == 't'
print("Enter True or False for b: ", end="")
b = input().lower()[0] == 't'
print("Enter True or False for c: ", end="")
c = input().lower()[0] == 't'

############ Part B ############ 

print(f"a and b and c: {a and b and c}")
print(f"a or b or c: {a or b or c}")

############ Part C ############ 

print(f"XOR: {(not (a and b)) and (a or b)}")
print(f"Odd number: {(a and not b and not c) or (not a and not b and c) or (b and not a and not c) or (b and a and c)}")

"""
Enter True or False for a: T
Enter True or False for b: T
Enter True or False for c: T
a and b and c: True
a or b or c: True
XOR: False
Odd number: True
"""

############ Part D ############ 

# reduce with de morgans laws

print("Complex 1:", (not (a and not b) or (not c and b)) and (not b) or (not a and b and not c) or (a and not b))
print("Simple 1:",  (not a and b and not c) or not b)

print("Complex 2:", (not ((b or not c) and (not a or not c))) or (not (c or not (b and c))) or (a and not c) and (not a or (a and b and c) or (a and ((b and not c) or (not b)))))
print("Simple 2:",  a or ((not b) and c))