# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Thomas Tang
# Section: 511
# Assignment: Lab 07
# Date: October 5th, 2025

num = int(input("Enter a four-digit integer: "))

sequence = [num]

iterations = 0
current = num

while current != 6174:
    num_str = f"{current:04d}"
    
    digits = list(num_str)
    digits.sort()
    small_num = int("".join(digits))
    digits.sort(reverse=True)
    large_num = int("".join(digits))
    
    next_num = large_num - small_num
    current = next_num
    sequence.append(current)
    iterations += 1
    
    if current == 0:
        break

# print sequence without extra leading zeros
print(" > ".join(str(x) for x in sequence))

if current == 6174:
    print(f"{sequence[0]} reaches 6174 via Kaprekar's routine in {iterations} iterations")
elif current == 0:
    print(f"{sequence[0]} reaches 0 via Kaprekar's routine in {iterations} iterations")
