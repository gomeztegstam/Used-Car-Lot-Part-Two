from Car import Car
from Car import Car
from CarInventoryNode import CarInventoryNode
from CarInventory import CarInventory


def test_car():
    c1 = Car("Honda", "CRV", 2007, 8000)
    c2 = Car("Toyota", "Camry", 2010, 12000)
    assert c1 > c2
    assert c2 < c1

def test_car_inventory_node():
    car1 = Car("Dodge", "dart", 2015, 6000)
    car2 = Car("dodge", "DaRt", 2003, 5000)
    carNode = CarInventoryNode(car1)
    carNode.cars.append(car2)
    assert carNode.getMake() == "DODGE"
    assert carNode.getModel() == "DART"
    assert carNode.getParent() is None
    assert carNode.getLeft() is None
    assert carNode.getRight() is None

def _testCarInventory():
    bst = CarInventory()
    car1 = Car("Nissan", "Leaf", 2018, 18000)
    car2 = Car("Tesla", "Model3", 2018, 50000)
    car3 = Car("Mercedes", "Sprinter", 2022, 40000)
    car4 = Car("Mercedes", "Sprinter", 2014, 25000)
    car5 = Car("Ford", "Ranger", 2021, 25000)
    bst.addCar(car1)
    bst.addCar(car2)
    bst.addCar(car3)
    bst.addCar(car4)
    bst.addCar(car5)
    assert bst.doesCarExist(car1)
    assert not bst.doesCarExist(Car("Toyota", "Camry", 2010, 12000))
    assert bst.getBestCar("Nissan", "Leaf") == car1
    assert bst.getBestCar("Mercedes", "Sprinter") == car3
    assert bst.getBestCar("Honda", "Accord") is None
    assert bst.getWorstCar("Nissan", "Leaf") == car1
    assert bst.getWorstCar("Mercedes", "Sprinter") == car4
    assert bst.getWorstCar("Honda", "Accord") is None
    assert bst.getTotalInventoryPrice() == 158000
    assert bst.inOrder() == \
        """\
        Make: FORD, Model: RANGER, Year: 2021, Price: $25000
        Make: MERCEDES, Model: SPRINTER, Year: 2022, Price: $40000
        Make: MERCEDES, Model: SPRINTER, Year: 2014, Price: $25000
        Make: NISSAN, Model: LEAF, Year: 2018, Price: $18000
        Make: TESLA, Model: MODEL3, Year: 2018, Price: $50000
        """

    assert bst.preOrder() == \
        """\
        Make: NISSAN, Model: LEAF, Year: 2018, Price: $18000
        Make: MERCEDES, Model: SPRINTER, Year: 2022, Price: $40000
        Make: MERCEDES, Model: SPRINTER, Year: 2014, Price: $25000
        Make: FORD, Model: RANGER, Year: 2021, Price: $25000
        Make: TESLA, Model: MODEL3, Year: 2018, Price: $50000
        """

    assert bst.postOrder() == \
        """\
        Make: FORD, Model: RANGER, Year: 2021, Price: $25000
        Make: MERCEDES, Model: SPRINTER, Year: 2022, Price: $40000
        Make: MERCEDES, Model: SPRINTER, Year: 2014, Price: $25000
        Make: TESLA, Model: MODEL3, Year: 2018, Price: $50000
        Make: NISSAN, Model: LEAF, Year: 2018, Price: $18000
        """
