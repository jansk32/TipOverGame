from block import Block

EMPTY = "[0]"
'''
        for i in range(0,6):
            arr = []
            for j in range(0,6):
                arr.append(self.board[(i,j)])
            print(i, arr)
'''
class Board:
    
    def __init__(self):
        self.board = {}
        #self.charCoor = charCoor
        self.start = (0,0)
        self.finish = (3,4)
    
    def build_empty_board(self):
        init_board = {}
        for i in range(0,6):
            for j in range(0,6):
                b = Block(0, (i,j))
                init_board[b] = EMPTY
        self.board = init_board

    def print_board(self):
        grids = sorted(self.buildListOfTupleBoard())
        string = ""
        for i in range(len(grids)):
            string += str(grids[i][1])
            if i % 6 == 5:
                string += "\n"
            else:
                string += " "
        print(string)
       
    def setUp(self, blockNumber, coor):
        ## This is to give coordinates new elements or blocks
        ## ONLY if they have a [0]
        delBlock = self.findBlockWithCoor(coor)
        if self.board[delBlock] == "[0]":
            del self.board[delBlock]
        else:
            return
        self.board[Block(blockNumber, coor)] = [blockNumber]


    def findBlockWithCoor(self,coor):
        ## Keep in mind board is a Dictionary of [0]
        ## Convert dictionary keys into a list, delete fro there
        arrBoard = list(self.board.keys())
        for i in range(len(arrBoard)):
            currBlock = arrBoard[i]
            if(arrBoard[i].getCoor() == coor):
                return arrBoard[i]
        return None

    def buildListOfTupleBoard(self):
        arr = []
        grid = list(self.board.items())
        for item in grid:
            arr.append(toTuple(item))
        return arr

def toTuple(item):
    (block, val) = item
    return (block.getCoor(), val)