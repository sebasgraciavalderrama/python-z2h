#Three Cup Monte
from random import shuffle
example = [1,2,3,4,5,6,7,8,9]
shuffle(example)
print(example)

def shuffle_list(myList):
    shuffle(myList)
    return myList

def player_guess():
    guess = ''
    while guess not in ['0','1','2']:
        guess = input("Pick a number: 0, 1 or 2: ")
    return int(guess)

def check_guess (myList, guess):
    if myList[guess] == 'O':
        print("Correct, you won!")
    else:
        print("Wrong, try again!")
        print(myList)

#Initial list
myList = [' ', 'O', '']
#Shuffle list
shuffled_list = shuffle_list(myList)
#User guess
guess = player_guess()
#Check guess
check_guess(shuffled_list, guess)
