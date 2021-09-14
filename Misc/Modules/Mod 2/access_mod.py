
class Employee:
    def __init__(self, ID, salary):
        # all properties are public
        self.ID = ID
        self.__salary = salary

    def displayDetails(self):
        print("ID:", self.ID)


    def displayMonthly(self):
        print("Monthly Salary: ",  self.__salary * 30)


Steve = Employee(3789, 2500)
Steve.displayMonthly()
print(Steve._Employee__salary)
