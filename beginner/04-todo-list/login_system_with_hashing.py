import hashlib

def hashed_password(password):
    return hashlib.sha256(password.encode()).hexdigest()
    #inside hashlib.sha256 password is the variable entered by user and password.encode()=>CONVERTS THE STRING TO bytes as hashing alogrithm works with binary
    #.hexdigest() will give raw object
    # for extra layer of security hashed_password+salt is the best option

print("#####   LOGIN SYSTEM Version-2.0   ###")
print("          MADE BY SBS             ")

req_username = "SBS"
req_password_hash = hashed_password("mba")

program_running = True

while program_running:
    
    for i in range(3):

        username = input("\nEnter the username: ")
        password = input("Enter the Password: ")

        if username == req_username and hashed_password(password) == req_password_hash:
            print("\nCongrats You are Logged In !!!")
            program_running = False
            break

    else:# for else means else only works if break doesnt happen
        print("\nAccount locked: Too many failed attempts")
        program_running = False