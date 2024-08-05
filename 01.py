# Lessons 00 and 01 + classwork on 07-15
a = 1
b = 3
c = a + b
print(a)
print(b)
print(c)
name = "Mano namas"

#String operations
print(name)
print(name[3])
print(name[-2])
print(name[0:3])
print(name[ :2])
print(name[::-1])
print(name.split())
print(name.upper())
print(name.replace('M', 'T'))
print(name[-1])
print(name[-2])
print(name.upper())
print(name.replace('s', 'i'))

# Combining of string
greeting = "Hi, my name is"
name = "Gabriele"
completed_greeting = f"{greeting} {name}"
print(completed_greeting)
# or
completed_greeting = greeting + " " + name
print(completed_greeting)

# Conversion types
str()
int()
float()

c = 4
d = int(c)
print(d)

e = "55"
f = int(e)
g = float(e)

e = 55
f = str(e)
g = float(e)
print(e)
print(f)
print(g)

# User input - it was error in the example, no brackets
name = input("Enter your name: ")
age = input("Enter your age: ")
print(f"Your name is {name}, you are {age} years old")

# Exercise 1. Enter surname and year user was born, calculate the age. Datetime duoda dabarties data
# f naudojamas kai norime kazka sujungti
import datetime
surname = input("Enter your surname: ")
birthyear = int(input("Enter you birth year: "))
print(f"Your surname is {surname}, your birth year is {birthyear}")
currentyear = datetime.datetime.now().year
exactage = currentyear - birthyear
print(f"Your age is {exactage}")

# Exercise 2. User enters full sentence, then it is made backwards, then capital letters and then very second letter is printed only
#galima iskart dvitaski
sentence = input("Enter your sentence: ")
result = sentence[1::2]
result1 = sentence[::2]
print(result)
print(result1)
print(sentence[::-1])
print(sentence.split())
print(sentence.upper())

# Exercise 3. User enters number, then multiple that number
number = int(input("Enter your number: "))
result2 = number * 2
print(result2)
result3 = number + 5
print(result3)
result4 = number / 2
print(result4)

# Exercise 4. User enters text, convert text to Leet speak 1337, print
def to_leet_speak(text):
    leet_dict = {
        'A': '4', 'a': '4',
        'E': '3', 'e': '3',
        'I': '1', 'i': '1',
        'O': '0', 'o': '0',
        'S': '5', 's': '5',
        'T': '7', 't': '7'
    }
    
    # Use a list comprehension to replace characters
    leet_text = ''.join(leet_dict.get(char, char) for char in text)
    return leet_text

# Get user input
input_text = input("Enter a text for leet: ")

# Convert to leet speak
leet_text = to_leet_speak(input_text)

# Print the result
print(leet_text)
