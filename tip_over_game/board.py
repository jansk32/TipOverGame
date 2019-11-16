from block import Block
from character import Character


EMPTY = [0]
'''
        for i in range(0,6):
            arr = []
            for j in range(0,6):
                arr.append(self.board[(i,j)])
            print(i, arr)
'''
class Board:
    
    def __init__(self):
        ## self.board = {}
        self.board = []
        self.start = (0,0)
        self.finish = (3,4)
    
    def build_empty_board(self):
        init_board = []
        for i in range(0,6):
            for j in range(0,6):
                b = Block(0, (i,j))
                ## init_board[b] = [0]
                init_board.append(b)
        self.board = init_board

    ## Print the board
    def print_board(self):
        grids = sorted(self.buildListOfTupleBoard())
        string = ""
        for i in range(len(grids)):
            string += str(grids[i][1])
            if i % 6 == 5:
                string += "\n"
            else:
                string += "   "
        print(string)

    ## Print board coordinates (for ref)
    def print_board_coor(self):
        grids = sorted(self.buildListOfTupleBoard())
        string = ""
        for i in range(len(grids)):
            string += str(grids[i][0])
            if i % 6 == 5:
                string += "\n"
            else:
                string += " "
        print(string)
    
    ## This is to give coordinates new elements or blocks
    ## ONLY if they have a [0]
    def setUp(self, blockNumber, coor):
        delBlock = self.findBlockWithCoor(coor)
        if self.board[delBlock].getNumBlocks() == 0:
            self.board[delBlock].setNumBlocks(blockNumber)
        '''
        if self.board[delBlock] == [0]:
            del self.board[delBlock]
        else:
            return
        self.board[Block(blockNumber, coor)] = [blockNumber]
        '''

    ## Finds index of block with that coor
    def findBlockWithCoor(self,coor):
        #arrBoard = list(self.board.keys())
        arrBoard = self.board
        for i in range(len(arrBoard)):
            currBlock = arrBoard[i]
            if(arrBoard[i].getCoor() == coor):
                return i
        return None

    ## convert board to tuple 
    def buildListOfTupleBoard(self):
        arr = []
        #grid = list(self.board.items())
        grid = self.board
        for item in grid:
            arr.append(toTuple(item))
        return arr

    ## Add character
    def addChar(self, coor):
        charInd = self.findBlockWithCoor(coor)
        self.board[charInd].setChar()
        #arr = list(self.board[charBlock]).copy()
        ##arr.append("X")
        #del self.board[charBlock]
        #self.board[Block(1,coor)] = arr
        
        

def toTuple(item):
    block = item
    if block.getChar() == True:
        return (block.getCoor(), "X")
    else:
        return (block.getCoor(), block.getNumBlocks())