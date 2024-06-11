 #****************************************************************************************
 #***                                                                                  ***
 #***  Date: 19/8/23  Time: 5:44 Pm     Author:  Shiraz Mazhar                         ***
 #***                                                                                  ***
 #***  Working On : Static Methods in Python                                           ***
 #***                                                                                  ***
 #****************************************************************************************
 
 
class Hello:
    def __init__(self,num):
        self.num=num
    @staticmethod  # basically static method me self ka use nhi hota uske baghair hi kaam chal jata ha 
    def add(a,b):
        return a+b
    
    def mul(self,x,y):
        return self.x*self.y
    
    @staticmethod
    def min(m,n):
        return m-n
    
obj=Hello(6)
print(obj.add(5,6))
# print(obj.mul(2,2))
print(obj.min(6,3))
