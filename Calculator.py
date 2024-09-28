





def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def multi(x, y):
    return x * y

def div(x, y):
    return x / y

def mod(x, y):
    return x % y


operation = {
    "+": add,
    "-": sub,
    "x": multi,
    "%": mod,
    "/": div,   
}
print(operation["+"](3, 5))

choice = input("What do you wanna do? (+, -, x, %, /): or q to quit ") # choice = "+"

while choice != "q":
    num1 = int(input("Enter 1st number: ")) # num1 = 4
    num2 = int(input("Enter 2nd number: "))
    result = operation[choice](num1, num2) # (operation["+"]) --> add(4, 6)
    print(result)


    choice = input("What do you wanna do? (+, -, x, %, /): or q to quit: ") # choice = "+"

    if choice != "q":
        num1 = int(input("Enter your first number: "))
        num2 = int(input("Enter your second number: "))
        result = operation[choice](num1, num2)
        print(result)


