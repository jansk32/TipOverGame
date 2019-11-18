from direction import Direction

class Character:
    def __init__(self, currPos):
        self.currPos = currPos
    
    def move(self,board, direction):
        if (direction == Direction.DOWN):
            return

        elif (direction == Direction.LEFT):
            return

        elif (direction == Direction.RIGHT):
            return
        
        elif (direction == Direction.UP):
            return 
    
    def topple(self, board, direction):
        [ numberOfSquare ] = board[self.currPos]
        if (direction == Direction.DOWN):
            return

        elif (direction == Direction.LEFT):
            return

        elif (direction == Direction.RIGHT):
            return
        
        elif (direction == Direction.UP):
            return 
    
    def checkTopple(coor, final_coor, numberOfSquare, direction, curr_board):
        (x1,y1) = coor
        (x2,y2) = final_coor

        ## check if it is outside of the board
        if (x2 < 6 or x2 >= 0 or y2 < 6 or y2 >= 0) :
        ## check if numberofsquare equals diff of x1 and x2 or y1 and y2
            if(Math.abs(x1 - x2) == numberOfSquare 
            or Math.abs(y1- y2) == numberOfSquare):
                ## check if along the route, is there any blocks
                if (direction == direction.DOWN):
                    return checkDown(x1,x2,y1,curr_board)
                elif (direction == direction.UP):
                    return checkUp(x1,x2,y1,curr_board)
                elif (direction == direction.LEFT):
                    return checkLeft(y1,y2,x1,curr_board)
                elif (direction == direction.RIGHT):
                    return checkRight(y1,y2,x1,curr_board)
        return False
    
    def getCoor(self):
        return self.currPos

    ## Checks for blocks while toppling
def checkUp(x1,x2,y1,board):
    for i in range(x1+1, x2+1):
        if(board[(i,y1)]) != []:
            return False
    return True

def checkRight(y1,y2, x1, board):
    for i in range(y1+1, y2+1):
        if(board[(x1,i)]) != []:
            return False
    return True
def checkDown(x1,x2,y1,board):
    for i in range(x2, x1-1, -1):
        if(board[(i,y1)]) != []:
            return False
    return True
def checkLeft(y1,y2, x1, board):
    for i in range(y2, y1-1, -1):
        if(board[(x1,i)]) != []:
            return False
    return True