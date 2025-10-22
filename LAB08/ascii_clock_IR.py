
# Ask the user for their preferred character
preferred_char = input("Enter your preferred character: ")
while preferred_char not in "abcdeghkmnopqrsuvwxyz@$&*=":
    preferred_char = input("Character not permitted! Try again: ")

print()

to_print = adjusted_time