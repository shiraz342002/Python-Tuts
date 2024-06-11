 #****************************************************************************************
 #***                                                                                  ***
 #***  Date: 29/8/2023  Time: 5:54 Pm     Author:  Shiraz Mazhar                       ***
 #***                                                                                  ***
 #***  Working On :  Operator Overloading in Python                                    ***
 #***                                                                                  ***
 #****************************************************************************************


class Vector:
  def __init__(self, i, j, k):
    self.i = i
    self.j = j
    self.k = k

  def __str__(self):
    return f"{self.i}i + {self.j}j + {self.k}k"

  def __add__(self, x):
    return Vector(self.i + x.i,  self.j+x.j, self.k+x.k) 
v1 = Vector(3, 5, 6)
print(v1)

v2 = Vector(1, 2, 9)
print(v2)

print(v1 + v2)
print(type(v1 + v2))

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)
    
c1= Point(5,8)
print(c1.__add__)