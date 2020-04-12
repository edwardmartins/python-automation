# Functions and imports
# ---------------------------------------------------------
import pyperclip # single import
import random, sys, os, math # multiple imports
from random import randint # single function import
from math import * # multiple function import

print(random.randint(1,10))
pyperclip.copy('Copied')
print(pyperclip.paste())

# Functions
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

new_number = plusOne(5)
print(new_number)