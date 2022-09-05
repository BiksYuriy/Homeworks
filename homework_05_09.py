#1
data = ("Yuriy", "2022-09-05")
sentence = "Good day %s! %s is good day to learn python."
print (sentence % data)

#2
name = "Yuriy"
day = "2022-09-05"
print(f'Good day {name}! {day} is good day to learn python.')

#3
name = "Yuriy"
day = "2022-09-05"
print("Good day %s! %s is good day to learn python." %(name, day))

name = "Yuriy"
day = "2022-09-05"

print("Good day {}! ".format(name) + "{} is good day to learn python.".format(day))

name = "Yuriy"
surname = "Biks"
print("Hello, {} ".format(name) + "{}!".format(surname))

name = "Yuriy"
surname = "Biks"
print("Hello, %s %s!" %(name, surname))

a = 6
b = 5
print(a + b)
print(a - b)
print(a / b)
print(a * b)
print(abs(a),abs(b))
print(a // b)





