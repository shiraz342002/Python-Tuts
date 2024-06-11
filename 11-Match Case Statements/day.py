month=int(input("Enter the month number :"))
match month:
    case 1:
        print("January")
    case 2:
        print("Feb")
    case 3:
        print("March")
    case _:
        print("Invalid year")