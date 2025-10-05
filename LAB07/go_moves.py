# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Thomas Tang
# Section: 511
# Assignment: Lab 07
# Date: October 5th, 2025

# Initialize empty board
BOARD_SIZE = 9 #  can change this later
board = [["." for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]

def display_board():
    print("   " + " ".join([chr(ord("A") + i) for i in range(BOARD_SIZE)]))
    for row in range(BOARD_SIZE):
        print(f"{row+1:2} " + " ".join(board[row]))
    print()

def parse_move(move):
    if len(move) < 2:
        return None
    col = move[0].upper()
    if not ("A" <= col <= "I"):
        return None
    try:
        row = int(move[1:])
    except ValueError:
        return None
    if 1 <= row <= BOARD_SIZE:
        return row - 1, ord(col) - ord("A")
    return None

current_player = "B" 
while True:
    display_board()
    move = input(f"Player {current_player}, enter your move (e.g. C5) or 'stop': ").strip()
    if move.lower() == "stop":
        print("Game stopped.")
        break
    coords = parse_move(move)
    if coords is None:
        print("Invalid input. Please use format like C5.")
        continue
    r, c = coords
    if board[r][c] != ".":
        print("That spot is already occupied! Try again.")
        continue
    board[r][c] = current_player
    # Switch players
    current_player = "W" if current_player == "B" else "B"

