# uzduotys 08

#1. Create a variables containing strings for username and password. 
# Start endless loop allowing to enter username and password. #
# If credentials are correct stop endless loop and print greeting message.

while True:
    user_input = input("Enter your username: ")
    if user_input == "gabi":
        break
while True:
    user_passw = input("Enter your password: ")
    if user_passw == "1234":
        break
print(f"Welcome {user_input }")


# 2. Allow user to enter 10 integers, and then print the sum and average of those entered numbers.

while True:
    user_input1 = input("Enter number1: ")
    if len(user_input1) != 0:
        break
while True:
    user_input2 = input("Enter number2: ")
    if len(user_input2) != 0:
        break
while True:
    user_input3 = input("Enter number2: ")
    if len(user_input3) != 0:
        break  
while True:
    user_input4 = input("Enter number2: ")
    if len(user_input4) != 0:
        break  
print(f"You entered {user_input }")



# 3. Generate a dictionary of 10 keys (1,2,3...10). Each of them should store a value of random integer number from 1 to 100.
# 4. Create a pin code cracker. Let's say pin code consists of 4 random digits. 
# You can store the value in variable. 
# Then create a loop going through all possible combinations until you find the one you entered.
# 5. Create a program that allows a user to enter a series of numbers, and then calculates the average of all the numbers. 
# The program should also print the list of all the numbers, as well as the average.