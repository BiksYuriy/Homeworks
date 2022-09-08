#Task1 symbol
a = "symbol"
combination = input("Please, enter the {} combination :".format(a))
if len(combination) > 2:
    print(combination[:2]+combination[-2:])
elif len(combination) == 2:
    print(combination[:2])
else:
    print(" ")

#Task 2 Phone number

phone_num = (input("Please, input your mobile number:"))
if (phone_num.isdigit()) == True and (len(phone_num)) == 10:
    print("Your number is correct")
elif (phone_num.isdigit()) != True or (len(phone_num)) != 10:
    print("Your number should be inputted in the format of 10 digits length only")
else:
    print("You should input your number in the format of 0123456789")

#Task 3 Math quiz program
# Enter the input numbers and operations
# Addition,Subtraction, Division, Multiplication, Exponent (Power), Modulus, Floor division.
# Write a program that asks the answer for a mathematical expression, checks whether the user
# is right or wrong, and then responds with a message accordingly.
a = 2
b = 3
addition = int(input(f'What will be the result of addition  {a} + {b} = '))
if int(addition) == a + b:
    print("Your answer in addition operation is correct.")
else:
    print("You are wrong in addition operation")

subtraction = int(input(f'What will be the result of subtraction  {a} - {b} = '))
if int(subtraction) == a - b:
    print("Your answer in subtraction operation is correct.")
else:
    print("You are wrong in substraction operation")
print("Tip: round result to two digits in the division operation.")

division = float(input(f'What will be the result of division {a} / {b} = '))
if (division) == round(a / b, 2):
    print("Your answer in division operation is correct.")
else:
    print("You are wrong in division operation")

multiplication = int(input(f'What will be the result of multiplication  {a} * {b} = '))
if int(multiplication) == a * b:
    print("Your answer in multiplication operation is correct.")
else:
    print("You are wrong in multiplication operation")

exponents = int(input(f'What will be the result of exponent  {a} ^ {b} = '))
if int(exponents) == a ** b:
    print("Your answer in exponent operation is correct.")
else:
    print("You are wrong in exponent operation")

Floor_division = int(input(f'What will be the result of floor division {a} / {b} = '))
if (Floor_division) == a // b:
    print("Your answer in floor division operation is correct.")
else:
    print("You are wrong in floor division operation")

#task 4 Write a program that has a variable with your name stored
#(in lowercase) and then asks for your name as input.
# The program should check if your input is equal to the
# stored name even if the given name has another case, e.g.,
# if your input is “Anton” and the stored name is “anton”, it should return True.
name = "yuriy"
check_name = str(input("Enter your name:"))
if (check_name == name) or (check_name.upper() == name) or (check_name.lower() == name):
    print("True")
else:
    print ("False")
    
