class Animal:
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        print("Dog making sound")

class Cat(Animal):
    def make_sound(self):
        print("Cat making sound")

for a in [Dog(), Cat()]:
    a.make_sound()