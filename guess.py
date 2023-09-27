#This is a guess the number game

import random

print("Hello, enter a name?")
name = input()
print("Well "+name +" I am thinking a number 1 to 20")

secretnumber = random.randint(1,20)

for guesstaken in range(1,7):
    print("Take a quess:")
    guess =int(input())
    if(guess < secretnumber):
        print("Your guess is to low")
    elif(guess > secretnumber):
        print("Your guess is to high")
    else:
        break
if(guess == secretnumber):

    print("Good Job! "+name+'Your Taken guess is'+str(guesstaken)+'\n')
else:
    print(f"Try Again number is={secretnumber} ")




print("guess")