# Project 1 - Snake Water Gun Game

'''

Name: Tushar Singh
Date: 25 December 2021
Language: Python

'''

''' First let us list the moves that win against certain other moves : -> '''
# snake > water
# water > gun
# gun > snake

import random

comp = ""

def gameWin(comp, you):

    ''' Function to write the snake water gun game functionality '''
    ''' "True" signifies you won the game whereas "False" signiies you lost the game against the computer '''

    # If both computer and you chose the same move
    if comp == you:
        return None

    # Check the rest of the ossibilities
    elif (comp == 's'):
        if (you == 'w'):
            return False
        elif (you == 'g'):
            return True
    elif (comp == 'g'):
        if (you == 's'):
            return False
        elif (you == 'w'):
            return True
    elif (comp == 'w'):
        if (you == 's'):
            return True
        elif (you == 'g'):
            return False

    

print("Computer's turn: Snake(s) or Gun(g) or Water(w): [selected]")
randomNumber = random.randint(1, 3)   # generating random move for computer's turn

if randomNumber == 1:
    computer = 's'
elif randomNumber == 2:
    computer = 'g'
else:
    computer = 'w'

you = input("Your Turn: Snake(s) or Gun(g) or Water(w): ")   # Asking user to select his move

print(f"Computer chose {computer}")
print(f"You chose {you}")

a = gameWin(computer, you)    # Function call

if a == None:
    print("Game is a tie")
elif a == True:
    print("Congratulations! You won the game!")
elif a == False:
    print("You lost the game!")









