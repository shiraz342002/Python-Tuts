def average(a, b, c=1):
  print("The average is ", (a + b + c) / 2)

# it will take a and b and will c=1 as defauly arguments
average(a=2,b=3)

def name(fname, mname = "Jhon", lname = "Whatson"):
    print("Hello,", fname, mname, lname)

name("Shiraz")

def avg(*subjects):
    sum=0
    for i in subjects:
        sum=sum+i
    # print("The average is :",sum/len(subjects))
    
    #return statement
    return sum/len(subjects)
    
ans=avg(4,4,4,9,7)
print("Avg is :",ans)
