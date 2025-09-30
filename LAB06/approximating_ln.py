# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Thomas Tang
# Section: 511
# Assignment: Lab 06
# Date: September 29th, 2025

import math

def main():
    x = float(input("Enter a value for x: "))
    while x <= 0 or x > 2:
        x = float(input("Out of range! Try again: "))
    
    tol = float(input("Enter the tolerance: "))

    n = 1
    term = (x - 1)
    approx = 0.0

    # series    
    while abs(term) >= tol:
        approx += term
        n += 1
        term = ((-1) ** (n+1)) * ((x - 1) ** n) / n

    exact = math.log(x)

    print(f"ln({x}) is approximately {approx}")
    print(f"ln({x}) is exactly {exact}")
    print(f"The difference is {abs(approx - exact)}")

if __name__ == "__main__":
    main()
