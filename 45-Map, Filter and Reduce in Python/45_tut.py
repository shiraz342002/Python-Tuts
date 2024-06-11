# In Python, the map, filter, and reduce functions are built-in functions that allow you to apply a function
# to a sequence of elements and return a new sequence. These functions are known as higher-order functions,
# as they take other functions as arguments.

# MAP()
# The map function applies a function to each element in a sequence and
# returns a new sequence containing the transformed elements. 
def avg(om):
    tm=1100
    return ((om/tm)*100)

avg_list=[]
marks_list=[777,892,794,400,1023,1092]
# avg_list=[]
# for item in marks_list:
#     avg_values=avg(item)
#     rounded_val=math.floor(avg_values)
#     avg_list.append(rounded_val)

avg_list=list(map(avg,marks_list))
print(avg_list)

# FILTER()

# The filter function filters a sequence of elements based on a given predicate 
# (a function that returns a boolean value) and returns a new sequence containing 
# only the elements that meet the predicate

def toppers(per):
   return per>80


new_list_2=list(filter(toppers,avg_list))
print("After Filter func")
print(new_list_2)

# REDUCE

# The reduce function is a higher-order function that applies a 
# function to a sequence and returns a single value

from functools import reduce
# List of numbers
numbers = [1, 2, 3, 4, 5]
# Calculate the sum of the numbers using the reduce function
sum = reduce(lambda x, y: x + y, numbers)
# Print the sum
print(sum)