
## Noob Method
# lst = ["Karachi", "Moscow", "Chicago", "Paris", "Rome"]
# loc = 0
# for i in lst:
#     print(i)
#     if i == "Chicago":
#         print(loc)
#         break
#     loc += 1


##Pro Method using enumerate function
lst = ["Karachi", "Moscow", "Chicago", "Paris", "Rome","Mumbai","Toronoto"]
for index,i in enumerate(lst,start=1): ##start=1 is not necessory can only be used if you want index to start from 1
    print(index,i)
    # if i == "Chicago":
     




