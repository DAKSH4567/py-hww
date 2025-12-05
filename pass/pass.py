import random
import string

length = int(input("Enter password length: "))

chars = string.ascii_lowercase + string.ascii_uppercase + string.digits
password = random.sample(chars, length)

random.shuffle(password)

print("Generated Password:", "".join(password))
