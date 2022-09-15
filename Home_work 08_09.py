# Task 1
# The Guessing Game.
# Write a program that generates a random number between
# 1 and 10 and lets the user guess what number was generated.
# The result should be sent back to the user via a print statement.
import random
computer_number = random.randint(1,10)
user_number = int(input("Please input the guessed number (1 to 10):"))
if computer_number == user_number:
    print(f" The random computer number is {computer_number}: is fit to you number {user_number}. You are mindreader")
else:
    print(f" The random computer number is {computer_number}, which not fit your guessed number {user_number}. Unfortunatelly, you are not David Copperfield")

# Task 2
# The birthday greeting program.
# Write a program that takes your name as input, and then your age as input and greets you with the following:
# “Hello <name>, on your next birthday you’ll be <age+1> years”
name = input ("Please, input your name:")
age = int(input ("Please, input your age:"))
age +=1
print (f"Hello {name}, on your next birthday you’ll be {age} years")

# Task 3
# Words combination
# Create a program that reads an input string and then creates and prints 5 random strings from characters of the input string.
# For example, the program obtained the word ‘hello’, so it should print 5 random strings(words) that combine characters

import random
word = str(input("Please input your word:"))
splitted_word = list(word)
new_combination1 = random.choices(splitted_word, k = len(word))
new_word1= "".join(new_combination1)
new_combination2 = random.choices(splitted_word, k = len(word))
new_word2= "".join(new_combination2)
new_combination3 = random.choices(splitted_word, k = len(word))
new_word3= "".join(new_combination3)
new_combination4 = random.choices(splitted_word, k = len(word))
new_word4= "".join(new_combination4)
new_combination5 = random.choices(splitted_word, k = len(word))
new_word5= "".join(new_combination5)
print (new_word1, new_word2, new_word3, new_word4, new_word5 )
# Я зрозумів, що рішення не є лаконічним та оптимальним) Пробував писати з циклом while,
# але щось не знаю ще, як помилки читати правильно. Прохання вказати на те , що слід виправити правильно.
# import random
# word = str(input("Please input your word:"))
# splitted_word = list(word)
# new_combination = random.choices(splitted_word, k = len(word))
# # new_list =[]
# while len(new_list) < 5:
#     new_list = new_word + "".join(random.choices(splitted_word, k = len(word))) # додаю до списка новий елемент,
#                                                                                   але як я зрозумів неправильно звертаюсь до індекса списку

# print (new_list)