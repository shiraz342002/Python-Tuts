 #****************************************************************************************
 #***                                                                                  ***
 #***  Date: 18/8/2023  Time: 12:42 Pm     Author:  Shiraz Mazhar                      ***
 #***                                                                                  ***
 #***  Working On :  Access Modifiers                                                  ***
 #***                                                                                  ***
 #****************************************************************************************

#Double underscore laga diya to variables access nhi kar saqty mangling hojate ha or wo private banta ha 
#single underscore se protected banta or wo kahin bhi access hojata ha 

# Protected Variables and Methods: By convention, attributes and methods that are intended to be "protected" within a class are prefixed 
# with a single underscore. This indicates that they are meant to be used only within the class and its subclasses, but they can still be accessed 
# from outside if needed.

class MyClass:
    def __init__(self):
        self._protected_var = 23
    
    def _protected_method(self):
        return "This is a protected method"


# Public Variables and Methods: These are accessible from anywhere, both inside and outside the class. 
# They are typically named in lowercase or lowercase with underscores (snake_case).

class MyClass:
    def __init__(self):
        self.__private_var = 10
    
    def __private_method(self):
        return "This is a private method"


