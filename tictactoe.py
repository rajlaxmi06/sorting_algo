def display_board(board):
    print('    |     |')
    print('  ' +board[7] + ' | ' + board[8] + ' | '+board[9])
    print('    |     |')
    print('--------------')
    print('    |     |')
    print('  ' +board[4] + ' | ' + board[5] + ' | '+board[6])
    print('    |     |')
    print('--------------')
    print('    |     |')
    print('  ' +board[1] + ' | ' + board[2] + ' | '+board[3])
    print('    |     |')

def player_input():
    marker=' '
    while not (marker=='O' or marker=='X'):
        marker=input("Player 1: Do you want X or O").upper()
    if marker=='X':
        return('X','O')
    else:
        return('O','X')

def place_marker(board,marker,position):
    board[position]=marker

def win_check(board,marker):
    return ((board[7]==marker and board[8]==marker and board[9]==marker) or 
    (board[4]==marker and board[5]==marker and board[6]==marker) or 
    (board[1]==marker and board[2]==marker and board[3]==marker) or 
    (board[1]==marker and board[4]==marker and board[7]==marker) or 
    (board[2]==marker and board[5]==marker and board[8]==marker) or 
    (board[3]==marker and board[6]==marker and board[9]==marker) or 
    (board[7]==marker and board[3]==marker and board[5]==marker) or 
    (board[5]==marker and board[1]==marker and board[9]==marker))

import random
def choose_first():
    if random.randint(0,1)==0:
        return 'Player 1'
    else:
        return 'Player 2'

def space_check(board,position):
    return board[position]==' '

def full_board_check(board):
    for i in range(1,10):
        if space_check(board,i):
            return False
    return True

def player_choice(board):
    position=' '
    while position not in '1 2 3 4 5 6 7 8 9'.split() or not space_check(board,int(position)):
        position=input("Choose your next position")
    return int(position)

def replay():
    return input("Do you want to play again? Enter yes or no").lower().startswith('y')

print('Welcome to tic tac toe')

while True:
    theBoard=[' ']*10
    player1_marker, player2_marker=player_input()
    turn=choose_first()
    print(turn+ ' will go first! ')
    game_on=True
    while game_on:
        if turn== 'Player 1':
            display_board(theBoard)
            position= player_choice(theBoard)
            place_marker(theBoard,player1_marker,position)

            if win_check(theBoard,player1_marker):
                display_board(theBoard)
                print('Congrats player 1 has won the game')
                game_on=False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw')
                else:
                    turn='Player 2'
        else:
            display_board(theBoard)
            position= player_choice(theBoard)
            place_marker(theBoard,player2_marker,position)


            if win_check(theBoard,player2_marker):
                display_board(theBoard)
                print('Congrats player 2 has won the game')
                game_on=False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw')
                else:
                    turn='Player 1'
    if not replay():
        break