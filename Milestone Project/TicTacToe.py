tictactoe_board = [['1','2','3'],
                   ['4','5','6'],
                   ['7','8','9']]

def tie(number_of_plays): # Check if at any given point in time the result of the match is a tie, returns True if tie
    if number_of_plays >= 9:
        print('Match has resulted with a tie!')
        return True
    return False

def win(tictactoe_board, player=''): # Check if any player won after inserting a 'X' or 'O' in the board, returns True if any player has won
    if tictactoe_board[0][0] == tictactoe_board[1][0] == tictactoe_board[2][0] == player:
        # win_position_vertical_1 = {(0,0),(1,0),(2,0)}
        print(f'Player {player} has won!')
        return True
    if tictactoe_board[0][1] == tictactoe_board[1][1] == tictactoe_board[2][1] == player:
        # win_position_vertical_2 = {(0,1),(1,1),(2,1)}
        print(f'Player {player} has won!')
        return True
    if tictactoe_board[0][2] == tictactoe_board[1][2] == tictactoe_board[2][2] == player:
        # win_position_vertical_3 = {(0,2),(1,2),(2,2)}
        print(f'Player {player} has won!')
        return True
    if tictactoe_board[0][0] == tictactoe_board[0][1] == tictactoe_board[0][2] == player:
        # win_position_horizontal_1 = {(0,0),(0,1),(0,2)}
        print(f'Player {player} has won!')
        return True
    if tictactoe_board[1][0] == tictactoe_board[1][1] == tictactoe_board[1][2] == player:
        # win_position_horizontal_2 = {(1,0),(1,1),(1,2)}
        print(f'Player {player} has won!')
        return True
    if tictactoe_board[2][0] == tictactoe_board[2][1] == tictactoe_board[2][2] == player:
        # win_position_horizontal_3 = {(2,0),(2,1),(2,2)}
        print(f'Player {player} has won!')
        return True
    if tictactoe_board[0][0] == tictactoe_board[1][1] == tictactoe_board[2][2] == player:
        # win_position_cross_1 = {(0,0),(1,1),(2,2)}
        print(f'Player {player} has won!')
        return True
    if tictactoe_board[0][2] == tictactoe_board[1][1] == tictactoe_board[2][0] == player:
        # win_position_cross_2 = {(0,2),(1,1),(2,0)}
        print(f'Player {player} has won!')
        return True
    return False

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

def want_to_play_again():
    choice = 'WRONG'
    while choice == 'WRONG':
        decision = input('Want to play again? (Y/N): ').upper()
        if decision == 'Y':
            return False
        elif decision == 'N':
            return True

def clean_board(tictactoe_board):
    pass

#-----------------------------------------MAIN SECTION - BEGIN-----------------------------------------#

# Initialization of variables
player_turn = False
anybody_won = False
valid_input = False
number_of_plays = 0
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
        player_symbol = 'X'
        while not valid_input: # While loop to get users 1)input 2)insertion 3)validation of win or tie
            print('Your turn X...')
            print_board(tictactoe_board)
            player_choice = input('Where would you like to place your symbol?: ')
            valid = insert_player_choice(tictactoe_board, player_choice, player_symbol)
            if valid:
                # Insertion was successful, next player can play
                valid_input = True
                player_turn = True
                anybody_won = win(tictactoe_board, player_symbol)
                number_of_plays += 1
    elif player_turn:
        player_symbol = 'O'
        while not valid_input:
            print('Your turn O...')
            print_board(tictactoe_board)
            player_choice = input('Where would you like to place your symbol?: ')
            valid = insert_player_choice(tictactoe_board, player_choice, player_symbol)
            if valid:
                # Insertion was successful, next player can play
                valid_input = True
                player_turn = False
                anybody_won = win(tictactoe_board, player_symbol)
                number_of_plays += 1
    # For each player insertion, we increase numer_of_plays by 1, after each insertion we
    # call the tie() function which returns True if after 9 plays nobody won (tie)
    if tie(number_of_plays):
        anybody_won = True

    if anybody_won:
        # Would you like to play again?
        anybody_won =  want_to_play_again()
        if not anybody_won:
            player_turn = False
            anybody_won = False
            valid_input = False
            '''TODO:
                Find a way to clean/reset the board
                clean_board(tictactoe_board)
                tictactoe_board = [['1','2','3'],
                               ['4','5','6'],
                               ['7','8','9']]
            '''
            print("Welcome again tozgit Sebastian's poorly-optimized-TicTacToe game!!!")
            # If statement to define which player 'X' or 'Y' gets to play first.
            decision = who_goes_first()
            if decision == 'X':
                player_turn = False
            else:
                player_turn = True

print("Thank you for playing!, See you soon...")

#-----------------------------------------MAIN SECTION - END-----------------------------------------#