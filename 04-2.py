# exercises 10
# 1. Create at least 5 different functions by your own and test it.

# #pirma funkcija
# import random #isidedam sita, jei norime gauti random skaiciu nuo 1 iki 100

# def get_random_number(): #vadiname viska mazosiomis, tarp zodziu dedame underscore _ ir funkcija turi buti pavadinta veiksmazodziu
#     return random.randint(0, 100)

# something = get_random_number()
# print(something) #galima naudoti random skaiciu spejime

# def find_difference(num1:int, num2:int, num3:int): #i musu funkcija paduodami variables numeris 1 ir numeris 2, numeris 3
#     difference_nums = num1 - num2 - num3 - something 
#     return difference_nums  # Returns the difference of the numbers

# print(find_difference(10, 5, 1)) #paduoda argumentus i sita funkcija 


# #antra funkcija
# import random #isidedam sita, jei norime gauti random skaiciu nuo 1 iki 1000

# def get_random_number(): #vadiname viska mazosiomis, tarp zodziu dedame underscore _ ir funkcija turi buti pavadinta veiksmazodziu
#     return random.randint(0, 1000)

# something = get_random_number()
# print(something) #galima naudoti random skaiciu spejime

# def find_difference(num1:int, num2:int, num3:int, num4:int=0.99): #i musu funkcija paduodami variables numeris 1 ir numeris 2, numeris 3
#     difference_nums = num1 - num2 - num3 + num4 + something 
#     return difference_nums  # Returns the difference of the numbers

# print(find_difference(1000, 100, 10)) #paduoda argumentus i sita funkcija 


# #trecia funkcija
# import random #isidedam sita, jei norime gauti random skaiciu nuo 1 iki 1000

# def get_random_number(): #vadiname viska mazosiomis, tarp zodziu dedame underscore _ ir funkcija turi buti pavadinta veiksmazodziu
#     return random.randint(0, 10)

# something = get_random_number()
# print(something) #galima naudoti random skaiciu spejime

# def find_difference(num1:int, num2:int, num3:int, num4:int=0.99): #i musu funkcija paduodami variables numeris 1 ir numeris 2, numeris 3
#     difference_nums = something / num1 / num2 / num3 + num4 
#     return difference_nums  # Returns the difference of the numbers

# print(find_difference(2, 2, 2)) #paduoda argumentus i sita funkcija 


# #ketvirta funkcija

# import random #isidedam sita, jei norime gauti random skaiciu nuo 1 iki 1000

# def get_random_number(): #vadiname viska mazosiomis, tarp zodziu dedame underscore _ ir funkcija turi buti pavadinta veiksmazodziu
#     return random.randint(0, 10)

# something = get_random_number()
# print(something) #galima naudoti random skaiciu spejime

# def find_difference(num1:int, num2:int, num3:int, num4:int=0.5): #i musu funkcija paduodami variables numeris 1 ir numeris 2, numeris 3
#     difference_nums = (something + something) - num1 - num2 - num3 + num4 
#     return difference_nums  # Returns the difference of the numbers

# print(find_difference(1, 1, 1)) #paduoda argumentus i sita funkcija 


# penkta funkcija

# def even_odd(num): #skaicius lyginis arba nelyginis

#     if num % 2 == 0:  # Checks if num/2 has a remainder of 0
#         return "even"  # If it has a remainder of 0, return "even"
#     else:
#         return "odd"  # If it doesn't, return "odd"

# print(even_odd(0.99)) #patikrina ar irasytas skaicius lyginis ar nelyginis

#----------------------------------------------------------

# 2. Create a function that adds a string ending to each member in a list.

# def add_string_beginning(list, beginning):
#     return [beginning + item for item in list]

# my_list = ['good', 'bad', 'better']
# string_beginning = 'the '
# new_list = add_string_beginning(my_list, string_beginning)
# print(new_list)

# for item in new_list:
#     print(item)


#----------------------------------------------------------

# 3. Create a mini python program which would take two numbers as an input and would return their sum, subtraction, division, multiplication.

# num1 = int(input("Ivesk pirma skaiciu: "))
# num2 = int(input("Ivesk antra skaiciu: "))

# def find_sum(num1, num2): 
#     sum_nums = num1 + num2 
#     return sum_nums  

# result = find_sum(num1, num2)
# print("suma:", result) 

