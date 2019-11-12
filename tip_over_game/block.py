
from direction import Direction


class Block:
    def __init__(self, numberOfBlocks, currPos):
        self.numberOfBlocks = numberOfBlocks #int
        self.currPos = currPos # Tuple (x,y)
    
    ## Where the actual toppling happens
    ## y and x are reversed
    def topple(self, board, direction):
        (x,y) = self.currPos
        delCurrBlock = board.findBlockWithCoor(self.currPos)
        del board[delCurrBlock]
        if direction == Direction.DOWN:
            for i in range(numberOfBlocks):
                newX = x + i
                if(newX < 6 and newX >= 0):
                    newCoor = (newX,y)
                    delBlock = board.findBlockWithCoor(newCoor)
                    del board[delBlock]
                    board[Block(1, newCoor)] = [1]
                    
            return board

        elif direction == Direction.LEFT:
            for i in range(numberOfBlocks):
                newY = y-i
                if(newY > 6 and newY >= 0):
                    newCoor = (x,newY)
                    delBlock = board.findBlockWithCoor(newCoor)
                    del board[delBlock]
                    board[Block(1, newCoor)] = [1]
                    
            return board

        elif direction == Direction.RIGHT:
            for i in range(numberOfBlocks):
                newY = y+i
                if(newY > 6 and newY >= 0):
                    newCoor = (x,newY)
                    delBlock = board.findBlockWithCoor(newCoor)
                    del board[delBlock]
                    board[Block(1, newCoor)] = [1]
                    
            return board
        
        elif direction == Direction.UP:
            for i in range(numberOfBlocks):
                newX = x-i
                if(newX > 6 and newX >= 0):
                    newCoor = (newX,y)
                    delBlock = board.findBlockWithCoor(newCoor)
                    del board[delBlock]
                    board[Block(1, newCoor)] = [1]
                    
            return board
    
    # Get coordinate
    def getCoor(self):
        return self.currPos

    # Get number of Blocks
    def getNumBlocks(self):
        return self.numberOfBlocks