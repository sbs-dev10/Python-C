print("Even or Odd Checker in Python.......")
print("####################################")
print("#                                    ")
print("#  Please Input Your Number:                                    ")
print("#  Or Press X To Exit                                 ")
print("####################################")

while True:

    user=input()

    # so that user can input an integrer or character
    # if string is provided then it is converted to lowercase and if its == "x" program breaks
    #else the user variable is checked by isdigit


    if user.lower() == "x":
        break
    
    # if not isdigit = if user variable is not isdigit

    if not user.isdigit():
        print("Invalid input! Please enter a number.")
        continue

    number=int(user)

    if number%2==0:
        print("The number is even")
    else:
        print("The number is odd")
