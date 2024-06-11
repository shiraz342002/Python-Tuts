gnum=0
cnum=5
while(gnum!=cnum):
    gnum=int(input("Enter the number :"))
    if(gnum!=cnum):
        print("Invalid Number input Again")
    if(gnum==cnum):
        print("Correct Guess")
        break
    
