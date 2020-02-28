''' Number Guessing game : Get a random number from the system and compare with entered user input and outputs will be
"You guessed right !" ,"My number is less than Entered number","My number is greater than Entered number",loop will stop
 on the right guess. User will get five chances if user fails to get correctly in 5 chances, output "You failed!!". '''
import random
i = random.randint(1, 100)
guess = int(input("Guess a number between 1 ,100 in 5 chances :"))
for j in range(1, 6):
    if guess == i:
        print("You guessed right !")
        break
    else:
        if guess > i:
            print("My number is less than {}".format(guess))
        else:
            print("My number is greater than {}".format(guess))
        if j == 5:
            print("You failed !!")
        else:
            guess = int(input("Guess Again :"))