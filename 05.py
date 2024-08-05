
# import math

# print(math.pi)
# area = 5 * 5 * math.pi

# print(area)


# print(math.ceil(6.1))

# print(math.floor(-11.1))


#exercises

# 1. Find all of the numbers from 1-1000 that are divisible by 6.

# divisible_by_six = [number for number in range(1, 1000) if number % 6 == 0]
# print(divisible_by_six)

# 2. Find all number from 1-1000 that have 9 in them.

# nine_in_them = [number for number in range(1, 1000) if '9' in str(number)]
# print(nine_in_them)

# 3. Given string: text = 'In this lecture we will review some additional 
# functionalities of python built-in data structures.' calculate how many words have letter e in it.

# text = 'In this lecture we will review some additional functionalities of python built-in data structures.'
# letter_e = [word for word in text.split() if 'e' in word]
# print(f"Number of words containing 'e': {len(letter_e)}")

#kitas pvz
# input_text = input("Ivesk teksta: ")
# words_with_e = [word for word in input_text.split() if 'e' in word]
# print(f"Number of words containing 'e': {len(words_with_e)}")

# kito studento
# text = 'In this lecture we will review some additional functionalities of python built-in data structures'
# string = text.split(" ")
 
# result = [1 for char in string if 'e' in str(char)]
# print(sum(result))

# 4. Given the same string as in previous exercise: calculate count of words that have more than 5 characters.

# text = 'In this lecture we will review some additional functionalities of python built-in data structures.'
# five_char = [word for word in text.split() if len(word) > 5]
# print(f"Words that have more than five characters': {len(five_char)}")

#kitas pvz

# input_text = input("Ivesk teksta: ")
# five_char = [word for word in input_text.split() if len(word) > 5]
# print(f"Words that have more than five characters': {len(five_char)}")


# 5. Given the same string calculate the occurrence of each letter in the string. (HINT: store everything in dictionary)

# text = 'In this lecture we will review some additional functionalities of python built-in data structures.'

# # Initialize an empty dictionary to store the counts
# letter_count = {}

# # Iterate through each character in the string
# for char in text:
#     # Convert the character to lowercase to count letters case-insensitively
#     char = char.lower()
#     if char.isalpha():  # Check if the character is a letter
#         if char in letter_count:
#             letter_count[char] += 1
#         else:
#             letter_count[char] = 1

# print(letter_count)


#kito studento:
text = 'In this lecture we will review some additional functionalities of python built-in data structures'
string = text.replace(" " and "-", "")
my_dict = {}
 
for char in string:
    if char not in my_dict:
        my_dict[char] = 1
    else:
        my_dict[char] += 1
 
print(my_dict)

# # 6. Write a program that checks if given number is a perfect square.

# import math

# def is_perfect_square(number):
#     if number < 0:
#         return False
#     sqrt = math.isqrt(number)  # Use integer square root for exact comparison
#     return sqrt * sqrt == number

# # Test the function with some numbers
# test_numbers = [16, 25, 26, 0, -4, 100]

# for number in test_numbers:
#     result = is_perfect_square(number)
#     print(f"{number} is a perfect square: {result}")
