def fibonacci(num):
    if(num==0):
        return 0
    elif(num==1):
        return 1
    
    return fibonacci(num-2)+ fibonacci(num-1)

maxnum=int(input("Enter the limit of fibonacci numbers :"))
for i in range(maxnum):
    print(fibonacci(i)," ")
