#Conditional Statements and Function
def condtional_st():
    if num > 0:
        print("Positive number")
    elif num < 0:
        print("Negative number")
    else:
        print("Zero")

num = int(input("Enter a number:"))
condtional_st()