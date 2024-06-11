
names="Shiraz"
print(len(names))  #len is used to check length of the string
print(names)
namelen=(len(names))
print(names,"is of",namelen,"characters")

print(names[0:3])  # String Slicing
#Always use 0 for 1st character
print("sup",names[0:-2]) # python uses len function and print the remaning characters
 
nm="Harry"
print(nm[-4:-2]) #will print ar as firstly it will do 5-4 will give us 1:-2 so it will print a and by len -2 it will print r so the output will be ar


str=("John Cena")
strlen=len(str)
print(strlen)
print(str[0:4])