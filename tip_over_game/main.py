from board import Board
from direction import Direction
from character import Character


def main():
    complete = False
    new_board = Board()
    new_board.build_empty_board()
    char = Character((2,3))

    new_board.setUp(3, (5,5))
    new_board.setUp('X', char.currPos)
    new_board.print_board()
    while complete == False:
        dir = dirConvert(input("Next Move (U,L,R,or D):"))

        ## move should return a new board
        ## new_board = char.move(new_board, dir)

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