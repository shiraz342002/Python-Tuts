 #****************************************************************************************
 #***                                                                                  ***
 #***  Date: 18/8/2023  Time: 9:45 AM     Author:  Shiraz Mazhar                       ***
 #***                                                                                  ***
 #***  Working On : OOP                                                                ***
 #***                                                                                  ***
 #****************************************************************************************

class Bank:
    cus_name="Dummy"
    cus_acc_no="1234"
    cus_balance="100"

    def show(self):
        print(f"Account name :{self.cus_name}\nAccount Number:{self.cus_acc_no}\nYour Balance is:{self.cus_balance}")
     
    def __init__(self,name,acc,bal):
         self.cus_name=name
         self.cus_acc_no=acc
         self.cus_balance=bal
        
    @property    
    def get_name(self):
        return self.cus_name
    
    @get_name.setter
    def set_name(self,name):
        self.cus_name=name
    @property    
    def get_accno(self):
        return self.cus_acc_no
    
    @get_accno.setter
    def set_accno(self,acc):
        self.cus_acc_no=acc
        
    @property    
    def get_balance(self):
        return self.cus_balance
    
    @get_balance.setter
    def set_balance(self,bal):
        self.cus_balance=bal
        
        
cus1=Bank("Shiraz",34,500)
cus1.set_name="Vince McMahon"
cus1.set_accno="69696969"
cus1.set_balance="1000000000000000000000"
print("Your Name is :",cus1.get_name)
print("Your Acc no is :",cus1.get_accno)
print("Your Acc Balance is :",cus1.get_balance)

cus2=Bank("dummy",123444,100)
cus2.set_name=input("Enter the name:")
cus2.set_accno=input("Enter Acc no:")
cus2.set_balance=input("Enter your Balance:")
cus2.show()