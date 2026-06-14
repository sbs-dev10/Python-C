todoList=[]

try:
    file = open("tasks.txt", "r")

    for line in file:
        todoList.append(line.strip())

    file.close()

except:
    todoList = []

def save_tasks(todoList):
    with open("tasks.txt", "w") as file:
        for task in todoList:
            file.write(task + "\n")

#Basically addding save and load functions in the simple todolist app


while True:
    print("\n--- TO-DO LIST MENU ---")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Delete Task")
    print("4. Save Task")
    print("5. Exit")

    choice=input("\nEnter your choice (1-5): ")

    #Add Task
    if choice=="2":
        task=input("Enter Task: ")
        todoList.append(task)
        save_tasks(todoList)
    
    #(View Tasks)
    elif choice=="1":
        print("\n Viewing Tasks... ")
        for i in range(len(todoList)):
            print(i + 1, todoList[i])

    #Delete Tasks
    elif choice=="3":

            try:
                index = int(input("Enter task number to remove: ")) - 1

                if 0 <= index < len(todoList):
                    todoList.pop(index)
                else:
                    print("Invalid task number")

            except:
                print("Please enter a valid number")


    elif choice=="5":
        print("Exiting the program.....")
        break

    elif choice=="4":
        save_tasks(todoList)

       
    else:
        print("Invalid Chocie ...")
