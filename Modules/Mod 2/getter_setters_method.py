class User:
    def __init__(self, username=None, password = None):  # defining initializer
        self.username = username
        self.__password = password

    def setUsername(self, username):
        self.__username = username

    def getUsername(self):
        return self.__username

    def setPassword(self, password):
        self.__password = password

    def getPassword(self):
        return self.__password

    def login(self, userName, password):
        if self.username == userName and self.__password == password:
            print("Access Granted!")
        else:
            print("Wrong Credentials")


Brooke = User("Brooke", "25Badger")
Brooke.login("Brooke", "25Badger")

