from abc import abstractmethod, ABC
from enum import Enum
from secrets import choice
import string

class UserType(Enum):
    MEMBER = 1
    EMPLOYEE = 2

class AccountType(Enum):
    CHECKINGS = 1
    SAVINGS = 2

class AccountStatus(Enum):
    OPEN = 1
    CLOSED = 2

class Generator:
    def id_generator(self, array, size=6):
        return ''.join([choice(array) for _ in range(size)])


class Card(Generator):
    def __init__(self, user_id):
        self.number = self.id_generator()
        self.user_id = user_id

    def id_generator(self):
        super().id_generator(string.digits, 8)

class User(Generator):
    def __init__(self, name, password, pin, accounts=[]):
        self.user_id = self.id_generator()
        self.name = name
        self.password = password
        self.accounts = accounts
        self.card = None
        self.pin = pin
        self.giveCard(self.user_id)

    def id_generator(self):
        return super().id_generator(string.digits+string.ascii_uppercase, 8)

    def giveCard(self, card):
        self.card = Card(self.user_id)

    def addBankAccount(self, intial_balance, accountType, password):
        if password == self.password:
            if len(self.accounts) == 2:
                print("You already have a checking and savings account!")
            if len(self.accounts) == 1:
                account = self.accounts[0]
                if account.type == accountType:
                    print("You already have a ", account.type, " account.")
                else:
                    new_account = Account(accountType, 200)
                    self.accounts.append(new_account)

            if len(self.accounts) == 0:
                new_account = Account(intial_balance, accountType)
                self.accounts.append(new_account)
        else:
            print("Incorrect password.")


class Account(Generator):
    def __init__(self, type, balance=0):
        self.account_number = self.id_generator()
        self.balance = balance
        self.active = AccountStatus.OPEN
        self.type = type

    def id_generator(self):
        super().id_generator(string.digits, 9)

class Transaction(ABC):
    @abstractmethod
    def withdraw(self):
        pass
    @abstractmethod
    def deposit(self):
        pass
    @abstractmethod
    def view_balance(self):
        pass

class ATM(Transaction, Generator):
    currentUser = None
    balance = 1000

    def __init__(self, bank):
        self.id = self.id_generator()
        self.bank = bank

    def readCard(self, cardNumber, pin):
        users = list(self.bank.users.values())
        user_found = list(filter(lambda u: u.card.number == cardNumber, users))[0]
        if user_found is None:
            print("You are not a member of this bank.")
        else:
            if user_found.pin == pin:
                self.login(user_found)
            else:
                print("You have entered the incorrect pin.")

    def login(self, user):
        self.currentUser = user

    def logout(self):
        self.currentUser = None
        print("Thank you for your service.")

    def withdraw(self, pin, amount):
        if self.check_pin(pin):
            accounts = self.currentUser.accounts
            if len(accounts) == 0:
                print("You need to open an account.")
            if len(accounts) == 1:
                account = accounts[0]
                self.withdrawAmount(account, amount)
            if len(accounts) == 2:
                answer = input("Which account would you like to withdraw from?")
                if answer == AccountType.CHECKINGS:
                    pass
                elif answer == AccountType.SAVINGS:
                    pass

                else:
                    while answer is not AccountType.SAVINGS or AccountType.CHECKINGS:
                        answer = input("Choose again.")
                        if answer == AccountType.CHECKINGS:
                            pass
                        elif answer == AccountType.SAVINGS:
                            pass
            self.logout()

    def withdrawAmount(self, account, amount):
        if account.balance < amount:
            print("You do not have enough money to withdraw")
        elif amount % 20 != 0:
            print("You must withdraw in increments of $20")
        else:
            account.balance - amount
            self.printReceipt(account)

    def depositAmount(self, account, amount):
        if amount < 10:
            print("You need to deposit at least $10")
        else:
            account.balance + amount
            self.printReceipt(account)

    def printReceipt(self, account: Account):
        print("User: ", self.currentUser)
        print("Current Balance: ", account.balance)

    def deposit(self, pin, amount):
        if self.check_pin(pin):
            accounts = self.currentUser.accounts
            if accounts == 0:
                print("You need to open an account.")
            if accounts == 1:
                account = accounts[0]
                self.depositAmount(account, amount)
            if accounts == 2:
                answer = input("Which account would you like to withdraw from?")
                if answer == AccountType.CHECKINGS:
                    pass
                elif answer == AccountType.SAVINGS:
                    pass
                else:
                    while answer is not AccountType.SAVINGS or AccountType.CHECKINGS:
                        answer = input("Choose again.")
                        if answer == AccountType.CHECKINGS:
                            pass
                        elif answer == AccountType.SAVINGS:
                            pass
            self.logout()

    def view_balance(self, pin):
        if self.check_pin(pin):
            accounts = self.currentUser.accounts
            if accounts == 0:
                print("You need to open an account.")
            if accounts == 1:
                account = accounts[0]
                self.printReceipt(account)
            if accounts == 2:
                answer = input("Which account would you like to withdraw from?")
                if answer == AccountType.CHECKINGS:
                    pass
                elif answer == AccountType.SAVINGS:
                    pass
                else:
                    while answer is not AccountType.SAVINGS or AccountType.CHECKINGS:
                        answer = input("Choose again.")
                        if answer == AccountType.CHECKINGS:
                            pass
                        elif answer == AccountType.SAVINGS:
                            pass
            self.logout()

    def check_pin(self, pin):
        expected = self.currentUser.pin
        return expected == pin

    def id_generator(self):
        return super().id_generator(string.digits, 8)

class Bank:
    def __init__(self, name):
        self.name = name
        self.routing_number = 4242
        self.atms = {}
        self.users = {}

    def addAtm(self):
        atm = ATM(self)
        id = atm.id
        if id not in self.atms:
            self.atms[id] = atm
        return atm

    def createUserAccount(self, name, password, pin):
        user = User(name, password, pin)
        user_id = user.user_id
        if user_id not in self.users:
            self.users[user_id] = user
        return user

    def addAccount(self, user_id, deposit, accountType, password):
        user: User = self.users[user_id]
        user.addBankAccount(deposit,accountType, password)

def main():
    bank = Bank("Chase")
    atm_1 = bank.addAtm()
    atm_2 = bank.addAtm()
    user = bank.createUserAccount("Brooke S", "Hello", 1993)
    bank.addAccount(user.user_id, 50,AccountType.CHECKINGS, "Hello")

    atm_1.readCard(user.card.number, 1993)
    atm_1.withdraw(1993, 50)

if __name__ == "__main__":
    main()

