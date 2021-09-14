class Employee:
    location = 'Austin'

    # defining the initializer
    def __init__(self, ID=None, salary=None, department=None):
        self.ID = ID
        self.salary = salary
        self.department = department

    def demo(self,a,b,c,d=5,e=None): # implicit method overloading
        print("a=", a)
        print("b=", b)
        print("c=", c)
        print("d=", d)
        print("e=", e)

    @classmethod
    def getLocation(cls):
        return cls.location

    @staticmethod
    def details(eyecolor, haircolor):
        return eyecolor + " " + haircolor

    def tax(self):
        return (self.salary * 0.2)

    def salaryPerDay(self):
        return (self.salary // 30)


# initializing an object of the Employee class
# Steve = Employee(3789, 2500, "Human Resources")
#
# # Printing properties of Steve
# print("ID =", Steve.ID)
# print("Salary", Steve.salary)
# print("Department:", Steve.department)
# print("Tax paid by Steve:", Steve.tax())
# print("Salary per day of Steve", Steve.salaryPerDay())
hair = "Black"
eye = "Blue"

print(Employee.details(hair, eye))
