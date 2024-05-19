class ParkingSystem(object):

    def __init__(self, big, medium, small):
        self.bigSpace = big
        self.midSpace = medium
        self.smallSpace = small
        

    def addCar(self, carType):
        if carType == 3:
            if self.smallSpace > 0:
                self.smallSpace -= 1
                return True
            else:
                return False
        elif carType == 2:
            if self.midSpace > 0:
                self.midSpace -= 1
                return True
            else:
                return False
        elif carType == 1:
            if self.bigSpace > 0:
                self.bigSpace -= 1
                return True
            else:
                return False
        else:
            return False