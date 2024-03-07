from CarInventoryNode import CarInventoryNode
from Car import Car

class CarInventory:
    def __init__(self):
        self.root = None
    def addCar(self, car):
        if self.root:
            self._addCar(self.root, car)
        else:
            self.root = CarInventoryNode(car)
    def _addCar(self, node, car):
        if (node.make == car.make) and (node.model == car.model):
            node.cars.append(car)
        elif car < node.cars[0]:
            if node.left == None:
                new_node = CarInventoryNode(car)
                new_node.setParent(node)
                node.setLeft(new_node)
            else:
                self._addCar(node.left, car)
        else:
            if node.right == None:
                new_node = CarInventoryNode(car)
                new_node.setParent(node)
                node.setRight(new_node)
            else:
                self._addCar(node.right, car)
    def doesCarExist(self, car):
        return self._doesCarExist(self.root, car)
    def _doesCarExist(self, node, car):
        if node == None:
            return False
        elif (node.make == car.make) and (node.model == car.model):
            for c in node.cars:
                if c == car:
                    return True
            return False
        elif car < node.cars[0]:
            return self._doesCarExist(node.left, car)
        else:
            return self._doesCarExist(node.right, car)
    def inOrder(self):
        return self._inOrder(self.root)
    def _inOrder(self, node):
        if node != None:
            return self._inOrder(node.left) + str(node) + self._inOrder(node.right)
        return ''
    def preOrder(self):
        return self._preOrder(self.root)
    def _preOrder(self, node):
        if node != None:
            return str(node) + self._preOrder(node.left) + self._preOrder(node.right)
        return ''
    def postOrder(self):
        return self._postOrder(self.root)
    def _postOrder(self, node):
        if node is not None:
            return self._postOrder(node.left) + self._postOrder(node.right) + str(node)
        return ''
    def getBestCar(self, make, model):
        return self._getBestCar(self.root, make, model)
    def _getBestCar(self, node, make, model):
        if node is not None:
            if make.upper() == node.make and model.upper() == node.model:
                if node.cars:
                    cars = node.cars
                    cars.sort(reverse=True)
                    return cars[0]
            elif make.upper() < node.make or (make.upper() == node.make and model.upper() < node.model):
                return self._getBestCar(node.left, make, model)
            else:
                return self._getBestCar(node.right, make, model)
        return None
    def getWorstCar(self, make, model):
        return self._getWorstCar(self.root, make, model)
    def _getWorstCar(self, node, make, model):
        if node is not None:
            if make.upper() == node.make and model.upper() == node.model:
                if node.cars:
                    cars = node.cars
                    cars.sort()
                    return cars[0]
            elif make.upper() < node.make or (make.upper() == node.make and model.upper() < node.model):
                return self._getWorstCar(node.left, make, model)
            else:
                return self._getWorstCar(node.right, make, model)
        return None
    def getTotalInventoryPrice(self):
        return self._getTotalInventoryPrice(self.root)
    def _getTotalInventoryPrice(self, node):
        if node:
            sum = 0
            for car in node.cars:
                sum += car.price
            return self._getTotalInventoryPrice(node.left) + sum + self._getTotalInventoryPrice(node.right)
        else:
            return 0
    def getSuccessor(self, make, model):
        carToSearch = Car(make, model, 0, 0)
        target_node = self._get(carToSearch, self.root)
        if target_node is None:
            return None
        if target_node.hasRightChild():
            return target_node.right.findMin()
        current_node = target_node
        while current_node.parent and current_node == current_node.parent.right:
            current_node = current_node.parent
        if current_node.parent:
            return current_node.parent.cars[0] if current_node.parent.cars else None
        else:
            return None

    def _get(self, car, node):
        if not node:
            return None
        elif (node.make == car.make) and (node.model == car.model):
            return node
        elif car < CarInventoryNode(node):
            return self._get(car, node.left)
        else:
            return self._get(car, node.right)

    def removeCar(self, make, model, year, price):
        car = Car(make, model, year, price)
        node = self._get(car, self.root)

        if node is None:
            return False

        for c in node.cars:
            if c.year == year and c.price == price:
                node.cars.remove(c)
                if not node.cars:
                    self._removeNode(node)

                return True

        return False

    def _removeNode(self, node):
        if node.isLeaf():
            
            if node.isLeftChild():
                node.parent.left = None
            else:
                node.parent.right = None

        elif node.hasBothChildren():
            
            successor = node.right.findMin()
            self._removeNode(successor)  
            node.replaceNodeData(successor.make, successor.model, successor.cars, successor.left, successor.right)

        else:
            child = node.left if node.hasLeftChild() else node.right

            if node.isLeftChild():
                node.parent.left = child
            else:
                node.parent.right = child

            child.parent = node.parent
        

