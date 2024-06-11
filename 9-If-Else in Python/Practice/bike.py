
cost=int(input("Enter the Cost of the Bike :"))
if(cost<=50000):
    tax=(cost*5)/100
    print("The Tax of bike will be: ",tax)
elif(cost>50000 and cost<=10000):
    tax=(cost*10)/100
    print("The Tax of bike will be: ",tax)
elif(cost>100000):
    tax=(cost*15)/100
    print("The Tax of bike will be: ",tax)
else:
    print("Invalid Cost")