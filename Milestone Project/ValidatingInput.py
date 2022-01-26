def user_choice():
    choice = 'WRONG'
    acceptable_range = range(0,10) #[0,1,2,3,4,5,6,7,8,9]
    while choice.isdigit() == False:
        choice = input('Please enter a number (0-10): ')
        if choice.isdigit() == False or int(choice) not in range(0,11):
            print('Sorry that is not a digit or not in range!')
    return int(choice)

user_choice()