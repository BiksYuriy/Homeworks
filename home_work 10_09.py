# Task 1
# Write a Python program to get the largest number from a list of random numbers with the length of 10
#  Constraints: use only while loop and random module to generate numbers

import random
random_list = []
while True:
    random_list.append(random.randint(1,100))
    if len(random_list) == 10:
        break
print(random_list, max(random_list))

# Task 2
# Exclusive common numbers.
# Generate 2 lists with the length of 10 with random integers from 1 to 10,
# and make a third list containing the common integers between the 2 initial lists without any duplicates.
# Constraints: use only while loop and random module to generate numbers


import random
random_list_1 = []
random_list_2 = []
unique_list = []
while True:
    random_list_1.append(random.randint(1,100))
    if len(random_list_1) == 10:
        break
while True:
    random_list_2.append(random.randint(1,100))
    if len(random_list_2) == 10:
        break
united_list = random_list_1 + random_list_2
unique_list = set(united_list)
unique_list = list(unique_list)
print(random_list_1,random_list_2, unique_list)

# Task 3
# Extracting numbers.
# Make a list that contains all integers from 1 to 100, then find all integers
# from the list that are divisible by 7 but not a multiple of 5, and store them
# in a separate list. Finally, print the list.
# Constraint: use only while loop for iteration

my_list = list(range(1, 100 + 1))
new_list = []
i = 0
while i < len(my_list):
    i += 1
    if i % 7 == 0 and i % 5 > 0:
        new_list.append(i)

print(new_list)

# Варівнт задачі 3 з циклом FOR
my_list = list(range(1, 100 + 1))
new_list = []
for i in list(range(1, 100 + 1)):
    if i % 7 == 0 and i % 5 > 0:
        new_list.append(i)

print(new_list)