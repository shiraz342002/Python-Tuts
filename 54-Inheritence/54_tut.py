 #****************************************************************************************
 #***                                                                                  ***
 #***  Date: 18/8/2023  Time: 10:46 Am     Author:  Shiraz Mazhar                      ***
 #***                                                                                  ***
 #***  Working On : Inheritence in Python                                              ***
 #***                                                                                  ***
 #****************************************************************************************

class Department:                   # Base Class
    def __init__(self,depname,depid):
        self.depname=depname
        self.depid=depid
    
    def depshow(self):                # Base class methdos
        print(f"Dep name is :{self.depname}\nDep Id is :{self.depid}")

    @property
    def get_depname(self):          # getters
        return self.depname
    
    @get_depname.setter
    def set_depname(self, new_depname):
        self.depname = new_depname
    
    @property
    def get_depid(self):
        return self.depid

    @get_depid.setter               # setters
    def set_depid(self, new_depid):
        self.depid = new_depid



class section(Department):          # Derived Class
    def __init__(self, depname, depid, secname, secid):
        self.secname = secname
        self.secid = secid  
        Department.__init__(depname, depid)  # Calling Base class __init__ function
        
    @property
    def get_secname(self):
        return self.secname
    
    @get_secname.setter
    def set_secname(self,secname):
        self.secname=secname
        
    @property
    def get_secid(self):
        return self.secid
    
    @get_secid.setter
    def set_secname(self,secid):
        self.secid=secid
    
    def display_all_data(self):
        print("Department Name:", self.get_depname)
        print("Department ID:", self.get_depid)
        print("Section Name:", self.get_secname)
        print("Section ID:", self.get_secid)
        
d1= Department("Computer Science",23)
d1.depshow()
s2=section("Software Eng",55,"Section WTF",399)
print("-------------------------AFTER ALL THE BULL SHIT-------------------------- ")
s2.display_all_data()


