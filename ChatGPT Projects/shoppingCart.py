print("Welcome to the Shopping Cart System!")#greet user
mode = 0
shoppingcart = {} 
while mode != 4: #while loop while running
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View Cart")
    print("4. Checkout and Exit")
    mode = int(input("Enter your choice: "))

    if mode == 1: ##Add Item
        name = input("Enter the item name: ")
        while True:
            try: #check valid price
                price = float(input("Enter the price of the item: "))

                break
            except ValueError: #catch invalid 
                print("Invalid price, try again.")
        while True: #check valid quantity
            try:
                quantity = int(input("Enter the quantity: "))

                break
            except ValueError: #catch invalid quantity
                print("Invalid price, try again.")
 
        tupleAdd = (price,quantity)
        shoppingcart[name]=tupleAdd

    elif mode ==2: ##remove Item
        if len(shoppingcart) == 0: #validate items to remove
            print("No items to remove.")
        else:
            remove = input("Please enter an item to remove: ")
            shoppingcart.pop(remove, None)
    
    
    elif mode ==3:
        if len(shoppingcart) == 0:
            print("No items to print.")
        else:
            print("Cart Contents:")
            for i in shoppingcart:
                item = i
                price = shoppingcart[i][0]
                quantity = shoppingcart[i][1]
                print(f"{item}: ${price} x {quantity} = ${price*quantity}")

## print total


total = 0 #total for cart set to 0
for i in shoppingcart: #calc total 
    price = shoppingcart[i][0]
    quantity = shoppingcart[i][1]
    total+=(price*quantity)
print(f"Checkout Total: ${total}") #print total 
print("Thank you for shopping with us!")