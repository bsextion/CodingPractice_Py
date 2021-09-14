class Vehicle:
    fuelMax = 90
    def __init__(self, make, model, color):
        self.make = make
        self.model = model
        self.color = color

    def printDetails(self):
        print(self.make)
        print(self.model)
        print(self.color)

    def turnOnVehicle(self):
        print("Stopping vehicles...")

class Truck(Vehicle):
    def __init__(self, make=None, model=None, color=None):
        super().__init__(make,model,color)

    def getTruckDetails(self):
        super().printDetails();

class Car(Vehicle):
    fuelMax = 50
    def __init__(self, make, model, color, doors):
        # Vehicle.__init__(self,make, model, color)
        super().__init__(make, model, color)
        self.doors = doors

    def printCarDetails(self):
        # self.printDetails()
        super().printDetails()
        print("Cap for vehicles ", super().fuelMax)
        print(self.doors)

    def startCar(self):
        print("Starting car...")

class Hybrid(Car):
    def __init__(self, make=None, model=None, color=None, doors=0):
        super().__init__(make, model,color,doors)
    def turnOnHybrid(self):
        print("Turning On...")

class CombustionEngine():
    def setTankCapacity(self, tankCapacity):
        self.tankCapacity = tankCapacity


class ElectricEngine():
    def setChargeCapacity(self, chargeCapacity):
        self.chargeCapacity = chargeCapacity

# Child class inherited from CombustionEngine and ElectricEngine
class HybridEngine(CombustionEngine, ElectricEngine):
    def printDetails(self):
        print("Tank Capacity:", self.tankCapacity)
        print("Charge Capacity:", self.chargeCapacity)
# Lexus = Car("Lexus", "UX", "Black", 4)
# Lexus.startCar()

# LexusHyb = Hybrid()
# LexusHyb.turnOnHybrid()

Ford = Truck()
Ford.getTruckDetails()
