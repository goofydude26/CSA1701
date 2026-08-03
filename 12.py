board = [' ' for _ in range(9)]

def display_board():
    print()
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")
    print()

def check_winner(player):
    win_positions = [
        (0,1,2), (3,4,5), (6,7,8),
        (0,3,6), (1,4,7), (2,5,8),
        (0,4,8), (2,4,6)
    ]

    for a, b, c in win_positions:
        if board[a] == board[b] == board[c] == player:
            return True
    return False

def is_draw():
    return ' ' not in board

current_player = 'X'

while True:
    display_board()

    move = int(input(f"Player {current_player}, enter position (1-9): ")) - 1

    if board[move] != ' ':
        print("Position already occupied!")
        continue

    board[move] = current_player

    if check_winner(current_player):
        display_board()
        print(f"Player {current_player} wins!")
        break

    if is_draw():
        display_board()
        print("It's a draw!")
        break

    current_player = 'O' if current_player == 'X' else 'X'