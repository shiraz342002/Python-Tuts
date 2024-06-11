import random
def menu():
    mode_c=int(input("Press 1 to Play with Computer\nPress 2 to play with Another Player"))
    return mode_c
    
def vsAi():
    print("Your Turn Choose one from the following")
    user_choice=int(input("Press 1 to Pick Snake\nPress 2 to pick Water\nPress 3 to pick Gun"))
    if user_choice==1:
        print("You Picked Snake")
    elif user_choice==2:
        print("You Picked Water")
    elif user_choice==3:
        print("You Picked gun")
    else:
        print("Invalid input Try Again")
    
    comp_choice=random.randint(1,3)
    if comp_choice==1:
        print("Computer Picked Snake")
    elif comp_choice==2:
        print("Computer Picked Water")
    elif comp_choice==3:
        print("Computer Picked gun")
   
    if(user_choice==1 and comp_choice==2 or user_choice==2 and comp_choice==3 or user_choice==3 and comp_choice==1):
        print("You Won")
        end_choice=int(input("Press 1 to play Again\nPress 2 to go back to main menu"))
        if end_choice==1:
            vsAi()
        elif end_choice==2:
            menu()
    elif(comp_choice==1 and user_choice==2 or comp_choice==2 and user_choice==3 or comp_choice==3 and user_choice==1):
        print("You Lost") 
        end_choice=int(input("Press 1 to play Again\nPress 2 to go back to main menu"))
        if end_choice==1:
            vsAi()
        elif end_choice==2:
            menu()
    if(user_choice==comp_choice):
        print("It's a draw")
        end_choice=int(input("Press 1 to play Again\nPress 2 to go back to main menu"))
        if end_choice==1:
            vsAi()
        elif end_choice==2:
            menu()
 
def vs2P():
    '''This is basically a function where the player can experiance 2 players'''
    print(vs2P.__doc__)
    print("Working on 2 Player is in development, It will be available on future, For Now enjoy Playing Against Computer")
    vsAi()
    
print("Welcome to Snake Water & Gun")
g_mode=menu()
if g_mode==1:
    vsAi()
if g_mode==2:
    vs2P()
    

    
        
    
    
    