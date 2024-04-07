import random

# Create the random number
num = random.randint(1,101)

# The number of guesses
cnt = 0

# Condition & Loop
while True:
    cnt += 1
    # taking guessing number as input
    inp = int(input("Guess a number between 1 to 100 : "))
    if inp == num:
        print("You guessed right \n %i try" %cnt)
        break;
    elif inp < num :
        print("Enter a Upper")
    elif inp > num :
        print("Enter a Lower")