# # IF ELSE

# num1=int(input("Enter your Age"))
# if(num1>=18):
#     print("You are a big dawg")
# else:
#     print("F you small as nigga")
## EL IF
# grade=(input("Enter Your Grade :"))
# print("Your grade is :",grade)
# if(grade=="A"):
#     print("Nice man you the topper")
# elif(grade=="B"):
#     print("Not bad Actually bro")
# elif(grade=="C"):
#     print("Dude you are a fucking dumb fuck")
# elif(grade=="D"):
#     print("dunno what to say")
# elif(grade=="F"):
#     print("Rest In peace Dawg")
# else:
#     print("Wrong input you EmptyHeaded Dumb Fuck")
    
## Nested if

print("Enter two Numbers :")
num1=int(input())
num2=int(input())
sum=num1+num2
print("The sum of ",num1,"and",num2,"is :",sum)
if(sum!=0 and sum>20):
    if(sum<60):
        print("Nested If Activated")
    else:
        print("Only if condition activated")
else:
    print("Not even if executed xD")