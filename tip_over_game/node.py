from character import topple, checkDown, checkLeft, checkRight, checkUp
from direction import Direction
import copy

class Node:
    
    def __init__(self, curr, prev, boardObj):
        self.currCoor = curr
        self.prevNode = prev
        self.boardObj = boardObj
        self.f = self.g = self.h = 0
    
    # Generate states
    def generateStates(self, boardObj):
        arr = []
        (x,y) = self.currCoor
        prev = None
        if self.prevNode == None:
            prev = (-1,-1)
        else:
            prev = self.prevNode.getCurr()

        if ((x+1,y) != prev and x+1 < 6 ):
            boardObj_new = copy.deepcopy(boardObj)
            nextCoor = (x+1,y)
            b_start = boardObj_new.findBlockWithCoor(self.currCoor)
            b_end = boardObj_new.findBlockWithCoor(nextCoor)
            if(x+1 < 6 and boardObj_new.board[b_end].getNumBlocks() > 0):
                ## Unset the current coor
                boardObj_new.board[b_start].setChar()
                boardObj_new.board[b_end].setChar()
            if(boardObj_new.board[b_end].getNumBlocks() == 0 and 
            boardObj_new.board[b_start].getNumBlocks() > 1):
                topple(self.currCoor, boardObj_new,Direction.DOWN)
                boardObj_new.board[b_start].setChar()
                boardObj_new.board[b_end].setChar()
            
            arr.append(Node((x+1,y), self, boardObj_new))

        if ((x-1,y) != prev and x-1 >= 0 and boardObj.findBlockWithCoor((x-1,y)) != 0):
            boardObj_new_u = copy.deepcopy(boardObj)
            nextCoor = (x-1,y)
            b_start = boardObj_new_u.findBlockWithCoor(self.currCoor)
            b_end = boardObj_new_u.findBlockWithCoor(nextCoor)
            if(x-1 < 6 and boardObj_new_u.board[b_end].getNumBlocks() > 0):
                boardObj_new_u.board[b_start].setChar()
                boardObj_new_u.board[b_end].setChar()
            if(boardObj_new_u.board[b_end].getNumBlocks() == 0 and 
            boardObj_new_u.board[b_start].getNumBlocks() > 1):
                topple(self.currCoor,boardObj_new_u,Direction.UP)
                boardObj_new_u.board[b_start].setChar()
                boardObj_new_u.board[b_end].setChar()

            arr.append(Node((x-1,y), self, boardObj_new_u))

        if ((x,y+1) != prev and y+1 < 6 and boardObj.findBlockWithCoor((x,y+1)) != 0):
            boardObj_new_r = copy.deepcopy(boardObj)
            nextCoor = (x,y+1)
            b_start = boardObj_new_r.findBlockWithCoor(self.currCoor)
            b_end = boardObj_new_r.findBlockWithCoor(nextCoor)
            if(y+1 < 6 and boardObj_new_r.board[b_end].getNumBlocks() > 0):
                boardObj_new_r.board[b_start].setChar()
                boardObj_new_r.board[b_end].setChar()
            if(boardObj_new_r.board[b_end].getNumBlocks() == 0 and
            boardObj_new_r.board[b_start].getNumBlocks() > 1):
                topple(self.currCoor,boardObj_new_r,Direction.RIGHT)
                boardObj_new_r.board[b_start].setChar()
                boardObj_new_r.board[b_end].setChar()

            arr.append(Node((x,y+1), self, boardObj_new_r))

        if ((x,y-1) != prev and y-1 >= 0 and boardObj.findBlockWithCoor((x,y-1)) != 0):
            boardObj_new_l = copy.deepcopy(boardObj)
            nextCoor = (x,y-1)
            b_start = boardObj_new_l.findBlockWithCoor(self.currCoor)
            b_end = boardObj_new_l.findBlockWithCoor(nextCoor)
            if(y-1 >= 0 and boardObj_new_l.board[b_end].getNumBlocks() > 0):
                boardObj_new_l.board[b_start].setChar()
                boardObj_new_l.board[b_end].setChar()
            if(boardObj_new_l.board[b_end].getNumBlocks() == 0 and
            boardObj_new_l.board[b_start].getNumBlocks() > 1):
                topple(self.currCoor,boardObj_new_l,Direction.LEFT)
                boardObj_new_l.board[b_start].setChar()
                boardObj_new_l.board[b_end].setChar()

            arr.append(Node((x,y-1), self, boardObj_new_l))
        
        return arr



    #### GETTERS AND SETTERS ######
    def getCurr(self):
        return self.currCoor
    
    def getPrev(self):
        return self.prevNode

    def getH(self):
        return self.h
    
    def setH(self,val):
        self.h = val
    
    def getF(self):
        return self.f
    
    def setF(self,val):
        self.f = val
    
    def getG(self):
        return self.g
    
    def setG(self,val):
        self.g = val