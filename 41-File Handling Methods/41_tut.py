# f=open('D:\Coding With Shiraz\Python\mymarks.txt','r')

# i=0
# while True:
#     i+=1
#     line=f.readline()
#     if not line:
#         print("No lines left ")
#         break
    
#     m1=int(line.split(",")[0])
#     m2=int(line.split(",")[1])
#     m3=int(line.split(",")[2])
#     print(f"The marks of student {i} is {m1}")
#     print(f"The marks of student {i} is {m2}")
#     print(f"The marks of student {i} is {m3}")

#     t = (m1 + m2 + m3) / 3
#     print(f"The average of student {i} marks is:", t)
    
f = open('myfile2.txt', 'w')
lines = ['line 1\n', 'line 2\n', 'line 3\n']
f.writelines(lines)
f.close()
    
