 #****************************************************************************************
 #***                                                                                  ***
 #***  Date: 12/9/2023  Time: 3:28 Pm     Author:  Shiraz Mazhar                       ***
 #***                                                                                  ***
 #***  Working On : Single Inheritance                                                 ***
 #***                                                                                  ***
 #****************************************************************************************

class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        
    def make_sound(self):
        print("Sound made by the animal")

class Dog(Animal):
    def __init__(self, name, breed):
        super.__init__(self, name, species="Dog")
        self.breed = breed
        
    def make_sound(self):
        print("Bark!")
        
class Cat(Animal):
    def __init__(self, name, breed):
        super().__init__(name, species="Cat")
        self.breed = breed  
        self.name=name                           
        
    def cat_speaks():
            print("Meeow")
    
    
    
d = Dog("Dog", "Doggerman")
d.make_sound()

a = Animal("Dog", "Dog")
a.make_sound()

c = Cat()
c.make_sound()
c.cat_speaks("Bilu","russian")
