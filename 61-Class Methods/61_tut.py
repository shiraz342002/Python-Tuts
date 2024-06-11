 #****************************************************************************************
 #***                                                                                  ***
 #***  Date: 21/8/2023  Time: 11:35 Pm     Author:  Shiraz Mazhar                      ***
 #***                                                                                  ***
 #***  Working On : Class Methods                                                      ***
 #***                                                                                  ***
 #****************************************************************************************

# class methods decorator lagane se class ke variables ke values change hojatin na sirf instance ki
class Employee:
  company = "Apple"
  def show(self):
    print(f"The name is {self.name} and company is {self.company}")

  @classmethod
  def changeCompany(cls, newCompany): # cls represents the class itself.
    cls.company = newCompany


e1 = Employee()
e1.name = "Harry"
e1.show()
e1.changeCompany("Tesla")
e1.show()
print(Employee.company)
