class students:
    name="Ali"
    Age=18
    cgpa=3.5
    
    def display(self):
        #self ka matlab wo object jispar ye call horaha ha 
        print(f"{self.name} is {self.Age} old and his cgpa is {self.cgpa}")
    
s1 = students()
s2 = students()
s3 = students()
s1.name="Shiraz Mazhar"
s1.Age="20"
s1.cgpa=3.5
s2.name="Abdullah"
s1.Age="22"
s1.cgpa="3.6"

s1.display()
s2.display()
s3.display()