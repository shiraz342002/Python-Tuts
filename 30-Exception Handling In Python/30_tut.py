# Exception handling is the process of responding to unwanted or 
# unexpected events when a computer program runs. Exception handling deals 
# with these events to avoid the program or system crashing, and without this process, 
# exceptions would disrupt the normal operation of a program.
num=input("Enter the number you want the table of : ")
try:
    for i in range(1,11):
     print(f"{int(num)} X {i} = {int(num)*i}")
except  Exception as e:
    print(e)
    print("Invalid Input re run the program")
   
        