# def find_substr(num1, num2): 
#     substr_nums = num1 - num2 
#     return substr_nums  

# result = find_substr(num1, num2)
# print("atimtis:", result) 

# def find_division(num1, num2): 
#     divide_nums = num1 // num2 
#     return divide_nums  

# result = find_division(num1, num2)
# print("dalyba:", result) 

# def find_multi(num1, num2): 
#     multi_nums = num1 * num2 
#     return multi_nums  

# result = find_multi(num1, num2)
# print("daugyba:", result) 


# kito studento

# from typing import Tuple

# def math(a: int, b: int) -> Tuple[int, int, float, float]:
#     addition = a + b
#     subtract = a - b 
#     division = a / b
#     multiply = a * b
#     return addition, subtract, division, multiply

# while True:
#     user_input1 = input("Insert a number ")
#     if not user_input1.isdigit():
#         print("The value is not a number, please try again")
#         continue
#     else:
#         user_input1 = int(user_input1)

#     while True:
#         user_input2 = input("Insert a second number ")
#         if not user_input2.isdigit():
#             print("The value is not a number, please try again")
#         else:
#             user_input2 = int(user_input2)
#             break
#     break

# result = math(user_input1, user_input2)
# print(result)

# kito studento

# def math(a: int, b: int) -> tuple[int, int, float, float]:
#     addition = a + b
#     subtract = a - b 
#     division = a / b
#     multiply = a * b
#     return addition, subtract, division, multiply

# def get_user_number() -> int:
#     while True:
#         user_input = input("Insert a number ")
#         if not user_input.isdigit():
#             print("The value is not a number, please try again")
#             continue
#         else:
#             user_input = int(user_input)
#             break
#     return user_input

# user_input1 = get_user_number()
# user_input2 = get_user_number()

# result = math(user_input1, user_input2)
# print(result)

# dar kito studento:
# def calculate():
#     num1 = int(input("Input first number "))
#     num2 = int(input("Input second number "))
 
#     sum = num1 + num2
#     sub = num1 - num2
#     if num2 != 0:
#         div = num1 / num2
#     else:
#         div = None
#     multi = num1 * num2
 
#     print(f"Sum of number {num1} and number {num2} is {sum}")
#     print(f"Subtraction of number {num1} and number {num2} is {sub}")
#     if num2 !=0:
#         print(f"Division of number {num1} and number {num2} is {div}")
#     else:
#         print(f"The world has ended because of you. You tried to devide by zero. ")
#     print(f"Multiplication of number {num1} and number {num2} is {multi}")
# calculate()

# 4. Create a function that returns only strings with unique characters.

# def has_unique_char(s): #characters
#     return len(s) == len(set(s)) #length

# def unique_character_strings(strings):
#     return [s for s in strings if has_unique_char(s)]

# input_strings = ["mama", "tetis", "vaikai", "senelis", "mociute"]
# unique_strings = unique_character_strings(input_strings)
# print("Strings with unique characters:", unique_strings)


# #kito studento

# def unique_strings(lst: list) -> list:
#     def has_unique_chars(s):
#         return len(s) == len(set(s))
#     return [s for s in lst if has_unique_chars(s)]

# lst ["mama", "tetis", "vaikai", "senelis", "mociute"]

# result = unique_strings(lst)
# print(result)

# 5. Write a program that defines a function called extract_email_addresses() 
# that takes a text as input and extracts all email addresses from the text.


# import re

# while True:
#     user_input = input("Iveskite teksta: ") #prasys ivesti, kol neives, tol ismes
#     if len(user_input) != 0:
#         break #sitas sako, kad isstojame is ciklo

# print(f"Ivedete: {user_input}")

# def extract_email_addresses(text):
#     email_patern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
#     find_email = re.findall(email_patern, text)
#     return find_email

# emails = extract_email_addresses(user_input)

# if emails:
#     print("Jusu tekste rastas sis el.pastas: ", ' '.join(emails))
# else:
#     print("Jusu tekste nerasta el. pastu")

# kito studnto

from typing import List

def get_email(text: str) -> List[str]:
    
    text_list = text.split()
    contains_at = [word for word in text_list if '@' in word]
    contains_point = [word for word in contains_at if '.' in word.split('@', 1)[1]]
    return contains_point

text = input('Insert text with emails: ')

answer = get_email(text)

print(answer)
