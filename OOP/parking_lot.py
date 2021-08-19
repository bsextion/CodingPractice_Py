from enum import Enum
#Car enters and gets a ticket
#Car parks in space
#System updates parking spots
#Cae exits and gives ticket, they see total and pay


class VehicleType(Enum):
    motorcycle, compact, large = 1,2,3

class Vehicle:
    def __init__(self, type,handicapped, status=None):
        self.handicapped = handicapped
        self.status = status
        self.type = type

    def park(self, parkingSpot):
        self.status = "Parked"
        pass

    def leave(self,):
        self.status = "N/A"
        pass

class Car(Vehicle):
    def __init__(self, type, handicapped):
        super().__init(self,type,handicapped,VehicleType.compact)

class Motorcycle(Vehicle):
    def __init__(self, type, handicapped):
        super().__init(self,type,handicapped,VehicleType.motorcycle)


class Large(Vehicle):
    def __init__(self, type, handicapped):
        super().__init(self,type,handicapped,VehicleType.large)

class System():
    def printTicket(self, vehicle_type):
        pass

    def takeTicket(self, ticket):
        self.calculatePrice(self, ticket)
        pass


    def calculatePrice(self, ticket):
        pass

class Customer():
    def __init__(self, name, email, vehicle):
        self.name = name
        self.email = email
        self.vehicle = vehicle

class Ticket():
    def __init__(self, customer, time):
        self.customer = customer
        self.time = time

class ParkingGarage():
    def __init__(self, name, spaces):
        self.name = name
        self.spaces = spaces
        self.levels = []


class ParkingLevel():
    def __init__(self, level):
        self.level = level
        self.spaces = 100


class ParkingSpot():
    def __init__(self, level):
        self.level = level
        occupied = False


#Parking Spot
#parking level
#occupied?


#Vehicle
#Vehcicletype
#handicapped
#status
#park()

#System
#print ticket
#take ticket
#calculate price


#Customer
#name
#address
#Vehicle


#Ticket
#customer
#time

#Parking Garage
#name
#spaces

#Parking Level
#level
#garage
#aviable