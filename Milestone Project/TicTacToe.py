tictactoe_board = [['1','2','3'],
                   ['4','O','6'],
                   ['7','8','9']]

def win(*args): # check if any player won after inserting a 'X' or 'O' in the board
    pass

def position_available(*args): # Given a position on the board, check if that position is available to be inserted or if its already taken
    return any (args in x for x in tictactoe_board)

def who_goes_first(): # Define who goes firts: 'X' or 'O'
    choice = 'WRONG'
    while choice == 'WRONG':
        decision = input('Who goes first? (X or O): ').upper()
        if decision in ('X', 'O'):
            return decision

def insert_player_choice (tictactoe_board, player_choice, player = ''): # Change board position to 'X' or 'O'
    my_tuple = get_index_of_player_choice(tictactoe_board, player_choice)
    if my_tuple == (-1,-1):
        print('Could not insert player choice, position already taken!')
        print_board(tictactoe_board)
        return False
    (i, j) = my_tuple
    tictactoe_board[i][j] = player.upper()
    print('Position changed successfully!')
    print_board(tictactoe_board)
    return True


def get_index_of_player_choice(tictactoe_board, player_choice):
    for i, item in enumerate(tictactoe_board):
        if player_choice in item:
            return i, item.index(player_choice)
    return -1,-1


def print_board(tictactoe_board): # Print board after any update (instert, win, etc)
    for item in tictactoe_board:
        print(" ".join(map(str, item)))


print(insert_player_choice(tictactoe_board, '2', 'X'))

'''
player_turn = False
player_choice = input('Where would you like to place your symbol?: ')
anybody_won = False
while not anybody_won:
    if player_turn == False:
        insert_player_choice(tictactoe_board, player_choice, 'X')
        anybody_won = win
    else:
        insert_player_choice(tictactoe_board, player_choice, 'O')
        anybody_won = win
'''