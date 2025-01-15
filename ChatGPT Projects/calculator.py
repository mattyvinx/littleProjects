def add(a,b): #define add function
    return a+b
def sub(a,b): #define subtraction function
    return a-b
def multi(a,b): #define multiplication function
    return a*b
def divide(a,b): #define dividing function 
    return a/b

print("Welcome to the Calculator!") #greet user
selection = 0
while selection != 5:
    try:
        selection = int(input("1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. Exit\nEnter your choice: "))##ask for current choice
    except ValueError: #catch non-int entry
        print("Invalid value entered, please try again.")
    print()
    if 0 < selection < 5: #take in values if not exiting 
        while True:
            try:
                a = float(input("Enter the first number: "))
                break
            except ValueError:
                print("Invalid entry please try again.")
        while True:
            try:
                b = float(input("Enter the second number: "))
                break
            except ValueError:
                print("Invalid entry please try again.")
    if selection == 1: #perform addition if selected
        result = add(a,b)
        print(f"Result: {a} + {b} = {result}\n")
    if selection ==2: #perform subtraction if selected
        result = sub(a,b)
        print(f"Result: {a} - {b} = {result}\n")
    if selection ==3: #perform multiplicaiton if selected
        result = multi(a,b)
        print(f"Result: {a} x {b} = {result}\n")
    if selection ==4: #perform division if selected
        if b == 0: #catch division by 0
            print("Cannot divide by 0.")
        else:
            result = divide(a,b)
            print(f"Result: {a} / {b} = {result}\n")
    if 0>= selection or selection>5: #if value is an int but not valid
        print("Invalid operation entered, please try again.")
    
        