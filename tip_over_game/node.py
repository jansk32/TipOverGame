
class Node:
    
    def __init__(self, bloc):
        self.block = bloc
        self.f = self.g = self.h = 0
    
    #### GETTERS AND SETTERS ######
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