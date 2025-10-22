# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Thomas Tang
# Section: 511
# Assignment: 
# Date: October 21st, 2025

# 5 lines
for row in range(5): 
    line = ""
    for c in output:
        if char not in "abcdeghkmnopqrsuvwxyz@$&*=" or char == "" :
            char = str(c)
        else:
            char = char
        line += chars[c][row].replace("#", char) + " "
    if ampm:
        line += ampm[row]
    else:
        line = line[:-1]

    print(line)