class Dog:
    def Speak(self):
        print("Bark")

class Cat:
    def Speak(self):
        print("Meow")

class AnimalSound:
    def Sound(self, animal):
        animal.Speak()


sound = AnimalSound()
dog = Dog()
cat = Cat()

sound.Sound(dog)
sound.Sound(cat)