"""
Objective   : Program to generate a random password using random.choice
function
"""
import random

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_+}{0123456789"
print(len(chars))
length = int(input("Enter password length: "))
password = ""

for i in range(length + 1):
    password += random.choice(chars)
print(password)
print(len(password))
