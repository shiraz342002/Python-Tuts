
##1. Write a Python program to sum all the items in a list.

# marks=[68,75,91,88,79]
# sum=0
# for i in range(len(marks)):
#    sum+=marks[i]
    
# print(f"Sum of marks is :{sum}")
# print("The average is :",sum/len(marks))

##2. Write a Python program to multiply all the items in a list
# num=[5,7,8,9,1,66]
# mul=0
# for i in range(len(num)):
#     mul=num[i]*num[i]
#     print(mul)
    
# print(f"After multiplication : {mul}")

##Write a Python program to get the largest number from a list.
# num=[55,77,18,91,12,66]
# max=num[0]
# min=num[0]
# for i in num:
#     if i >max:
#         max=i
# for k in num:
#     if k < min:
#         min=k
    
# print("The Largest num is :",max)
# print("The Smallest num is :",min)


# a = [10,20,30,20,10,50,60,40,80,50,40]

# dup_items = set()
# uniq_items = []
# for x in a:
#     if x not in dup_items:
#         uniq_items.append(x)
#         dup_items.add(x)

# print(dup_items)
# print(uniq_items)

##8. Write a Python program to check if a list is empty or not.

# l = [3,7,8,1]
# num=0
# if not l:
#   print("List is empty")
# else : 
#     for i in l:
#         num+=1
#     print(f"list has {num} items")
      
      
##Write a Python program to clone or copy a list.

# orglist = [3,7,8,1,7,9]
# newlist=[]
# for i in orglist:
#     newlist.append(i)
#     print(i)

# print("The clone list is :")
# print(newlist)

# # Write a Python program to find the list of words that are longer than n from a given list of words.
# def long_words(n, str):
#     word_len = []
#     txt = str.split(" ")
#     print(txt)
#     print(type(txt))
#     for x in txt:
#         if len(x) > n:
#             word_len.append(x)
#     return word_len	
# print(long_words(3, "The quick brown fox jumps over the lazy dog"))

## Write a Python function that takes two lists and returns True if they have at least one common member.
# l1 = [1, 2, 3, 4, 5]
# l2 = [9, 8, 6, 7, 8]

# def common_no(l1,l2):
#     for i in l1:
#         for j in l2:
            
#             if i==j:
#                 print(i," is common in both ")
#                 return
#     print("No numbers are common in two lists")
            
# common_no(l1,l2)
               
                


# # Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.
# SampleList = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# ExpectedOutput = []
# loc = 0

# for i in SampleList:
#     if loc not in [0, 4, 5]:
#         ExpectedOutput.append(i)
    
#     loc += 1

# print(ExpectedOutput)



