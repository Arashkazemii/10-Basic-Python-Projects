import secrets
import string

def passGenerator(length) :
    alphabet = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(alphabet) for i in range (length))
    return password

length = 16
password = passGenerator(length)
print(f'New Password is : {password}')