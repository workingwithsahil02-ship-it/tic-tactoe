import random

wins = [
    (0, 1, 2), (3, 4, 5), (6, 7, 8), 
    (0, 3, 6), (1, 4, 7), (2, 5, 8), 
    (0, 4, 8), (2, 4, 6)
]

def print_board(board):
    print(f"\n{board[0]} | {board[1]} | {board[2]}")
    print("---+---+---")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("---+---+---")
    print(f"{board[6]} | {board[7]} | {board[8]}\n")

def check(board, player):
    for a, b, c in wins:
        if board[a] == board[b] == board[c] == player:
            return True
    return False

def get_player_move(board, name, symbol):
    while True:
        move = input(f"{name} ({symbol}) pick a spot (1-9): ").strip()
        if not move.isdigit():
            print("Numbers only from 1 to 9.")
            continue
        
        idx = int(move) - 1
        
        if idx < 0 or idx > 8:
            print("Number must be between 1 and 9.")
            continue
            
        if board[idx] in ("X", "O"):
            print("Already taken.")
            continue
            
        return idx

def main():
    board = [str(i) for i in range(1, 10)]
    print("Tic-Tac-Toe")
    mode = ""
    
    while mode not in ("1", "2"):
        mode = input("1. Play against a friend \n2. Play against the computer \nMode (1 or 2): ").strip()

    p1 = input("Player 1 name (X): ").strip()
    if not p1:
        p1 = "Player 1"

    if mode == "1":
        p2 = input("Player 2 name (O): ").strip()
        if not p2:
            p2 = "Player 2"
        vs_cpu = False
    else:
        p2 = "Computer"
        vs_cpu = True

    players = {"X": p1, "O": p2}
    current = "X"
    turns = 0

    while turns < 9:
        print_board(board)
        
        if current == "O" and vs_cpu:
            print("Computer is thinking...")
            open_spots = [i for i, v in enumerate(board) if v not in ("X", "O")]
            move = random.choice(open_spots)
        else:
            move = get_player_move(board, players[current], current)

        board[move] = current
        turns += 1

        if check(board, current):
            print_board(board)
            print(f"{players[current]} wins!")
            return

        current = "O" if current == "X" else "X"

    print_board(board)
    print("It's a tie!")

if __name__ == "__main__":
    main()