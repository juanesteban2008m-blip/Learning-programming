
from random import randint 
# Functions 
def roll_dices():
    dice1 = randint(1, 6) 
    dice2 = randint(1, 6)
    return dice1, dice2 
dices = roll dices ()
 print(dices)
 print(f"Dice 1: {dice[1]}")
 print(f"Dice 2: {dice[2]}")
 
 if (dices[0] == dices[1]):
    print("You've win")
    else:
        print("Try again !!!")
        