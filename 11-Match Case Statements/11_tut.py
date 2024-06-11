#Basically is a switch case from c/c++/java xD
# print("Enter your age ")
x=int(input("Enter your Age : "))
match x:
    case 16:
        print("Best Age in my opinion")
    case 17:
        print("Still the best age but a bit rusty on education side ")
    case 18:
        print("Probs started to flow like blood but have fun sometimes ")
    case 19:
        print("Even Worse Probs")
    case 20:
        print("Rip")
    case 21:
        print("gg")
    case _ if(x!=15):
        print(x," is not 15")
    case _ if(x!=50 and x<70):
        print("Dude Live the golden years")
    case _ if(x==0 or x==1):
        print("Go back bro")
    case _ :  #default case
        print("Wront age my nigga")
        
    