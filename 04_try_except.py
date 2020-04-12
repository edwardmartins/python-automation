# Try and except statements
# ---------------------------------------------------------
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
num_cats = input()
try:
    if int(num_cats) >= 4:
        print('That a lot of cats')
    else:
        print('That is not that many cats')
except ValueError:
    print('You did not enter a number')
