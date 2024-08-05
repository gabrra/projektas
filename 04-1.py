import random #isidedam sita, jei norime gauti random skaiciu nuo 1 iki 10


def get_random_number(): #vadiname viska mazosiomis, tarp zodziu dedame underscore _ ir funkcija turi buti pavadinta veiksmazodziu
    return random.randint(0, 10)

# Sum: sum_nums = num1 + num2
# Subtraction: difference_nums = num1 - num2
# Multiplication: product_nums = num1 * num2
# Division: quotient_nums = num1 / num2 (This performs true division and results in a float.)
# Floor Division: floor_division_nums = num1 // num2 (This performs division and rounds down to the nearest integer.)
# Modulus: remainder_nums = num1 % num2 (This finds the remainder after division.)
# Exponentiation: power_nums = num1 ** num2 (This raises num1 to the power of num2.)
#-------------------------------
# su minuso zenklu:

def find_difference(num1, num2): #i musu funkcija paduodami du variables numeris 1 ir numeris 2/ cia num skaiciai yra lokalus
#     '''Returns the sum of num1 and num2.''' #return yra rezultatas, ka mums grazina funkcija
# sito ''' nebutinai reikia, kad funkcija veiktu
    difference_nums = num1 - num2  # Finds the sum of num1 and num2
    return difference_nums  # Returns the sum of the numbers

something = get_random_number()
print(something) #galima naudoti random skaiciu spejime

print(find_difference(10, 5)) #paduodu du argumentus i sita funkcija ir gaunu random numeri ir tada 15

#neprivaloma rasyti num1 arba num2, galima rasyti number1 ir number2

number1 = 30 #sitie number skaiciai yra globalus
number2 = 50

print(find_difference(number1, number2))

number3 = 350
number4 = 400

print(find_difference(number3, number4))


#-------------------------------
# su daugybos zenklu:

def find_multi(num1, num2): #i musu funkcija paduodami du variables numeris 1 ir numeris 2/ cia num skaiciai yra lokalus
#     '''Returns the sum of num1 and num2.''' #return yra rezultatas, ka mums grazina funkcija
# sito ''' nebutinai reikia, kad funkcija veiktu
    multi_nums = num1 * num2  # Finds the sum of num1 and num2
    return multi_nums  # Returns the sum of the numbers


# Division: quotient_nums = num1 / num2 (This performs true division and results in a float.)
# Floor Division: floor_division_nums = num1 // num2 (This performs division and rounds down to the nearest integer.)
# Modulus: remainder_nums = num1 % num2 (This finds the remainder after division.)
# Exponentiation: power_nums = num1 ** num2 (This raises num1 to the power of num2.)

something = get_random_number()
print(something) #galima naudoti random skaiciu spejime

print(find_multi(10, 5)) #paduodu du argumentus i sita funkcija ir gaunu random numeri ir tada 15

#neprivaloma rasyti num1 arba num2, galima rasyti number1 ir number2

number1 = 30 #sitie number skaiciai yra globalus
number2 = 50

print(find_multi(number1, number2))

number3 = 350
number4 = 400

print(find_multi(number3, number4))


#-------------------------------

# su dalybos zenklu:
# Division: quotient_nums = num1 / num2 (This performs true division and results in a float.)
# Floor Division: floor_division_nums = num1 // num2 (This performs division and rounds down to the nearest integer.)
# Modulus: remainder_nums = num1 % num2 (This finds the remainder after division.)
# Exponentiation: power_nums = num1 ** num2 (This raises num1 to the power of num2.)

def find_div(num1, num2): #i musu funkcija paduodami du variables numeris 1 ir numeris 2/ cia num skaiciai yra lokalus
#     '''Returns the sum of num1 and num2.''' #return yra rezultatas, ka mums grazina funkcija
# sito ''' nebutinai reikia, kad funkcija veiktu
    div_nums = num1 / num2  # Finds the sum of num1 and num2
    return div_nums  # Returns the sum of the numbers


something = get_random_number()
print(something) #galima naudoti random skaiciu spejime

print(find_div(10, 5)) #paduodu du argumentus i sita funkcija ir gaunu random numeri ir tada 15

#neprivaloma rasyti num1 arba num2, galima rasyti number1 ir number2

number1 = 10 #sitie number skaiciai yra globalus
number2 = 5

print(find_div(number1, number2))

number3 = 100
number4 = 20

print(find_div(number3, number4))

