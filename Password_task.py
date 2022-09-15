# import random
#
# lowercase_alphabet = "abcdefghijklmnopqrstuvwxyz"
# uppercase_alphabet = lowercase_alphabet.upper()
# numbers = "0123456789"
# special_characters = "!?#$%^&*()+@-"
#
# # By default you need to initialize set with lowercase alphabet
# characters_set = lowercase_alphabet  # -- * Your code here * --
#
# print("By default password creates from english alphabet in lower case.")
#
# answer = input("Do you want to add upper case letters to your random password? YES/NO: ")
# while ((answer != "YES") and (answer != "NO")):  # -- * Your code here * --:
#     answer = input("You typed wrong asnwer. Please enter YES or NO: ")
# else:
#     if (answer == "YES"):
#         characters_set = characters_set + uppercase_alphabet
#
# answer = input("Do you want to add numbers to your random password? YES/NO: ")
# while ((answer != "YES") and (answer != "NO")):
#     answer = input("You typed wrong asnwer. Please enter YES or NO: ")
# else:
#     if (answer == "YES"):
#         characters_set = characters_set + numbers
#
# answer = input("Do you want to add special characters to your random password? YES/NO: ")
# while ((answer != "YES") and (answer != "NO")):
#     answer = input("You typed wrong asnwer. Please enter YES or NO: ")
#     # If positive answer than add new set of characters to current set
# else:
#     if (answer == "YES"):
#         characters_set = characters_set + special_characters
#     # -- * Your code here * --
#
# print("Set of symbols to create password:", characters_set, end="\n\n")
#
# print("Password should be not lower than 6 symbols and not more than 32")
#
# password_length = int(input("Enter password length: "))
# # If user entered wrong number program asks again
# password = ""
# while (password_length > 32) or (password_length < 6):  # -- * Your code here * --
#     input("You typed wrong number. Enter number between 6 and 32: ")
#
# while len(password) < password_length:  # -- * Your code here * --:
#      # Take one random character out of characters set
#     password = password + random.choice(characters_set) # Add character to password
#     # -- * Your code here * -
#
# print("Random generated password:", password)
#
# # password_length = int(input("Enter password length: "))
# # If user entered wrong number program asks again
# # password = ""
# # while  32 < password_length < 6:
# #     input("You typed wrong number. Enter number between 6 and 32: ")
# # else:
# #     while  password_length < len(str(password)):
# #         random_character = random.choice(characters_set)
# #         password = password + random_character# -- * Your code here * --
# # print("Random generated password:", password)
import random

lowercase_alphabet = "abcdefghijklmnopqrstuvwxyz"
uppercase_alphabet = lowercase_alphabet.upper()
numbers = "0123456789"
special_characters = "!?#$%^&*()+@-"

# By default you need to initialize set with lowercase alphabet
characters_set = lowercase_alphabet  # -- * Your code here * --

print("By default password creates from english alphabet in lower case.")

answer = input("Do you want to add upper case letters to your random password? YES/NO: ")
while ((answer != "YES") and (answer != "NO")):  # -- * Your code here * --:
    answer = input("You typed wrong asnwer. Please enter YES or NO: ")
else:
    if (answer == "YES"):
        characters_set = characters_set + uppercase_alphabet

answer = input("Do you want to add numbers to your random password? YES/NO: ")
while ((answer != "YES") and (answer != "NO")):
    answer = input("You typed wrong asnwer. Please enter YES or NO: ")
else:
    if (answer == "YES"):
        characters_set = characters_set + numbers

answer = input("Do you want to add special characters to your random password? YES/NO: ")
while ((answer != "YES") and (answer != "NO")):
    answer = input("You typed wrong asnwer. Please enter YES or NO: ")
    # If positive answer than add new set of characters to current set
else:
    if (answer == "YES"):
        characters_set = characters_set + special_characters
    # -- * Your code here * --

print("Set of symbols to create password:", characters_set, end="\n\n")

print("Password should be not lower than 6 symbols and not more than 32")

password_length = int(input("Enter password length: "))

# If user entered wrong number program asks again
while password_length < 6 or password_length > 32:  # -- * Your code here * --
    password_length = int(input("You typed wrong number. Enter number between 6 and 32: "))

password = ""
while len(password) < password_length:  # -- * Your code here * --:
    # Take one random character out of characters set
#     random_character = random.choice(characters_set)  # -- * Your code here * --
    password = password + random.choice(characters_set) # Add character to password
print("Random generated password:", password)