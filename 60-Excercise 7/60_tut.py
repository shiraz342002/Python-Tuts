 #****************************************************************************************
 #***                                                                                  ***
 #***  Date: 20  Time:      Author:  Shiraz Mazhar         ***
 #***                                                                                  ***
 #***  Working On :                                                                    ***
 #***                                                                                  ***
 #****************************************************************************************
import os 
# os.mkdir("wwe")

os.chdir("D:\Coding With Shiraz\Python\wwe")
print(os.getcwd())
# os.rename("haha.png","stfu.png")
# print(os.listdir()) 
files=os.listdir()
k=1

# soltion to excercise

# for i in files:
#     if(i.endswith("png")):
#         os.replace(i,f"{k}.{i}")
#         k+=1

# Extra stuff
print(files)
os.remove("sup.png") # to delete a file
