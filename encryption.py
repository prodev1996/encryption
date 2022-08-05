'''
Fernet is built on top of:

AES in CBC mode with a 128-bit key for encryption; using PKCS7 padding.

'''
from cryptography.fernet import Fernet

# Open Text file and encrypt it using a key
with open ("dummy.txt", "r") as myfile:
    data = myfile.read()

# Generation of a key
key = Fernet.generate_key()

# Value of key assigned to variable
f = Fernet(key)
encrypted = f.encrypt(data.encode())

with open("key.txt", "wb") as key_file:
    key_file.write(key)

with open("encrypted.txt", 'wb') as myfile:
    myfile.write(encrypted)

