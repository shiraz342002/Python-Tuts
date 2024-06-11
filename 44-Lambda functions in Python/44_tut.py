per= lambda om,tm:((om/tm)*100)
# print(per(777,1100))

# Lambda is only suitable for 1 liners functions

def msg(perc):
    if perc<60:
        print("nikama saale")
    if perc>=60 and perc <=80:
        print("thk ha bhai sahi jaraha")
    if perc>80:
        print("Topper")
        
msg(per(800,1100))