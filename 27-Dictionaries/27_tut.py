info = {'name':'Karan', 'age':19, 'eligible':True}
# print(info['name'])
# print(info.get('eligible'))
# print(info.keys()) ## To print keys 
# print(info.values()) ##To print Values

# #Another Method to print the keys
# for key in info.keys():
#     print(f"The keys in dictionary are",{info[key]})

#TO just print items ie both keys and values together
print(info.items())
#To print both keys and values seprately
for key,value in info.items():
   print(f"The value corresponding to {key} is {value}")
