# 1) Introduction
print("Hello world")

print("What is your name?")
myName = input()
print('It is good to meet you ' + myName)
print('The length of your name is: ' + str(len(myName)))

print('What is your age?')
myAge = input()
print('You will be ' + str(int(myAge) + 1) +' in a year')


# 2) Flow control
password = 'swordfish'
if password == 'swordfish':
    print('Acces granted')
else:
    print('Wrong password')


name = 'Bob'
age = 3000
if name == 'Alice':
    print('Hi Alice')
elif age < 12:
    print('You are not Alice, kiddo')
elif age > 2000:
    print('Unlike you, Alice is not an inmortal vampire')
elif age > 100:
    print('You are not Alice, grannie')


spam = 0
while spam < 5:
    print('Hello world')
    spam = spam + 1


name = ''
while True:
    print('Please type your name')
    name = input()
    if name == 'your name':
        break
print('Thank you')

spam = 0
while spam < 5:
    spam = spam + 1
    if spam == 3:
        continue
    print('spam is ' + str(spam))

for i in range(5):
    print('Jimmy Five times ' + str(i))

total = 0
for num in range(101):
    total += num
print(total)

for i in range(0,10,2):
    print('Jimmy Five times ' + str(i))



# 3) Functions and imports
import pyperclip
import random, sys, os, math
from random import randint
from math import *

print(random.randint(1,10))
pyperclip.copy('Copied')
print(pyperclip.paste())

def hello():
    print('Edward!!')
    print('Hello there!!')

hello()

def hello(name):
    print('Hello ' + name + '!!')

hello('Alice')
hello('Bob')

def plusOne(number):
    return number + 1

newNumber = plusOne(5)
print(newNumber)



# 4) Try and except statements
def divBy(number,divideBY):
    try:
        return number / divideBY
    except ZeroDivisionError:
        print('Error: you tried to divide by zero')

print(divBy(42,2))
print(divBy(42,12))
print(divBy(42,0))
print(divBy(42,1))

print('How many cats do you have?')
numCats = input()
try:
    if int(numCats) >= 4:
        print('That a lot of cats')
    else:
        print('That is not that many cats')
except ValueError:
    print('You did not enter a number')


    
# 5) Guess the number program
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
    
