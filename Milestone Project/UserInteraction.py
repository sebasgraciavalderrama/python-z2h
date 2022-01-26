game_list = [0,1,2]

def display_game(game_list):
    print('Here is the current list: ')
    print(game_list)

def position_choice():
    choice = 'wrong'
    while choice not in ['0','1','2']:
        choice = input("Pick a position to replace (0,1,2): ")
        if choice not in ['0','1','2']:
            print("Sorry, but you did not choose a valid position (0,1,2)")
    return int(choice)

def replacement_choice(game_list,position):
    user_placement = input("Type a string to place at the position: ")
    game_list[position] = user_placement
    return game_list

def gameon_choice():
    choice = 'wrong'
    while choice not in ['Y','N']:
        choice = input("Would you like to keep playing? Y or N: ")
        if choice not in ['Y','N']:
            print("Sorry, I didn't understand. Please make sure to choose Y or N: ")
    if choice == "Y":
        return True
    else:
        return False


game_on = True

game_list = [0,1,2]



while game_on:
    display_game(game_list)
    # Have player choose position
    position = position_choice()
    # Rewrite that position and update game_list
    game_list = replacement_choice(game_list,position)
    display_game(game_list)
    # Ask if you want to keep playing
    game_on = gameon_choice()
