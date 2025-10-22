DIGITS = {
    '0': [
        "###",
        "# #",
        "# #",
        "# #",
        "###"
    ],
    '1': [
        " # ",
        "## ",
        " # ",
        " # ",
        "###"
    ],
    '2': [
        "###",
        "  #",
        "###",
        "#  ",
        "###"
    ],
    '3': [
        "###",
        "  #",
        "###",
        "  #",
        "###"
    ],
    '4': [
        "# #",
        "# #",
        "###",
        "  #",
        "  #"
    ],
    '5': [
        "###",
        "#  ",
        "###",
        "  #",
        "###"
    ],
    '6': [
        "###",
        "#  ",
        "###",
        "# #",
        "###"
    ],
    '7': [
        "###",
        "  #",
        "  #",
        "  #",
        "  #"
    ],
    '8': [
        "###",
        "# #",
        "###",
        "# #",
        "###"
    ],
    '9': [
        "###",
        "# #",
        "###",
        "  #",
        "###"
    ],
    ':': [
        " ",
        ":",
        " ",
        ":",
        " "
    ],
    'AM': [
        " A  M   M",
        "A A MM MM",
        "AAA M M M",
        "A A M   M",
        "A A M   M"
    ],
    'PM': [
        "PPP M   M",
        "P P MM MM",
        "PPP M M M",
        "P   M   M",
        "P   M   M"
    ],
    ' ': [    # for spacing between time and AM/PM
        "   ",
        "   ",
        "   ",
        "   ",
        "   "
    ]
}

# Ask the user to enter the time
entered_time = input("Enter the time: ")
time_list = entered_time.split(":")
hour = int(time_list[0])
minutes = time_list[1]

# Ask the user for the clock type (12 or 24)
clock_type = input("Choose the clock type (12 or 24): ")