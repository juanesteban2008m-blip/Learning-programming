
# import libraries or packages
from random import randint
import os

# functions
def rollDices():
    dice1 = randint(1,6)
    dice2 = randint(1,6)
    return dice1, dice2
    return dice1, dice2

# declare and initialize variables and/or constants
Player_lives = 3
dice1 = 0
dice2 = 0
roll_count = 0
equal_count = 0
status=True


# Main
print(" welcom to casino :::")
press_key = input("\nPress any key to start the game :::")
while status:
    os.system('cls')
    dices = rollDices()
    roll_count += 1
    dices_add = 0
    print("#"* 20)
    print(f"Roll dices N°.: {roll_count}")
    print("#"* 20)
    print(f"Player lives: {Player_lives}")
    print(f"dice 1: {dices[0]}")
    print(f"dice 2: {dices[1]}")
    dices_add = dices[0] + dices[1]

if dices_add % 2 != 0:
    Player_lives-=1
    print("you ' ve lost one live ::: Now you have {player_lives} lives")
    if Player_lives == 0:
        print("::: GAME OVER :::")
            break

    if dices[0] == 6 and dices[1] == 6 or dices[0]==1 and dices[1] == 1:
        Player_lives+=1
        print("you 've win one live :::")
        print(f"Dices addition: {dices_add}")
    if player_lives == 0:
        print("::: game over :::")
        print(f"roll count: {roll_count}")
else:
    press_key = input ("\nPress any key to roll dices again")
