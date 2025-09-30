# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Thomas Tang
# Section: 511
# Assignment: Lab 06
# Date: September 29th, 2025

n = int(input("Enter a value for n: "))

sum1 = 0
for i in range(1, n + 1):
    sum1 += i

# find mid
sum2 = 0
r = 1
while sum2 < sum1:
    sum2 += n + r
    if sum2 == sum1:
        print(f"{n} is a co-balancing number with r={r}")
        exit()
    r += 1

print(f"{n} is not a co-balancing number")