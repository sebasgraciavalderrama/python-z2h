tictactoe_board = [[1,2,3],
                   [4,'X',6],
                   [7,8,9]]

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


def insert_player_choice (tictactoe_board, player_choice, player): # Change board position to 'X' or 'O'
    i, j = get_index_of_player_choice(tictactoe_board, 11)
    print(f' {i} {j}')
    if tictactoe_board[i][j] in ('X', 'O'):
        print('Position already taken, please try a different position!!!')
        print_board(tictactoe_board)
        return False
    elif tictactoe_board[i][j] not in ('X', 'O'):
        tictactoe_board[i][j] = player.upper()
        print_board(tictactoe_board)
        return True


def get_index_of_player_choice(tictactoe_board, player_choice):
    if player_choice not in range(0,10):
        return 'Please enter a valid position (1-9)!!!'
    for i in range(len(tictactoe_board)):
      try:
            j = tictactoe_board[i].index(player_choice)
            return (i,j)
      except ValueError:
          pass
    raise ValueError


def print_board(tictactoe_board): # Print board after any update (instert, win, etc)
    for item in tictactoe_board:
        print(" ".join(map(str, item)))


print(insert_player_choice(tictactoe_board, 11,'x'))