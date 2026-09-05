# A mini number guessing name:
import random
secret_number=random.randint(1,10)
guess=int(input("WHAT'S YOUR BEST GUESS:"))
while guess!=secret_number:
    if(guess<secret_number):
        print("TOO LOW")
        break
    elif(guess>secret_number):
        print("TOO HIGH")
        break
    elif(guess==secret_number):
        print("CORRECT THE ANSWER IS:",secret_number)
        break
print("THE CORRECT ANSWER WAS:",secret_number)