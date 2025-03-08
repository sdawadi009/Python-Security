import hashlib

def hashed_password(password):
    "This program hashes the value of a password"
    encoding = password.encode() #converts to byte since it cannot operate on plain text"
    encoded = hashlib.sha256(encoding) #the encoding function
    converting = encoded.hexdigest() #Since the enocded is in binary format, it converts to readable hexadecimal format"
    return converting

password = input ("enter a password to hash :")
hashed_password = hashed_password (password)
print (f"Original password is : {password}")
print (f"hashed password is : {hashed_password}")


