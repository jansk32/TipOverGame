from board import Board
from direction import Direction
from character import Character
import csv


def main():
    complete = False
    new_board = Board()
    new_board.build_empty_board()

    ## new_board.setUp('X', char.currPos)
    ## Set up for 4 (1,5) | 2 (2,5) | 2 (5,0) | 3 (2,0) | F (5,3)
    finishCoor = setUpGame(new_board,"level_1.csv")
    
    
    new_board.print_board_coor()
    print("\n")
    new_board.print_board()
    new_board.print_block_number()
    print("\n\n")
    while complete == False:
        dir = dirConvert(input("Next Move (U,L,R,or D):"))
        # print(dir)

        ## move should return a new board
        new_board = new_board.moveChar(dir)
        new_board.print_board()
        new_board.print_block_number()
        print("\n\n")

        # Check to see if player reached goal
        fBlock = new_board.findBlockWithCoor(finishCoor)
        if new_board.board[fBlock].getChar() == True:
            complete = True
    
    print("PUZZLE SOLVED!")

# Converts the letters to directions
def dirConvert(dir):
    dir = dir.lower()
    if (dir == 'u'):
        return Direction.UP
    elif(dir == 'd'):
        return Direction.DOWN
    elif(dir == 'l'):
        return Direction.LEFT
    elif(dir == 'r'):
        return Direction.RIGHT

def setUpGame(boardObj, fileName):
    '''
    Format of CSV file
    *** each Block ****
    4,4,5 ===> numBlock, x,y
    X,4,5 ==> Char, char coordinate
    F,4,5 ==> Finish, finish coordinate
    '''
    csvFile = open(fileName, "r")
    for line in (csv.reader(csvFile)):
        if (line[0]== "X"):
            x = int(line[1])
            y = int(line[2])
            coor = (x,y)
            print(coor)
            char = Character(coor)
            boardObj.addChar(coor)
            boardObj.setChar(char)
        elif(line[0] == "F"):
            x = int(line[1])
            y = int(line[2])
            finishCoor = (x,y)
            boardObj.setUp(1, (x,y))
            boardObj.setFinish((x,y))
        else:
            numBlock = int(line[0])
            x = int(line[1])
            y = int(line[2])
            coor = (x,y)
            boardObj.setUp(numBlock, coor)
    csvFile.close()
    return finishCoor

if __name__ == "__main__":
    main()