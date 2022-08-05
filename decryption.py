from cryptography.fernet import Fernet

# Open Text file and encrypt it using a key
with open ("encrypted.txt", "r") as myfile:
    data = myfile.read()

# Reading the key
key = open("key.txt", "rb").read()
f = Fernet(key)

# Loading text file into a variable
decrypted = f.decrypt(data.encode())

# Printing the decrypted text
print(decrypted)
