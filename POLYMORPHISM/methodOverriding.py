class animal:
    def sound(self):
        print("Animals Sound")
class Dog(animal):
    def sound(self):
        print("Bark Bark...")
        super().sound()
class Cat(animal):
    def sound(self):
        print("Meow Meow...")
        super().sound()
c=Cat()
c.sound()
#d=Dog()
#d.sound()
#an=animal()
#an.sound()
#USE OF SUPER METHOD TO ACESS PARENT FUNCTION