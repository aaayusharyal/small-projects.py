import random as rand
import string
# print(dir(rand))
# print(dir(string))
numbers = string.digits
length = int(input("Enter the desired length of the password: "))
password = ''.join(rand.choice(numbers) for _ in range(length))
print("Generated password:", password)
