questions = [
    ["Which is the longest railway route in Pakistan?",
    "Karachi–Peshawar Railway Line", "Lahore–Karachi Railway Line", "Quetta–Taftan Railway Line", "Rohri–Chaman Railway Line", 1],

    ["Which city is known as the 'Railway Junction of Pakistan'?",
    "Lahore", "Karachi", "Rawalpindi", "Multan", 2],

    ["Which is the highest railway station in Pakistan?",
    "Attock Khurd", "Kan Mehtarzai", "Landi Kotal", "Quetta", 1],

    ["Which railway track connects Pakistan with Iran?",
    "Quetta-Taftan Railway Line", "Peshawar-Karachi Railway Line", "Lahore-Islamabad Railway Line", "Karachi-Hyderabad Railway Line", 0],

    ["Which is the oldest railway station in Pakistan?",
    "Lahore Junction", "Karachi Cantonment", "Multan Cantt", "Rawalpindi", 1],

    ["Which is the fastest train in Pakistan?",
    "Karakoram Express", "Awam Express", "Green Line Express", "Tezgam Express", 0],

    ["Which railway track connects Pakistan with India?",
    "Lahore-Amritsar Railway Line", "Wagah-Lahore Railway Line", "Karachi-Mumbai Railway Line", "Quetta-Jodhpur Railway Line", 1],

    ["Which is the largest railway workshop in Pakistan?",
    "Mughalpura Railway Workshop, Lahore", "Carriage Factory, Islamabad", "Railway Locomotive Factory, Risalpur", "Pakistan Railways Workshop, Karachi", 0],

    ["In which city is the Pakistan Railways Headquarters located?",
    "Lahore", "Karachi", "Islamabad", "Rawalpindi", 2],

    ["Which is the first railway station in Pakistan that offers free Wi-Fi to passengers?",
    "Karachi Cantt", "Lahore Junction", "Islamabad", "Rawalpindi", 1],

    ["Which is the largest railway bridge in Pakistan?",
    "Attock Bridge", "Sukkur Bridge", "Khanpur Bridge", "Gujranwala Bridge", 0],

    ["Which railway station in Pakistan holds the record for the highest number of platforms?",
    "Karachi Cantt", "Lahore Junction", "Rawalpindi", "Multan", 3]
]

levels=[1000,2000,5000,20000,50000,100000,200000,500000,10000000]

money=0
for i in range(len(questions)):
   question=questions[i]
   print(f"Question for Rupess {levels[i]}")
   print(question[0])
   print(f"a.{question[1]}        b.{question[2]}")
   print(f"c.{question[3]}        d.{question[4]}")
   ans=int(input("Enter Your Answer (1-4) or Press 5 To Quit Game"))
   if ans==5:
       print("You quit the game\nCongrats You Won :",money," Rupees")
   if ans==question[-1]:
       print(f"Correct Answer You Won {levels[i]} Rupees")
       if(i==3):
           money=20000
       elif(i==6):
           money=200000
       elif(i==8):
           money=1000000
   else:
       print("You Lost")
       break
   
print(f"Thanks for playing You Won {money} Rupees")