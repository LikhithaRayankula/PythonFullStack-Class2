class Vehicle:
    def navigate(self):
        pass

class Car(Vehicle):
    def navigate(self):
        print('navigate via car')

class Bicycle(Vehicle):
    def navigate(self):
        print('navigate via bicycle')

for v in [Car(), Bicycle()]:  #Insted of creating objects separetely, we use for loop
    v.navigate()

v=Car()    # This is another method
v.navigate()

v=Bicycle()
v.navigate()