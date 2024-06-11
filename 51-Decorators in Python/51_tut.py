 #****************************************************************************************
 #***                                                                                  ***
 #***  Date: 17/8/2023  Time: 9:30 Pm     Author:  Shiraz Mazhar                       ***
 #***                                                                                  ***
 #***  Working On : Decorators in Python                                               ***
 #***                                                                                  ***
 #****************************************************************************************



def greet(fx):
  def mfx(*args, **kwargs):
    print("Good Morning")
    fx(*args, **kwargs)
    print("Thanks for using this function")
  return mfx

@greet
def hello():
  print("Hello world")

@greet
def add(a, b):
  print(a+b)
  
# greet(hello)()
hello()
# greet(add)(1, 2)
add(1, 2)

