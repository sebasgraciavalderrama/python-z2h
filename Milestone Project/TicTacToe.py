tictactoe_board = [['1','2','3'],
                   ['4','5','6'],
                   ['7','8','9']]

'''
win_position_vertical_1 = {(0,0),(1,0),(2,0)}
win_position_vertical_2 = {(0,1),(1,1),(2,1)}
win_position_vertical_3 = {(0,2),(1,2),(2,2)}
win_position_horizontal_1 = {(0,0),(0,1),(0,2)}
win_position_horizontal_2 = {(1,0),(1,1),(0,2)}
win_position_horizontal_3 = {(2,0),(2,1),(2,2)}
win_position_cross_1 = {(0,0),(1,1),(2,2)}
win_position_cross_1 = {(0,2),(1,1),(2,0)}
'''
def tie(player=''): # Check if at any given point in time the result of the match is a tie, returns True if tie
    print('Match has resulted with a tie!')
    return True

def win(player=''): # Check if any player won after inserting a 'X' or 'O' in the board, returns True if any player has won
    #(board[7] == board[8] == board[9] == marker)
    print(f'Player {player} has won!')
    return True

def position_available(*args): # Given a position on the board, check if that position is available to be inserted or if its already taken
    return any (args in x for x in tictactoe_board)

def who_goes_first(): # Define who goes firts: 'X' or 'O', returns 'X' or ? based on user input
    choice = 'WRONG'
    while choice == 'WRONG':
        decision = input('Who goes first? (X or O): ').upper()
        if decision in ('X', 'O'):
            return decision

def insert_player_choice (tictactoe_board, player_choice, player = ''): # Inserts player symbol given a position of the board, returns True if insertion was successful
    my_tuple = get_index_of_player_choice(tictactoe_board, player_choice)
    if my_tuple == (-1,-1):
        print('Could not insert player choice, position already taken or not valid!')
        print_board(tictactoe_board)
        return False
    (i, j) = my_tuple
    tictactoe_board[i][j] = player.upper()
    print('Position changed successfully!')
    print_board(tictactoe_board)
    return True

def get_index_of_player_choice(tictactoe_board, player_choice): # Returns the position x, y (tuple) of the player's choice, if not found or found symbol ('X', 'Y') returns (-1,-1)
    for i, item in enumerate(tictactoe_board):
        if player_choice in item:
            return i, item.index(player_choice)
    return -1,-1

def print_board(tictactoe_board): # Prints board after any update (instert, win, etc)
    print("#---------------------------------------#")
    for item in tictactoe_board:
        print(" ".join(map(str, item)))
    print("#---------------------------------------#")

#-----------------------------------------MAIN SECTION - BEGIN-----------------------------------------#

# Initialization of variables
player_turn = False
anybody_won = False
valid_input = False
print("Welcome to Sebastian's poorly-optimized-TicTacToe game!!!")

# If statement to define which player 'X' or 'Y' gets to play first.
decision = who_goes_first()
if decision == 'X':
    player_turn = False
else:
    player_turn = True

while not anybody_won: # While loop to play until any player won or tied match
    valid_input = False
    if not player_turn: # If statement to control players turn
        while not valid_input: # While loop to get users 1)input 2)insertion 3)validation of win or tie
            print('Your turn X...')
            print_board(tictactoe_board)
            player_symbol = 'X'
            player_choice = input('Where would you like to place your symbol?: ')
            valid = insert_player_choice(tictactoe_board, player_choice, player_symbol)
            if valid:
                # Insertion was successful, next player can play
                valid_input = True
                player_turn = True
        '''
        TODO: Win function
        anybody_won = win(player_symbol)
        '''
    elif player_turn:
        while not valid_input:
            print('Your turn O...')
            print_board(tictactoe_board)
            player_symbol = 'O'
            player_choice = input('Where would you like to place your symbol?: ')
            valid = insert_player_choice(tictactoe_board, player_choice, player_symbol)
            if valid:
                # Insertion was successful, next player can play
                valid_input = True
                player_turn = False
        '''
        TODO: Win function
        anybody_won = win(player_symbol)
        '''
#-----------------------------------------MAIN SECTION - END-----------------------------------------#