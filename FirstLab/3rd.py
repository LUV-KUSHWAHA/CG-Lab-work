#Loops and main()_function
def loops(x,y):
    print("Numbers from ",x,"to ",y,"is: ")
    for i in range(x,y+1):
        print(i)

def main():
    print("Loops in PYTHON")
    x = int(input("Enter initial value: "))
    y = int(input("Enter final value: "))
    loops(x,y)

if __name__ == "__main__":
    main()