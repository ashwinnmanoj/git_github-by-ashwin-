import random
import string
length = int(input("password length: "))
characters = string.ascii_letters + string.digits + string.punctuations 
password = ""
for i in range(length):
    password +=random,choice(characters)
    print("generated password",password)
    