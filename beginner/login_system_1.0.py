print("#####   LOGIN SYSTEM Version-1.0   ###")
print("          MADE BY SBS278              ")

req_username = "SBS"
req_password = "mba"

program_running = True

while program_running:

    for i in range(3):

        username = input("\nEnter the username: ")
        password = input("Enter the Password: ")

        if username == req_username and password == req_password:
            print("\nCongrats You are Logged In !!!")
            program_running = False
            break

    else:
        print("\nAccount locked: Too many failed attempts")
        program_running = False