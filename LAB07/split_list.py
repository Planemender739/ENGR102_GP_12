# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Thomas Tang
# Section: 511
# Assignment: Lab 07
# Date: October 5th, 2025

numbers_input = input("Enter numbers: ")
numbers_str = numbers_input.split()
numbers = []
for token in numbers_str:
    numbers.append(int(token))

# Initialize 
split_found = False
total_numbers = len(numbers)

for split_index in range(1, total_numbers):
    left_sum = 0
    right_sum = 0

    for i in range(split_index):
        left_sum += numbers[i]

    for i in range(split_index, total_numbers):
        right_sum += numbers[i]

    # split if left = right
    if left_sum == right_sum:
        print(f"Left: {numbers[:split_index]}")
        print(f"Right: {numbers[split_index:]}")
        print(f"Both sum to {left_sum}")
        split_found = True
        break

if not split_found:
    print("Cannot split evenly")