city="Lahore da pawa Lahore"
print(len(city))
print(city.upper()) # will print in upper case
print(city.lower()) # will print in lower case
city2="shirazzzzz"
print(city2.rstrip("z")) # will only strip traling characters
print(city.replace("Lahore","Karachi")) # will replace the specefic characters from all ends 
print(city.split(" ")) # split all the sentences,characters in the string 
print(city2.capitalize()) # will turn 1st character to upper rest to lower

print(city2.center(50)) #The center() method aligns the string to the center as per the parameters given by the user.
str1 = "Welcome to the Console!!!"
print(str1.center(50, "-"))

print(city.count("Lahore")) #The count() method returns the number of times the given value has occurred within the given string.

str2 = "Abracadabra"
countStr = str2.count("a")
print(countStr)

print(city.endswith("Lahore")) #The endswith() method checks if the string ends with a given value. If yes then return True, else return False.

print(city.find("lahore"))
print(city.find("lawa")) #The find() method searches for the first occurrence of the given value and returns the index where it is present. If given value is absent from the string then return -1.

print(city.index("da")) #The index() method searches for the first occurrence of the given value and returns the index where it is present. If given value is absent from the string then raise an exception





