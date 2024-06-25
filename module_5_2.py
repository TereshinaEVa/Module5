class House:
    def __init__(self):
        self.number_OfFloors = 0

    def setNewNumberOfFloors(self, floors):
        self.number_OfFloors = floors
        print(self.number_OfFloors)

H1 = House()
H1.setNewNumberOfFloors(5)
H1.setNewNumberOfFloors(6)
