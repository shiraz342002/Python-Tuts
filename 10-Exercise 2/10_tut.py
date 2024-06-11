
# time=input("Enter the current time\nExp 6Am,12Pm : ")
# if(time=="6Am" or time=="7Am" or time=="8Am"):
#     print("Good Morning Sir")
# elif(time=="12Pm" or time=="1Pm" or time=="2Pm"):
#     print("Good After Noon Sir")
# elif(time=="8Pm" or time=="9Pm" or time=="10Pm"):
#     if(time=="9Pm"):
#         print("Dinner Time yayy")
        
#     print("Good Night Sir")
# elif(time=="1Am" or "2Am" or "3Am"):
#     print("Soja bhai")
# else:
#     print("Invalid Time")

## Harry Code
import time
t = time.strftime('%H:%M:%S') 
hour = int(time.strftime('%H'))
# hour = int(input("Enter hour: "))
print(hour)

if(hour>=0 and hour<12):
  print("Good Morning Sir!")
elif(hour>=12 and hour<17):
  print("Good Afternoon Sir!")
elif(hour>=17 and hour<0):
  print("Good Night Sir!")