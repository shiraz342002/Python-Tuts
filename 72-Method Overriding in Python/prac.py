class Vehicle:
    def display_info(self):
        pass

class Car(Vehicle):
    def __init__(self, make, model):
        self.make = make
        self.model = model
    
    def display_info(self):
        print(f"Car: {self.make} {self.model}")

class Motorcycle(Vehicle):
    def __init__(self, brand):
        self.brand = brand
    
    def display_info(self):
        print(f"Motorcycle: {self.brand}")

car = Car("Toyota", "Corolla")
motorcycle = Motorcycle("Harley Davidson")

car.display_info()
motorcycle.display_info()
