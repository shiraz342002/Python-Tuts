 #****************************************************************************************
 #***                                                                                  ***
 #***  Date: 18/8/2023  Time: 6:00 Pm     Author:  Shiraz Mazhar                       ***
 #***                                                                                  ***
 #***  Working On :  Library Managment                                                 ***
 #***                                                                                  ***
 #****************************************************************************************

class Library:
    book_list=[]
    no_of_books=0
    def addbooks(self):
        while True:
            temp=input(("Enter the Name of Book you want to Add Press -1 to Stop : "))
            if temp!="-1":
             self.book_list.append(temp)
             self.no_of_books+=1
            else:
                break
            
    def displayBooks(self):
        if len(self.book_list)==self.no_of_books:
           print(f"Total books in library is : {self.no_of_books}")
        print("Following Books are Avialable in Library")
        for i in self.book_list:
          print(i)
            
        
l1 = Library()          
l1.addbooks()
l1.displayBooks()