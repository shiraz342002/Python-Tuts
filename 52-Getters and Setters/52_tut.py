 #****************************************************************************************
 #***                                                                                  ***
 #***  Date: 17/8/2023  Time: 9:28 Pm     Author:  Shiraz Mazhar                       ***
 #***                                                                                  ***
 #***  Working On : Getters & Setters                                                  ***
 #***                                                                                  ***
 #****************************************************************************************
class Student:
    name="Shiraz"
    Age="20"
    cgpa="3.5"

    def __init__(self,Age,cgpa):
        self.Age=Age
        self.cgpa=cgpa

        
    @property
    def get_name(self):
        return self.name
    
    @get_name.setter
    def set_name(self,n):
        self.name=n

    def show(self):
        print(f"Your name is {self.name}, Your age is {self.Age} and your csgpa is {self.cgpa}")


s1 = Student(69,2.1)
s1.name="Abdul Sattar"
s1.show()