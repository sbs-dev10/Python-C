import random

# Setting up the secret number:
secret_num=random.randint(1,100)
attempts=0

print("Welcome To The Number Guessing Game!!!")
print("You have to think of a number between 1 and 100")

while True:
    guess=int(input("Take a guess : "))
    attempts=attempts+1

    if guess<secret_num:
        print("Too Low! Try a higher number")

    elif guess>secret_num:
        print("Too High Take another guess")

    else:
        print(f"Congratulations ! You found it in {attempts} attempts")
        break 