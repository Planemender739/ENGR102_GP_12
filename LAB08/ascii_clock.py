# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Thomas Tang
# Section: 511
# Assignment: 
# Date: October 15th, 2025

chars = {
    "0": [
        "000",
        "0 0",
        "0 0",
        "0 0",
        "000",
    ],
    "1": [
        "  1",
        "  1",
        "  1",
        "  1",
        "  1",
    ],
    "2": [
        "222",
        "  2",
        "222",
        "2  ",
        "222",
    ],
    "3": [
        "333",
        "  3",
        "333",
        "  3",
        "333",
    ],
    "4": [
        "4 4",
        "4 4",
        "444",
        "  4",
        "  4",
    ],
    "5": [
        "555",
        "5  ",
        "555",
        "  5",
        "555",
    ],
    "6": [
        "666",
        "6  ",
        "666",
        "6 6",
        "666",
    ],
    "7": [
        "777",
        "  7",
        "  7",
        "  7",
        "  7",
    ],
    "8": [
        "888",
        "8 8",
        "888",
        "8 8",
        "888",
    ],
    "9": [
        "999",
        "9 9",
        "999",
        "  9",
        "999",
    ],
    "a": [
        " # ",
        "# #",
        "###",
        "# #",
        "# #",
    ],
    "p": [
        "###",
        "# #",
        "###",
        "#  ",
        "#  ",
    ],
    "m": [
        "#   #",
        "## ##",
        "# # #",
        "#   #",
        "#   #",
    ],
    ":": [
        "   ",
        " # ",
        "   ",
        " # ",
        "   ",
    ]
}

print("Enter the time: ", end="")

time = input().strip()

print("Choose the clock type (12 or 24): ", end="")

clock_type = int(input().strip())

print("Enter your preferred character: ", end="")

char = input().strip()[0]

while (char != "" and not char in "abcdeghkmnopqrsuvwxyz@$&*="):
    print("Character not permitted! Try again: ", end="")
    char = input().strip()[0]

ampm = ""

if clock_type == 12:
    hours, minutes = map(int, time.split(":"))
    if hours == 0:
        hours = 12
        ampm = "am"
    elif hours > 12:
        hours -= 12
        ampm = "pm"
    time = f"{hours}:{minutes:02}"

print()

grid = [[], [], [], [], []]

for c in time + ampm:
    if c in chars:
        char_grid = chars[c]
        for i in range(5):
            grid[i] += char_grid[i]
            grid[i] += [" "]  # space between characters

for row in grid:
    for i in range(len(row[0])):
        for c in row:
            print(c[i].replace("#", char), end="")
        print()
