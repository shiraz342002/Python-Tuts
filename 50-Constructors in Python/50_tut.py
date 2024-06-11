class students:
    name="Ali"
    Age=18
    cgpa=3.5
    
    def __init__(self,n,a,cgpa): ##Constructor takes 4 arguments self is default
        self.name=n
        self.Age=a
        self.cgpa=cgpa

    def display(self):
        #self ka matlab wo object jispar ye call horaha ha 
        print(f"{self.name} is {self.Age} old and his cgpa is {self.cgpa}")
    
    
    
    
obj = students("John Cena",45,"4.0")
obj.display()
