file= open("tasks.txt", "a+") #open file
file.seek(0) #set file cursor to 0
toDoList = [line.rstrip() for line in file]
file.seek(0) #set cursor positon to 0
file.truncate() #clear contents of file

print("Welcome to the To-Do List Manager!")
mode = int(0) #while loop variable 
while mode != 4: #loop for program run
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Exit")
    try:
        mode = int(input("Enter your choice: ")) 
    except: #verify valid input
       print("Invalid choice, please try again. \n")
    if mode ==1:
        if len(toDoList)==0: #verify items in list
            print("No items in To-Do list")
        else: #if items present, display
            print(f"Your Tasks: ")
            for i in range(len(toDoList)):
                print(f"{i+1}. {toDoList[i]}")
        print()
    if mode ==2: #add item to list
        toDoList.append(input("Enter the task to add: "))
        print("Task added!\n") 
    if mode ==3: #remove item from list
        if len(toDoList) == 0:
            print("No items to remove. \n")
        rmv = input("Enter item to remove: ")
        if rmv in toDoList:
            toDoList.remove(rmv)
            print("Item removed.\n")


print("Saving tasks to file... Goodbye!") #display closing 
for i in range(len(toDoList)):
    file.write(f"{toDoList[i]}\n") #write items to file
    file.close() #close file


