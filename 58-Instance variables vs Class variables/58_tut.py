 #****************************************************************************************
 #***                                                                                  ***
 #***  Date: 19/8/2023  Time: 7:00 Pm     Author:  Shiraz Mazhar                       ***
 #***                                                                                  ***
 #***  Working On :  Instance variables vs Class variables                             ***
 #***                                                                                  ***
 #****************************************************************************************

# basically class variables class ke andar define hote or sab instances ke liye hote hen
# jabke instance variables jo hen wo kisi specefic object ke hisab se modify hote hen 

#yahan instance object ko keh rahe hen btw : )

class Employee:
  companyName = "Apple"
  noOfEmployees = 0
  def __init__(self, name):
    self.name = name
    self.raise_amount = 0.02
    Employee.noOfEmployees +=1
  def showDetails(self):
    print(f"The name of the Employee is {self.name} and the raise amount in {self.noOfEmployees} sized {self.companyName} is {self.raise_amount}")

# Employee.showDetails(emp1)
emp1 = Employee("Harry")
emp1.raise_amount = 0.3
emp1.companyName = "Apple India" 
emp1.showDetails()
Employee.companyName = "Google"
print(Employee.companyName)

emp2 = Employee("Rohan")
emp2.companyName = "Nestle"
emp2.showDetails()
