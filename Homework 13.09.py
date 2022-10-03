# Task 1
#
# Make a program that has some sentence (a string) on input and returns a dict
# containing all unique words as keys and the number of occurrences as values.

sentence = (input("Please input your sentence:"))
split_sentence = sentence.lower().split()
# a = set(split_sentence)

dict_words = {}
for word in split_sentence:
    if dict_words.get(word) is None:
        dict_words[word] = 1
    else:
        dict_words[word] += 1

print(dict_words)



# Task 2
# Compute the total price of the stock where the total price is
# the sum of the price of an item multiplied by the quantity of this exact item.

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

total_price = {}
print({value: stock[value] * prices[value] for value in prices})
print(sum(stock[key] * price for key, price in prices.items())) # from stack overflow


# Task 3
#
# List comprehension exercise
# # Use a list comprehension to make a list containing tuples (i, j)
# where `i` goes from 1 to 10 and `j` is corresponding to `i` squared.

list_a = list(range(1, 10 + 1))
new_list = []
for number in list_a:
    squared_number = number ** 2
    new_list.append(squared_number)

tupled_list = tuple(list_a) + tuple(new_list)
print(tupled_list)
# Task 4
# Створити лист із днями тижня.
# В один рядок (ну або як завжди) створити словник виду: {1: “Monday”, 2:...
# Також в один рядок або як вдасться створити зворотний словник {“Monday”: 1,

week_day_list = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
for i, day in  enumerate(week_day_list):
    week_day_list[i] = (day, i+1)
dict(week_day_list)
new_dict = {y: x for x, y in dict(week_day_list).items()}
print (dict(week_day_list))
print (new_dict)