import board
import os
from random import randint
i = 0
error = ""
turns = 8
offset = 0
unused_variable = os.system("cls")
board.printBoard()
ship = board.genShip(randint(0,4), randint(0,4))

while i < turns:
    print(error)
    print("Turn " + str(i + 1))
    print()
    while True:
        try:
            guessY = int(input("guess X: "))
            guessX = int(input("guess Y: "))
        except ValueError:
            unused_variable = os.system("cls")
            board.printBoard()
            print("Thats not even a number")
            print("Turn " + str(i+1))
            print()
        else:
            break
        
    
    if guessY > 5 or guessX > 5 or guessY <= 0 or guessX <= 0:
        error = "You must guess within the ocean"
        i -= 1
        guess = False
    else:
        guess = board.fire(guessX-1, guessY-1)
    if guess == True:
        error = "You already guessed that"
        i -= 1

    
    if guess == ship:
        unused_variable = os.system("cls")
        print("You Win")
        break
    unused_variable = os.system("cls")
    board.printBoard()
    i += 1
else:
    print("You Lose")
    print()
    print("Ship Location:")
    print("     X: " + str(int(ship[0]) + 1))
    print("     Y: " + str(int(ship[2]) + 1))