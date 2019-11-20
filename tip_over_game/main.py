from board import Board
from direction import Direction
from character import Character


def main():
    complete = False
    char = Character((1,5))
    new_board = Board(char)
    new_board.build_empty_board()
    finishCoor = (5,3)

    ## new_board.setUp('X', char.currPos)
    ## Set up for 4 (1,5) | 2 (2,5) | 2 (5,0) | 3 (2,0) | F (5,3)
    new_board.setUp(4, (1,5))
    new_board.setUp(2, (2,5))
    new_board.setUp(2, (5,0))
    new_board.setUp(3, (1,0))
    new_board.setUp(1, finishCoor)
    new_board.setFinish(finishCoor)

    
    new_board.print_board_coor()
    print("\n")
    new_board.print_board()
    new_board.print_block_number()
    while complete == False:
        dir = dirConvert(input("Next Move (U,L,R,or D):"))
        print(dir)

        ## move should return a new board
        new_board = new_board.moveChar(dir)
        new_board.print_board()

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
if __name__ == "__main__":
    main()