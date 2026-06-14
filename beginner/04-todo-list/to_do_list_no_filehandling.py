todoList=[]

while True:
    print("\n--- TO-DO LIST MENU ---")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Delete Task")
    print("4. Exit")

    choice=input("\nEnter your choice (1-4): ")

    #Add Task
    if choice=="2":
        task=input("Enter Task: ")
        todoList.append(task)
    
    #(View Tasks)
    elif choice=="1":
        print("\n Viewing Tasks... ")
        for i in range(len(todoList)):
            print(i + 1., todoList[i])

    elif choice=="3":

        if len(todoList) == 0:
            print("No tasks to delete")

        index = int(input("Enter task number for removing it: ")) - 1
        todoList.pop(index)

    elif choice=="4":
        print("Exiting the program.....")
        break
    else:
        print("Invalid Chocie ...")