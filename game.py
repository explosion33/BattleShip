import board
from random import randint
i = 0
turns = 10
offset = 0

board.printBoard()
ship = board.genShip(randint(0,4), randint(0,4))

while i < turns:
    print("Turn " + str(i + 1))
    print()
    while True:
        try:
            guessY = int(input("guess Y: "))
            guessX = int(input("guess X: "))
        except ValueError:
            print()
            print("Thats not even a number")
            print()
        else:
            break
        
    guess = board.fire(guessX-1, guessY-1)

    if guess == True:
        print()
        print("You already guessed that")
        print()
        i -= 1

    if guessY > 4 or guessX > 4:
        print()
        print("You must guess within the ocean")
        i -= 1

    if guess == ship:
        print("You Win")
        break
    print()
    board.printBoard()
    i += 1
else:
    print("You Lose")