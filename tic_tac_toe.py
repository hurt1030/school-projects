# Matthew Hurt
# CSC 540 - Intro to Artificial Intelligence
# Use minimax to create an AI that never loses at tic-tac-toe

import math

def print_board(board):
    print(f"\n  {board[0][0]}  |  {board[0][1]}  |  {board[0][2]}  \
    \n_________________\n\n  {board[1][0]}  |  {board[1][1]}  |  {board[1][2]}  \
    \n_________________\n\n  {board[2][0]}  |  {board[2][1]}  |  {board[2][2]}\n")

def is_win(board, turn):
    # Check rows
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] == turn:
            return True
    
    #check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] == turn:
            return True

    #check diagonals
    if board[0][0] == board[1][1] == board[2][2] == turn:
        return True
    if board[0][2] == board[1][1] == board[2][0] == turn:
        return True

    return False

def pos_available(board, i, j):
    return board[i][j] == ' '

def is_full(board):
    for i in range(3):
        for j in range(3):
            if pos_available(board, i, j):
                return False
    return True

def get_possible_moves(board):
    moves = []
    for i in range(3):
        for j in range(3):
            if pos_available(board, i, j):
                moves.append([i, j])

    return moves

def make_move(board, position, turn):
    board[position[0]][position[1]] = turn

def undo_move(board, position):
    board[position[0]][position[1]] = ' '

def minimax(board, maximize_score):
    if is_win(board, 'O'):
        return 1
    elif is_win(board, 'X'):
        return -1
    elif is_full(board):
        return 0

    scores = []
    for move in get_possible_moves(board):
        turn = 'O' if maximize_score else 'X'
        make_move(board, move, turn)
        scores.append(minimax(board, not maximize_score))
        undo_move(board, move)

    return max(scores) if maximize_score else min(scores)

def make_best_move(board):
    best_score = -math.inf
    best_move = None

    for move in get_possible_moves(board):
        make_move(board, move, 'O')
        score = minimax(board, False)
        undo_move(board, move)

        if score > best_score:
            best_score = score
            best_move = move

    print(f"The AI's optimal score is {str(best_score)}")
    make_move(board, best_move, 'O')

def play_game():
    print("Starting Tic Tac Toe")
    player_turn = input("Enter 'f' to go first or 's' to go second: ").upper()

    # Player will always be X, AI will always be O
    if player_turn == 'F':
        current_turn = 'X'
    else:
        current_turn = 'O'

    board = [[' ' for col in range(3)] for row in range(3)]
    
    while True:
        # Show the Current Board
        print_board(board)

        if current_turn == 'X':

            # Check if the AI player won the game on their previous turn, or if the game has ended in a draw
            if is_win(board, 'O'):
                return "The AI wins!"
            elif is_full(board):
                return "It is a tie!"

            
            player_choice = input("Select a column and row between 0 and 2. Example: '0 1': ")
            print(f"You chose {player_choice}")
            choice = list(map(int, player_choice.split()))
            i = choice[0]
            j = choice[1]
            if pos_available(board, i, j):
                make_move(board, [i, j], 'X')
                current_turn = 'O'
            else:
                print(f"Invalid input. Position {i} {j} is taken.")
        else:
            # Check if the human player won the game on their previous turn, or if the game has ended in a draw
            if is_win(board, 'X'):
                return "You win!"
            elif is_full(board):
                return "It is a tie!"

            print("The AI is thinking...")
            make_best_move(board)
            current_turn = 'X'

def main():
    winner = play_game()
    print(winner)

if __name__ == '__main__':
    main()