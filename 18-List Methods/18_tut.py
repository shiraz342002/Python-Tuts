## List Methods IN Python
fruits=["Apple","Bannana","Apricot","Grapes","Mango","Orange"]
num=[5,1,3,9,2,19,5]
print("Before")
print(fruits)
print(num)
print(len(fruits)) # prints length of list
print(type(fruits)) # print the type 
fruits.append("Guava") # To add more items
# num.sort() # will sort the items
fruits.reverse() # Will reverse the order of items
print("9 is present at index no :",num.index(9))# will print the index of given item
print(num.count(5))# Will give how much time an item is present in the list
fruits.insert(1,"Pineapple") # Can insert values at certrain index
num.extend(fruits)












print("After")
print(num)
print(fruits)