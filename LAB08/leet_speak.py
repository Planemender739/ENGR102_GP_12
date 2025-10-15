# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Thomas Tang
# Section: 511
# Assignment: Leet Speak
# Date: October 15th, 2025

"""
Enter some text: howdy aggies whoop
In leet speak, "howdy aggies whoop" is:
h0wdy 4ggi35 wh00p
"""

# store conversions
d = {
    "a": "4",
    "e": "3",
    "o": "0",
    "s": "5",
    "t": "7",
}

print("Enter some text: ", end="")

s = input()

print(f"In leet speak, \"{s}\" is:")

for c in s:
    if c in d:
        print(d[c], end="")
    else:
        print(c, end="")
print()
