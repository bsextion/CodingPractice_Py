class Employee:
    teamName = 'GDPS'  # class variable
    # formerJobs = [] #wrong use
    teamMembers = []

    def __init__(self, name, id=0, salary=0):
        self.name = name  # instance variable
        self.id = id
        self.salary = salary
        self.formerJobs = []
        self.teamMembers.append(self.name)


Brooke = Employee("Brooke")
Phil = Employee("Phillip")
Brooke.formerJobs.append("Infosys")
Phil.formerJobs.append("N/A")

print(Brooke.name)
print(Phil.name)
print(Brooke.teamName)
print(Phil.teamName)
print(Brooke.formerJobs)
print(Phil.formerJobs)
print(Phil.teamMembers)




