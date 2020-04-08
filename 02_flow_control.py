# Flow control
# ---------------------------------------------------------
# If-else
password = 'swordfish'
if password == 'swordfish':
    print('Acces granted')
else:
    print('Wrong password')

# If-elif
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

# While
spam = 0
while spam < 5:
    print('Hello world')
    spam = spam + 1

# Break
name = ''
while True:
    print('Please type your name')
    name = input()
    if name == 'your name':
        break
print('Thank you')

# Continue
spam = 0
while spam < 5:
    spam = spam + 1
    if spam == 3:
        continue
    print('spam is ' + str(spam))

# For
for i in range(5):
    print(str(i))

total = 0
for num in range(101):
    total += num
print(total)

# For with increment by
for i in range(0,10,2):
    print(str(i))
