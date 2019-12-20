from direction import Direction

class Character:
    def __init__(self, currPos):
        self.currPos = currPos


    # Moves character and topple when possible
    def move(self,boardObj, direction):
        (x,y) = self.currPos
        if (direction == Direction.DOWN):
            nextCoor = (x+1,y)
            b_start = boardObj.findBlockWithCoor(self.currPos)
            b_end = boardObj.findBlockWithCoor(nextCoor)
            if b_end == None:
                return boardObj
            if(x+1 < 6 and boardObj.board[b_end].getNumBlocks() > 0):
                ## Unset the current coor
                self.setCoor(nextCoor)
                boardObj.board[b_start].setChar()
                boardObj.board[b_end].setChar()
            if(boardObj.board[b_end].getNumBlocks() == 0 and 
            boardObj.board[b_start].getNumBlocks() > 1):
                j = topple(self.currPos, boardObj,Direction.DOWN)
                if j == True:
                    self.setCoor(nextCoor)
                    boardObj.board[b_start].setChar()
                    boardObj.board[b_end].setChar()
            return boardObj

        elif (direction == Direction.LEFT):
            nextCoor = (x,y-1)
            b_start = boardObj.findBlockWithCoor(self.currPos)
            b_end = boardObj.findBlockWithCoor(nextCoor)
            if b_end == None:
                return boardObj
            if(y-1 >= 0 and boardObj.board[b_end].getNumBlocks() > 0):
                ## Unset the current coor
                self.setCoor(nextCoor)
                boardObj.board[b_start].setChar()
                boardObj.board[b_end].setChar()
            if(boardObj.board[b_end].getNumBlocks() == 0 and
            boardObj.board[b_start].getNumBlocks() > 1):
                j = topple(self.currPos,boardObj,Direction.LEFT)
                if j == True:
                    self.setCoor(nextCoor)
                    boardObj.board[b_start].setChar()
                    boardObj.board[b_end].setChar()
            return boardObj

        elif (direction == Direction.RIGHT):
            nextCoor = (x,y+1)
            b_start = boardObj.findBlockWithCoor(self.currPos)
            b_end = boardObj.findBlockWithCoor(nextCoor)
            if b_end == None:
                return boardObj
            if(y+1 < 6 and boardObj.board[b_end].getNumBlocks() > 0):
                ## Unset the current coor
                self.setCoor(nextCoor)
                boardObj.board[b_start].setChar()
                boardObj.board[b_end].setChar()
            if(boardObj.board[b_end].getNumBlocks() == 0 and
            boardObj.board[b_start].getNumBlocks() > 1):
                j = topple(self.currPos,boardObj,Direction.RIGHT)
                if j == True:
                    self.setCoor(nextCoor)
                    boardObj.board[b_start].setChar()
                    boardObj.board[b_end].setChar()
            return boardObj
        
        elif (direction == Direction.UP):
            nextCoor = (x-1,y)
            b_start = boardObj.findBlockWithCoor(self.currPos)
            b_end = boardObj.findBlockWithCoor(nextCoor)
            if b_end == None:
                return boardObj
            if(x-1 < 6 and boardObj.board[b_end].getNumBlocks() > 0):
                ## Unset the current coor
                self.setCoor(nextCoor)
                boardObj.board[b_start].setChar()
                boardObj.board[b_end].setChar()
            if(boardObj.board[b_end].getNumBlocks() == 0 and 
            boardObj.board[b_start].getNumBlocks() > 1):
                j = topple(self.currPos,boardObj,Direction.UP)
                if j == True:
                    self.setCoor(nextCoor)
                    boardObj.board[b_start].setChar()
                    boardObj.board[b_end].setChar()
            return boardObj
    

    def getCoor(self):
        return self.currPos
    
    def setCoor(self, coor):
        self.currPos = coor

# To topple the blocks
def topple(currPos, boardObj, direction):
    blockInd = boardObj.findBlockWithCoor(currPos)
    currBlock = boardObj.board[blockInd]
    (x1,y1) = currPos
    if (direction == Direction.DOWN):
        x2 = x1 + currBlock.getNumBlocks() - 1 
        (check, arr) = checkDown(x1,x2,y1,boardObj)
        if (check == True):
            for i in arr:
                boardObj.board[i].setNumBlocks(1)
            currBlock.setNumBlocks(0)
            return True
        else:
            return False

    elif (direction == Direction.LEFT):
        y2 = y1 - currBlock.getNumBlocks()
        (check, arr) = checkLeft(y1,y2,x1,boardObj)
        if (check == True):
            for i in arr:
                boardObj.board[i].setNumBlocks(1)
            currBlock.setNumBlocks(0)
            return True
        else:
            return False

    elif (direction == Direction.RIGHT):
        y2 = y1 + currBlock.getNumBlocks()
        (check, arr) = checkRight(y1,y2,x1,boardObj)
        if (check == True):
            for i in arr:
                boardObj.board[i].setNumBlocks(1)
            currBlock.setNumBlocks(0)
            return True
        else:
            return False
    
    elif (direction == Direction.UP):
        x2 = x1 - currBlock.getNumBlocks()
        (check, arr) = checkUp(x1,x2,y1,boardObj)
        if (check == True):
            for i in arr:
                boardObj.board[i].setNumBlocks(1)
            currBlock.setNumBlocks(0) 
            return True
        else:
            return False

## Checks for blocks while toppling
def checkUp(x1,x2,y1,boardObj):
    checked = []
    if x2 < 0:
        return (False, [])
    for i in range(x1-1, x2-1, -1):
        l = boardObj.findBlockWithCoor((i,y1))
        if(l == None or boardObj.board[l].getNumBlocks()) != 0 :
            return (False, [])
        else:
            checked.append(l)
    return (True, sorted(checked, reverse=True))

def checkRight(y1,y2, x1, boardObj):
    checked = []
    if y2 >= 6:
        return (False,[]) 
    for i in range(y1+1, y2+1):
        l = boardObj.findBlockWithCoor((x1,i))
        if(l == None or boardObj.board[l].getNumBlocks()) != 0:
            return (False,[])
        else:
            checked.append(l)
    return (True, checked)

def checkDown(x1,x2,y1,boardObj):
    checked = []
    if x2 >= 6:
        return (False, [])
    for i in range(x2+1, x1, -1):
        l = boardObj.findBlockWithCoor((i,y1))
        if(l == None or boardObj.board[l].getNumBlocks()) != 0:
            return (False, [])
        else:
            checked.append(l)
    return (True, checked)

def checkLeft(y1,y2, x1, boardObj):
    checked = []
    if y2 < 0:
        return (False, [])
    for i in range(y2, y1):
        l = boardObj.findBlockWithCoor((x1,i))
        if(l == None or boardObj.board[l].getNumBlocks()) != 0:
            return (False, [])
        else:
            checked.append(l)
    return (True, sorted(checked, reverse= True))