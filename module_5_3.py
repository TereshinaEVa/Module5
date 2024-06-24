class Building:
    def __init__(self, numberOfFloors, buildingType ):
        self.numberOfFloors = numberOfFloors
        self.buildingType = buildingType

    def __eq__(self, other):
        return self.numberOfFloors == other.numberOfFloors and self.buildingType == other.buildingType

house_old = Building(5, 'Пятиэтажка')
house_new = Building(10, 'Десятиэтажка')
house_old_new = Building(5, 'Пятиэтажка')

print(house_old == house_new)
print(house_old == house_old_new)