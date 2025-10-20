# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Thomas Tang
# Section: 511
# Assignment: 
# Date: October 19th, 2025

def print_puzzle(puzzle):
    ''' Print puzzle as a long division problem. '''
    puzzle = puzzle.split(',')
    for i in range(len(puzzle)):
        if i == 1:
            print(f'{len(puzzle[i].split("|")[1]) * "_": >16}')
        print(f'{puzzle[i]: >16}')
        if i > 1 and i % 2 == 0:
            print(f"{'-'*len(puzzle[i]): >16}")

def get_valid_letters(s):
    out = ""
    for c in s:
        if c.isalpha() and c not in out:
            out += c
    return out

def is_valid_guess(v, s):
    if len(v) != len(s):
        return False
    for i in range(len(v)):
        if not v[i] in s:
            return False
    return True

def check_user_guess(dividend, quotient, divisor, remainder):
    return dividend == quotient * divisor + remainder

def make_number(word, guess):
    i = 0
    for c in word:
        i *= 10
        i += guess.index(c)
    return i

def make_numbers(puzzle, guess):
    one = puzzle.split(",")[0].strip()
    two = puzzle.split(",")[1].split("|")[0].strip()
    three = puzzle.split(",")[1].split("|")[1].strip()
    four = puzzle.split(",")[-1].strip()

    return (make_number(three, guess),
            make_number(one, guess),
            make_number(two, guess),
            make_number(four, guess))

def main():
    # Read puzzle string from the user (prompt on its own line as in examples)
    puzzle = input("Enter a word arithmetic puzzle: \n")

    print_puzzle(puzzle)

    print()

    # Determine the set of valid letters from the puzzle
    valid = get_valid_letters(puzzle)

    # Prompt the user for a single guess (example text must match)
    guess = input("Enter your guess, for example ABCDEFGHIJ: ")

    # If the guess isn't valid, show the specified multi-line message
    if not is_valid_guess(guess, valid):
        print(f"Your guess should contain exactly {len(valid)} unique letters used in the puzzle.")
        return

    # Convert puzzle words into numbers and check the arithmetic
    dividend, quotient, divisor, remainder = make_numbers(puzzle, guess)

    if check_user_guess(dividend, quotient, divisor, remainder):
        print("Good job!")
    else:
        print("Try again!")

if __name__ == '__main__':
    main()
