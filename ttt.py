
def insertSymb(gameboard, loc, symb):
    board_copy=[]
    dec_loc = (loc[0] - 1)*3 + (loc[1]-1)
    if gameboard[dec_loc] != "":
        raise Exception(f"This location already has a {gameboard[dec_loc]} in it! Choose somewhere else!")
    for i in range(0, len(gameboard)):
        if i == dec_loc:
            board_copy.append(symb)
        else:
            board_copy.append(gameboard[i])
    return board_copy

def insertCross(gameboard, loc):
    return insertSymb(gameboard, loc, "X")

def insertNought(gameboard, loc):
    return insertSymb(gameboard, loc, "O")

def prettyBoard(gameboard):
    initStr = ""
    for i in range(0, 9):
        if i % 3 == 0 or i % 3 == 1:
            if gameboard[i] == "":
                initStr += " " + "|"
            else:
                initStr += gameboard[i] + "|"
        elif i % 3 == 2 and i != 8:
            if gameboard[i] == "":
                initStr += " " + "\n-----\n"
            else:
                initStr += gameboard[i] + "\n-----\n"
        else:
            if gameboard[i] == "":
                initStr+= " "
            else:
                initStr += gameboard[i]
    print(initStr)


def transpose(gameboard):
    board = []
    for i in range(0, 9):
        if i == 0:
            board.append(gameboard[0])
        elif i == 1:
            board.append(gameboard[3])
        elif i == 2:
            board.append(gameboard[6])
        elif i == 3:
            board.append(gameboard[1])
        elif i == 4:
            board.append(gameboard[4])
        elif i == 5:
            board.append(gameboard[7])
        elif i == 6:
            board.append(gameboard[2])
        elif i == 7:
            board.append(gameboard[5])
        elif i == 8:
            board.append(gameboard[8])
    return board


def horWinCondition(gameboard):
    for i in range(0,3):
        if gameboard[0+i] == gameboard[1+i] and gameboard[1+i] == gameboard[2+i] and gameboard[0+i] != "":
            return True
        else:
            return False

def verWinCondition(gameboard):
    return (horWinCondition(transpose(gameboard)))

def diagWinCondition(gameboard):
    if gameboard[0] == gameboard[4] and gameboard[4] == gameboard[8] and gameboard[0] != "":
        return True
    elif gameboard[2] == gameboard[4] and gameboard[4] == gameboard[6] and gameboard[2] != "":
        return True
    else:
        return False

def winCondition(gameboard):
    return horWinCondition(gameboard) or verWinCondition(gameboard) or diagWinCondition(gameboard)

def fullBoard(gameboard):
    for i in gameboard:
        if i == "":
            return False
    return True

def convertInput(tup):
    return (int(tup[0], int(tup[1])))


gameboard = ["","","","","","","","",""]
for turn in range(0,9):
    prettyBoard(gameboard)

    if turn % 2 == 0:
        Xrow = int(input("Crosses go row: "))
        Xcol = int(input("Crosses go col: "))
        gameboard = insertCross(gameboard, (Xrow, Xcol))
        if winCondition(gameboard):
            winner = "Crosses"
            break
    else:
        Orow = int((input("Noughts go row: ")))
        Ocol = int((input ("Noughts go col: ")))
        gameboard = insertNought(gameboard, (Orow, Ocol))
        if winCondition(gameboard):
            winner = "Noughts"
            break

prettyBoard(gameboard)
if turn < 8:
    print(f"The winner is {winner}! Congratulations!")
else:
    print("It's a draw...")
