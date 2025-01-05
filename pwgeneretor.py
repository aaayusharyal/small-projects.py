import random as rand #using random module-used to generate random digits
import string
# print(dir(rand))#dir prints all the keywords of that module
# print(dir(string))
numbers = string.digits
length = int(input("Enter the desired length of the password: "))
password = ''.join(rand.choice(numbers) for _ in range(length))
print("Generated password:", password)
