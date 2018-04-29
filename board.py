from random import randint

board = [
    ["O","O","O","O","O"],
    ["O","O","O","O","O"],
    ["O","O","O","O","O"],
    ["O","O","O","O","O"],
    ["O","O","O","O","O"]
]


def printBoard():
    for i in range(0,5):
        print(board[i][0] + " " + board[i][1] + " " + board[i][2] + " " + board[i][3] + " " + board[i][4])
    print()

def genShip(x,y):
    out = str(y) + " " + str(x)
    return(out)

def fire(x,y):
    if board[x][y] == "X":
        return True
    else:
        board[x][y] = "X"
        guess = str(y) + " " + str(x)
        return(guess)
    


    

