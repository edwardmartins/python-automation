# 5) Writting a complete program : Guess the number 
# ---------------------------------------------------------
import random

print('Hello what is your name?')
name = input()
secretNumber = random.randint(1,20)
print('Well ' + name + ' I am thinking of a number between 1 and 20')

for guessTaken in range (1,7):
    print('Take a guess:')
    guess = int(input())

    if guess < secretNumber:
        print('Too low')
    elif guess > secretNumber:
        print('Too high')
    else:
        break

if guess == secretNumber:
    print('Your guess is correct')
else:
    print('You fail, the number I was thinking of was ' + str(secretNumber))

print('You tried ' + str(guessTaken) + ' time/s')
