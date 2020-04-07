# 1) Introduction
# ------------------------------------------------------------
print("Hello world")

print("What is your name?")
myName = input()
print('It is good to meet you ' + myName)
print('The length of your name is: ' + str(len(myName)))

print('What is your age?')
myAge = input()
print('You will be ' + str(int(myAge) + 1) +' in a year')


# 2) Flow control
# ------------------------------------------------------------
# if-else
password = 'swordfish'
if password == 'swordfish':
    print('Acces granted')
else:
    print('Wrong password')

# if-elif
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

# while
spam = 0
while spam < 5:
    print('Hello world')
    spam = spam + 1

# break
name = ''
while True:
    print('Please type your name')
    name = input()
    if name == 'your name':
        break
print('Thank you')

# continue
spam = 0
while spam < 5:
    spam = spam + 1
    if spam == 3:
        continue
    print('spam is ' + str(spam))

# for
for i in range(5):
    print(str(i))

total = 0
for num in range(101):
    total += num
print(total)

# for with increment by
for i in range(0,10,2):
    print(str(i))


# 3) Functions and imports
# ------------------------------------------------------------
import pyperclip # single import
import random, sys, os, math # multiple imports
from random import randint # single function import
from math import * # multiple function import

print(random.randint(1,10))
pyperclip.copy('Copied')
print(pyperclip.paste())

# functions
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
# ------------------------------------------------------------
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
# ------------------------------------------------------------
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


# 6) Lists
# ------------------------------------------------------------
spam = ['car', 'bat', 'rat', 'elephant']
print(spam)
print('----------------------------------')
print(spam[0]) # first item
print(spam[-1]) # last item
print(spam[1:3]) # slice between second and thrid item
print(spam[:2]) # slice between first and second item
print(spam[1:]) # slice between second and last item
print(spam[:-1]) # slice between first and second last item
print(spam[::-1]) # inverse the list
print('----------------------------------')
print('Making a list out of a string')
characters = list('hello')
print(characters)
print('h' in characters)
print('h' not in characters)

# for loops with lists (index and value)
supplies = ['pens', 'staplers', 'throwers', 'blinders']
for i in range(len(supplies)):
    print(str(i) + ' : ' + supplies[i])

# multiple assignment
cat = ['fat', 'orange', 'loud']
size, color, disposition = cat
print(size + ',' + color + ',' + disposition)

size, color, disposition = 'skinny', 'black', 'quiet'
print(size + ',' + color + ',' + disposition)

a = 'AAA'
b = 'BBB'
a, b = b, a
print(a + ',' +  b)

# list methods
spam = ['bat', 'rat', 'elephant']
print(spam.index('bat')) # index of the first time the value is found in the list
spam.append('dog') # add a value to the end of the list
print(spam)
spam.insert(1,'chicken') # insert a value in a particular position in the list
print(spam)
spam.remove('bat') # removes an specific value in the list
del spam[2]
print(spam) 

spam = [2, 5, 3.14, 1, -7]
spam.sort() # sorts a list
print(spam)
spam.sort(reverse=True) # reverse order
print(spam)

spam = ['bat', 'Rat', 'elephant', 'ant']
spam.sort() # doesn't use true alphabetical order
print(spam)
spam.sort(key=str.lower) # true alphabetical order
print(spam)

# There are mutuable and inmutable datatypes
# Mutable datatypes stores references 
# Lists are mutable and strings unmutable
# To modidy a string you have to create a new string
name = 'Zophie a cat'
newName = name[0:7] + 'the' + name[8:12]
print(newName)

# Copies the whole list and creates a new reference
import copy
spam = ['a', 'b','c','d']
spamCopy = copy.deepcopy(spam) 
spamCopy[0] = 'z'
print(spam)
print(spamCopy)