a = [1, 2, 3]
b = [1, 2, 3]
# print(a == b)  # True
# print(a is b)  # False

x=5
y=5
print(x==y) # True
print(x is y) # True

# For mutable objects such as lists and dictionaries, is and == can behave differently.
# In general, you should use == when you want to compare the values of two objects, 
# and use is when you want to check if two objects are the same object in memory.