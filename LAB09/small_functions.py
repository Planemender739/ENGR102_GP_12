# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Thomas Tang
# Section: 511
# Assignment: 
# Date: October 20th, 2025

def parta(list):
    max = -float('inf')
    min = float('inf')
    median = 0
    for num in list:
        if num > max:
            max = num
        if num < min:
            min = num
    # sort to find median
    sorted_list = sorted(list)
    n = len(sorted_list)
    if n % 2 == 1:
        median = sorted_list[n // 2]
    else:
        median = (sorted_list[n // 2 - 1] + sorted_list[n // 2]) / 2
    return (min, median, max)

def partb(times, distances):
    out = []
    for i in range(len(times) - 1):
        # calculate vel
        out += [(distances[i + 1] - distances[i]) / (times[i + 1] - times[i])]
    return out

def partc(list):
    seen = set() # work in complements

    for num in list:
        if (2029 - num) in seen:
            return num * (2029 - num)
        seen.add(num)
        
    return False

from math import pi

def partd(n):
    for i in range(2, n): # length of at least 2
        num = n - i * (i - 1)
        den = 2 * i
        
        if num <= 0:
            break
        
        if num % den == 0:
            start = num // den
            if start >= 1:
                seq = [2 * (start + i) for i in range(i)]
                return seq

    return False
        

def parte(sr, hr):
    # formula from integration
    h = 2.0 * (sr ** 2 - hr ** 2) ** 0.5
    return (pi * (h ** 3)) / 6.0

def partf(char, name, company, email):
    # find longest to pad
    longest = max(len(char), len(name), len(company), len(email))
    return char * (longest + 6) + f"\n{char}  {name:^{longest}}  {char}" + f"\n{char}  {company:^{longest}}  {char}" + f"\n{char}  {email:^{longest}}  {char}" + f"\n" + char * (longest + 6)

def partg(x, tolerance):
    summation = 0.0
    n = 1

    while True:
        # calc
        term = (2 / (2 * n - 1)) * (x ** (2 * n - 1))
        if abs(term) < tolerance:
            break
        summation += term
        n += 1

    return summation
