
while True:
    print("Temperature Converter Program Written In Python....")
    print("###################################################")
    print("Options:   ")
    print("1.Celsius  to Fahrenheit")
    print("2.Fahrenheit to Celsius")
    print("3.Celsius TO Kelvin")
    print("4.kelvin To Celsius")
    print("5.Fahrenheit to Kelvin")
    print("6. Kelvin to Fahrenheit")
    print("7.Exit App")

    choice=input("Enter Your Choice")

    if choice=="7":
        print("Exiting........")
        break


    a=float(input("Enter the Temperature You Want To convert"))

    if choice=="1":
        print("In Fahrenheit is: ",(a*9/5)+32 )
    elif choice=="2":
        print("In Celsius is ",(a-32)*5/9)
    elif choice=="3":
        print("In Kelvin  is ",a+273.15)
    elif choice=="4":
        print("In Celsius is ",a-273.15)
    elif choice=="5":
        print("In Kelvin is ",(a-32)*5/9+273.15)
    elif choice=="6":
        print("In Celsius is ",(a-273.15)*9/5+32)
    else:
        print("Invalid choice...............")


