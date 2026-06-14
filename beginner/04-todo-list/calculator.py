def add(a,b):
        return a+b
def subtract(a,b):
        return a-b
def multiply(a,b):
        return a*b
def divide(a,b):
        if b==0:
                return"Error: Division by zero ..."
        else:
                return a/b
while True:
        print("##############################")
        print("Welcome To the calculator app...")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")
        choice=input("Choose Option")

        if choice=="5":
                print("Exiting the calculator app")
                break 
        
        a=float(input("Enter first number: "))
        b=float(input("Enter second number"))

        if choice=="1":
                print("Result: ",add(a,b))
        elif choice=="2":
                print("Result: ",subtract(a,b))

        elif choice=="3":
                print("Result",multiply(a,b))
        elif choice=="4":
                print("Result",divide(a,b))

        else:
                print("Invalid choice")