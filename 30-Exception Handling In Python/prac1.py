def dividenums(x,y):
    try:
        ans=x/y
        print(f"The Ans after division of {x} and {y} is : {ans}")
    except ZeroDivisionError:
        print(f"The denumenator is 0")
        
dividenums(8,0)