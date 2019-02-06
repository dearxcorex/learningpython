import random



chars = 'asdokqweokasdflkslkfdsdk544825@'

length = input('password length: ')
length = int(length)

password=''
for i in range(length):
    password += random.choice(chars)
print(password)
