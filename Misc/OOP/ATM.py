
from enum import Enum
import random
from abc import ABC, abstractmethod

#Customer inserts card
#ATM reads card
#ATM displays account information
#ATM provides a list of options
#Customer picks option
#Customer takes card
#ATM reset screen


class AccountType(Enum):
    SAVINGS, CHECKINGS = 1,2

class AccountStatus(Enum):
    ACTIVE, INACIVE = 1,2

class Account:
    def __init__(self, customer, type):
        self.customer = customer
        self.__accountnumber = random.randint(1000,9999)
        self.type = type
        self.balance = 100
        self.status = AccountStatus.ACTIVE

    def getAccountNumber(self):
        return self.__accountnumber

    def depositAmount(self, amount):
        self.balance += amount

    def withdrawAmount(self, amount):
        self.balance -= amount


class SavingsAccount:
    def __init__(self, customer, type):
        super().init(customer)

    def calculateInterest(self):
        interest = self.balance * 0.2
        return self.balance


class CheckingsAccount:
    def __init__(self, customer, type):

        super().init(customer, AccountType.CHECKINGS)


class AccountFactory:
    def createAccount(self, type, customer):
        if type == "savings"
            return SavingsAccount()




#Card
#number
#account
#customer

#Customer
#[Account]
#Name
#Email


#Account
#number
#type
#balance
#status
#getAccountNumber


#System
#deposit()
#withDraw()
#viewBalance()
#readCard()

