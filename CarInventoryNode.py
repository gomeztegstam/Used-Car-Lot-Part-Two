from Car import Car

class CarInventoryNode:
    def __init__(self, car):
        self.make = car.make.upper()
        self.model = car.model.upper()
        self.cars = [car]
        self.parent = None
        self.left = None
        self.right = None
    def getMake(self):
        return self.make
    def getModel(self):
        return self.model
    def getParent(self):
        return self.parent
    def setParent(self, parent):
        self.parent = parent
    def getLeft(self):
        return self.left
    def setLeft(self, left):
        self.left = left
    def getRight(self):
        return self.right
    def setRight(self, right):
        self.right = right
    def __str__(self):
        car_string = ''
        for car in self.cars:
            car_string += str(car) + '\n'
        return car_string
    def hasLeftChild(self):
        return self.left 
    def hasRightChild(self):
        return self.right
    def isLeftChild(self):
        return self.parent and self.parent.left == self
    def isRightChild(self):
        return self.parent and self.parent.right == self
    def isRoot(self):
        return not self.parent
    def isLeaf(self):
        return not (self.right or self.left)
    def hasAnyChildren(self):
        return self.right or self.left
    def hasBothChildren(self):
        return self.right and self.left
    def replaceNodeData(self,make,model,cars,lc,rc):
        self.make = make
        self.model = model
        self.cars = cars
        self.left = lc
        self.right = rc
        if self.hasLeftChild():
            self.left.parent = self
        if self.hasRightChild():
            self.right.parent = self
    def findMin(self):
        current = self
        while current.hasLeftChild():
            current = current.left
        return current
    def spliceOut(self):
        if self.isLeaf():
            if self.isLeftChild():
                self.parent.left = None
            else:
                self.parent.right = None
        elif self.hasAnyChildren():
            if self.hasRightChild():
                if self.isLeftChild():
                    self.parent.left = self.right
                else:
                    self.parent.right = self.right
                self.right.parent = self.parent
        
            
    
