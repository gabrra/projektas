# uzduotys 05 - uzdeti ir nuimti hashtag su command ir \

# 1. Let user enter name, surname and age. Print if user is allowed to enter an online casino or not. 21 is the age cap.

#mano pvz
# number1 = input("Ivesk savo varda: ")
# number2 = input("Ivesk savo pavarde: ")
# number3 = int(input("Ivesk savo amziu: ")) #atsimint reikia kad funkcijos dirba taip len() int() ir t.t 
# x = number3

# if x >= 21:
#     print("Sveiki atvyke i kazino!")
# else:
#     print("Jus negalite patekti i kazino")

# kitu pvz
# name = input("Please write your name ")
# surname = input("Please write your surname ")
# age = int(input("Please write your age "))
# if age >= 21:
#    print("You are allowed to lose your money ")
# else:
#    print("Save your parents money for something else like milk and stuff ")

#kitu pvz
#name = input("Insert your name ")
#lastname = input("Insert your lastname ")
#age = int(input("Insert your age "))
 
#if age <= 21:
#    print(f"Client {name} {lastname} is not allowed to go into our casino")
#else:
#    print(f"Client {name} {lastname} is {age} years old and is allowed to go into our casino")

#kitu pvz
#name = input("please enter your name: ")
#age = int(input("please enter your age: "))
 
#my_dic = {
#    "name": name,
#    "age": age
#}
 
#if my_dic["age"] >= 21:
#    print("allowed to enter")

# -------------------------
# 2. Create a database (list of privileged users), 
# #print a specific message with a personal greeting if the user is a privileged and just "Welcome otherwise"

# user = input("what is your name, user?: ")
# privileged_users = ["gabi", "benas", "ana"]
# if user.lower() in privileged_users: #lower tikrins ir didziasias ir mazasias raides nepaisant to kaip ivesta
#     print(f"Welcome home {user}")
# else:
#     print("Welcome")

#ant array negali naudoti lower - mazinti teksto raidziu

#kito studento:
#admin_users = ["admin", "sudo", "superuser"]
#user_input = input("Please insert your username ")
 
#if user_input not in admin_users:
#    print("Welcome")
#else:
#    print(f"Welcome back {user_input}")

# ------------------------
# 3. Allow user to enter two numbers, print out which one is higher than the other, or equal.

number1 = int(input("Ivesk numeri: "))
number2 = int(input("Ivesk kita numeri: "))
a = number1
b = number2

if a > b:
    print(a)
elif a < b:
     print(b)
else:
    print(a, b)

# --------------------------
# 4. Write a small calculator application, 
# that allows user to enter two numbers and a symbol, do the operation and print the answer.


# number1 = int(input("Ivesk numeri: "))
# number2 = int(input("Ivesk kita numeri: "))
# number3 = input("Ivesk simboli: ")
# a = number1
# b = number2
# c = number3

# oper = a, c, b
# print(oper)

# kito studento
# number1 = int(input("Please insert first number "))
# number2 = int(input("Please insert second number "))
# operator = input("Please insert an operator for the equation (+, -, * or /) ")
 
# if operator == '+':
#     result = number1 + number2
# elif operator == '-':
#     result = number1 - number2
# elif operator == '*':
#     result = number1 * number2
# else:
#     result = number1 / number2
# print(f"{number1} {operator} {number2} = {result}")


#kito studento
# number1 = int(input("Please insert first number "))
# number2 = int(input("Please insert second number "))
# operator = input("Please insert an operator for the equation (+, -, * or /) ")
 
# if operator == '+':
#     result = number1 + number2
#     print(f"{number1} {operator} {number2} = {result}")
# elif operator == '-':
#     result = number1 - number2
#     print(f"{number1} {operator} {number2} = {result}")
# elif operator == '*':
#     result = number1 * number2
#     print(f"{number1} {operator} {number2} = {result}")
# elif operator == '/':
#     result = number1 / number2
#     print(f"{number1} {operator} {number2} = {result}")
# elif operator != '+' or '-' or '*' or '/':
#     print("Operator is incorrect, please read the instructions carefully")

# -------------------------
# 5. Create a number guessing game from 1-10.py

x = 2
number1 = int(input("Atspek numeri: "))
a = number1

if a == x:
    print("teisingai")
else:
    print("bandyk is naujo")


# kito studento
# n1 = int(input("Write a number please "))
# n2 = int(input("Write a second number please "))
# s1 = input("Write a symbol *, /, +, - ")
# if s1=="*":
#     print(f"The answer of your multiplication is {n1*n2} ")
# elif s1=="/":
#     print(f"The answer of your division is {n1/n2} ")
# elif s1=="+":
#     print(f"The answer of your addition is {n1+n2} ")
# else:
#     print(f"The answer of your deduction is {n1-n2}")