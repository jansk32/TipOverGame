from direction import Direction
from character import Character
from board import Board
from node import Node

class Player:
    def __init__(self,boardObj):
        self.char = None
        self.boardObj = boardObj
    
    def astar(self, boardObj):
        dir = Direction.DOWN
        startBlock = self.getCharBlock(boardObj).getCoor()
        finishBlock = self.getFinishBlock(boardObj).getCoor()
        open_list = []
        closed_list = []

        open_list.append(startBlock)

        # (curr, next, f)
        # f = g + h


        while len(open_list) > 0:

            # Set current coordinate
            curr_coor = open_list[0]
            



        return dir

    # Find the current block of character
    def getCharBlock(self,boardObj):
        for bloc in boardObj.board:
            if bloc.getChar() == True:
                return bloc
        return None
    
    # Find the finish block
    def getFinishBlock(self,boardObj):
        for bloc in boardObj.board:
            if bloc.getFinish() == True:
                return bloc
        return None