
from direction import Direction


class Block:
    def __init__(self, numberOfBlocks, currPos):
        self.numberOfBlocks = numberOfBlocks #int
        self.currPos = currPos # Tuple (x,y)
    
    def topple(self, board, direction):
        if direction == Direction.DOWN:
            return

        elif direction == Direction.LEFT:
            return

        elif direction == Direction.RIGHT:
            return
        
        elif direction == Direction.UP:
            return 
    
    # Get coordinate
    def getCoor(self):
        return self.currPos

    # Get number of Blocks
    def getNumBlocks(self):
        return self.numberOfBlocks