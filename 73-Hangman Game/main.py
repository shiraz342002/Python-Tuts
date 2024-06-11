import random
word=("computer","python","fridge","artificial","metro")
sec_word=random.choice(word)
turns=5
guesses=''
print(sec_word)
while turns>0:
    failed=0
    for char in sec_word:
        if char in guesses:
            print(char,end="")
        else:
            print("_",end="")
            failed+=1
    if failed == 0:
        print("You Won")
        break
    user_input=input("\nEnter a char : ")
    guesses+=user_input
    if user_input not in word:
        turns-=1
        print(f"Try Again, You have {turns} left")
    if turns==0:
        print("You Lost better luck next time ")
        