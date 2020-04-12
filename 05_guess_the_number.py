# Writting a complete program : Guess the number 
# ---------------------------------------------------------
import random

print('Hello what is your name?')
name = input()
secret_number = random.randint(1,20)
print('Well ' + name + ' I am thinking of a number between 1 and 20')

for guessTaken in range (1,7):
    print('Take a guess:')
    guess = int(input())

    if guess < secret_number:
        print('Too low')
    elif guess > secret_number:
        print('Too high')
    else:
        break

if guess == secret_number:
    print('Your guess is correct')
else:
    print('You fail, the number I was thinking of was ' + str(secret_number))

print('You tried ' + str(guessTaken) + ' time/s')
