import string
import secrets

""" 
The secret module is used for generating cryptographically strong random
numbers suitable for managing data

"""
alphabet = string.printable # Printable contains String of ASCII which are considered printable. This is a combination of digits, asciii_letters, punctuation and whitespace
password = ''.join(secrets.choice(alphabet) for i in range(12))
print("The password is: " + password + "\nand the password length is: " + str(len(password)))


