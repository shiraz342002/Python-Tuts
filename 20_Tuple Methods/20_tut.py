
# Tuples are immutable, hence if 
# you want to add, remove or change tuple items, 
# then first you must convert the tuple to a list.
# Then perform operation on that list 
# and convert it back to tuple.
countries = ("Spain", "Italy", "India", "England", "Germany")
temp = list(countries)
temp.append("Russia")       #add item 
temp.pop(3)                 #remove item
temp[1] = "Finland"         #change item
countries = tuple(temp)
print(countries)

## We can also concatenate two tuples to add more items in it
# countries = ("Pakistan", "Afghanistan", "Bangladesh", "SriLanka")
# countries2 = ("Vietnam", "India", "China")
# southEastAsia = countries + countries2
# print(southEastAsia)

##Count Method
Tuple1 = (0, 1, 2, 3,69, 2, 3, 1, 3, 2)
res1 = Tuple1.count(69)
print('Count of 69 in Tuple1 is:', res1)
res2=Tuple1.index(69)
print(res2)
print("The Length of tuple is :",len(Tuple1)) 

#You can use all list methods by converting the tuple to list and then convert it back to tuple.