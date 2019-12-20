from direction import Direction
from character import Character
from board import Board
from node import Node
import copy
'''
// A* (star) Pathfinding
// Initialize both open and closed list
let the openList equal empty list of nodes
let the closedList equal empty list of nodes
// Add the start node
put the startNode on the openList (leave it's f at zero)
// Loop until you find the end
while the openList is not empty
    // Get the current node
    let the currentNode equal the node with the least f value
    remove the currentNode from the openList
    add the currentNode to the closedList
    // Found the goal
    if currentNode is the goal
        Congratz! You've found the end! Backtrack to get path
    // Generate children
    let the children of the currentNode equal the adjacent nodes
    
    for each child in the children
        // Child is on the closedList
        if child is in the closedList
            continue to beginning of for loop
        // Create the f, g, and h values
        child.g = currentNode.g + distance between child and current
        child.h = distance from child to end
        child.f = child.g + child.h
        // Child is already in openList
        if child.position is in the openList's nodes positions
            if the child.g is higher than the openList node's g
                continue to beginning of for loop
        // Add the child to the openList
        add the child to the openList
'''
class Player:
    def __init__(self, boardObj):
        self.char = None
        self.boardObj = boardObj
    
    def astar(self, boardObj):
        dir = Direction.DOWN

        ## Start State
        startCoor = self.getCharBlock(boardObj).getCoor()
        startNode = Node(startCoor, None, boardObj)

        ## Finish State
        finishCoor = self.getFinishBlock(boardObj).getCoor()
        finishNode = Node(finishCoor,finishCoor, boardObj)


        open_list = []
        closed_list = []

        open_list.append(startNode)


        while len(open_list) > 0:
            # Set current coordinate
            currNode = open_list[0]
            currNodeInd = 0
            for s in range(len(open_list)):
                if open_list[s].getF() < open_list[currNodeInd].getF():
                    currNode = open_list[s]
                    currNodeInd = s

            
            # Pop the currNode out of the open list into closed
            closed_list.append(currNode)
            open_list.pop(currNodeInd)
            
            # If currNode is the finish block
            currBlockInd = boardObj.findBlockWithCoor(currNode.getCurr())
            currBlock = boardObj.board[currBlockInd]
#            print(currBlock.getFinish())
            if currBlock.getFinish() == True:
#                print("Finished")
                nextStepNode = backTrack(currNode, startNode, closed_list)
#                print("Made decision")
                dir = nextStepNode.direction
                return dir

            # Generate children
            tmpBoardObj = copy.deepcopy(boardObj)
            
            children = currNode.generateStates()
#            print("CURRENT:",currNode.getCurr())
#            if currNode.getPrev() != None:
#                print("PREVIOUS:", currNode.getPrev().getCurr())
            currNode.boardObj.print_board()
            for node in children:
#                print(node.getCurr())
                isStuck = 0
                # Stop the nodes that are the same
                if node.getCurr() == node.getPrev().getCurr():
                    isStuck = 999

                if node in closed_list:
                    continue
                node.setG(heuristics(currNode, node))
                node.setH(isStuck + heuristics(node, finishNode))
                node.setF(node.getG() + node.getH())

                ## if child is in open_list
                for olist in  open_list:
                    if node.getCurr() == olist.getCurr():
                        if node.getG() > olist.getG():
                            continue

                ## Add child to open_list 
                open_list.append(node)
#            print("######################")

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
    
# Heuristics
def heuristics(node1, node2):
    (x1,y1) = node1.getCurr()
    (x2,y2) = node2.getCurr()

    distance = abs(x1-x2) + abs(y1-y2)

    return distance
 

# Back track function
def backTrack(finalNode, startNode, closedList):
    currPointer = finalNode.getPrev()
    if currPointer.getPrev() == None:
        return finalNode
    else:
        while currPointer.getPrev() != startNode:
            currPointer = currPointer.getPrev()

    return currPointer