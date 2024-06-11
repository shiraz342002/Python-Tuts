import pandas as pd # as can be used to shorten the pandas words and now can use pandas fuctions with just pd.()
# from math import sqrt,pi,floor #Can import specefic methods from a package as well
# from pygame import *  # * basically import all possible functions in pygame
import pygame
import math
sq=math.sqrt(9)
print(f"The squaid of 9 is {sq}")

#dir function
# Finally, Python has a built-in function called dir that you can use to view the names of all the functions 
# and variables defined in a module. This can be helpful for exploring and understanding the contents of a new module.
print(dir(math))
print("The Methods in pandas are : ")
# print(dir(pd))

#You can also import methods and attributes from different file ie package
from Shiraz import welcome,crap

welcome()
print(crap)