letter = "Hey my name is {1} and I am from {0}"
country = "India"
name = "Harry"

print(letter.format(country, name))

print(f"Hello my name is {name} and I'm from {country}")

txt = "For only {price:.2f} dollars!"
print(txt.format(price = 49.435345))

val = 'Geeks'  
print(f"{val}for{val} is a portal for {val}.")  
name = 'Tushar'  
age = 23  
print(f"Hello, My name is {name} and I'm {age} years old.")

##you can print the format by using double curly  brackets
print(f"Hello my name is {{name}} ")