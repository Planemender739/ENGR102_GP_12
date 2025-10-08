# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Thomas Tang
# Section: 511
# Assignment: Lab 07
# Date: October 5th, 2025

name = input("What is your name? ")

vowels = "AEIOUYaeiouy"

# Find the index of the first vowel
first_vowel_index = 0
for i, char in enumerate(name):
    if char in vowels:
        first_vowel_index = i
        break

# Determine Y
if first_vowel_index == 0:
    # Name starts with a vowel: Y is full name in lowercase
    Y = name.lower()
else:
    # Name starts with consonant(s): drop initial consonant cluster
    Y = name[first_vowel_index:]

# Print Name Game rhyme
print(f"{name}, {name}, Bo-B{Y}")
print(f"Banana-Fana Fo-F{Y}")
print(f"Me Mi Mo-M{Y}")
print(f"{name}!")