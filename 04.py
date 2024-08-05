# 10 lesson funkcijos



# Function to print 'Hello world!'
# def print_smth():
#     print('Hello world!')

# # # Call the function - kaip iskviest funkcija, reikes visais atvejais - tiesiog funkcijos pavadinimas ir () 
# print_smth()

# # Import the random module
# import random #isidedam sita, jei norime gauti random skaiciu nuo 1 iki 10

# def get_random_number(): #vadiname viska mazosiomis, tarp zodziu dedame underscore _ ir funkcija turi buti pavadinta veiksmazodziu
#     print(random.randint(0, 10))

# # # Call the function
# get_random_number()

# # -----------------------

# import random #isidedam sita random moduli, jei norime gauti random skaiciu nuo 1 iki 10

# def get_random_number(): #vadiname viska mazosiomis, tarp zodziu dedame underscore _ ir funkcija turi buti pavadinta veiksmazodziu
#     return random.randint(0, 10) #random integer - randint

# def find_sum(num1, num2): #i musu funkcija paduodami du variables numeris 1 ir numeris 2/ cia num skaiciai yra lokalus
# #     '''Returns the sum of num1 and num2.''' #return yra rezultatas, ka mums grazina funkcija
# # sito ''' nebutinai reikia, kad funkcija veiktu
#     sum_nums = num1 + num2  # Finds the sum of num1 and num2
#     return sum_nums  # Returns the sum of the numbers


import random


def get_random_number():
    return random.randint(0, 10)

def find_sum(num1: int, num2: int, num3: int=0) -> int: #kaip padaryti, kad num3 pagal default butu 0, sitie turi buti paskutiniai
    sum_nums = num1 + num2 + num3
    return sum_nums  

number = find_sum(1, 2) #num1 = 1, num2= 2 siuo atveju, o num3 by default 0, nes pries tai parasyta funkcijoje. 
#Jei nuli ismesime, tada duos error           ^^^^^^^^^^^^^^
#TypeError: find_sum() missing 1 required positional argument: 'num3'
#jei vsigi bus paduotas trecias skaicius cia, tada sumuos

print(number)


# #kiti zenklai:
# # Sum: sum_nums = num1 + num2
# # Subtraction: difference_nums = num1 - num2
# # Multiplication: product_nums = num1 * num2
# # Division: quotient_nums = num1 / num2 (This performs true division and results in a float.)
# # Floor Division: floor_division_nums = num1 // num2 (This performs division and rounds down to the nearest integer.)
# # Modulus: remainder_nums = num1 % num2 (This finds the remainder after division.)
# # Exponentiation: power_nums = num1 ** num2 (This raises num1 to the power of num2.)

# something = get_random_number()
# print(something) #galima naudoti random skaiciu spejime

# print(find_sum(10, 5)) #paduodu du argumentus i sita funkcija ir gaunu random numeri ir tada 15

# #neprivaloma rasyti num1 arba num2, galima rasyti number1 ir number2

# number1 = 30 #sitie number skaiciai yra globalus
# number2 = 50

# print(find_sum(number1, number2))

# number3 = 350
# number4 = 400

# print(find_sum(number3, number4))


# # Call the function with two arguments
# result = find_sum(3, 5)
# print(result)  # This should print 8

# # -------------------------------

# def get_random_number():
#     return random.randint(0, 10)

# def find_sum(num1: int, num2: int, num3: int=500) -> int:
#     sum_nums = num1 + num2 + num3
#     return sum_nums

# number = find_sum(1, 2)

# print(number)

# # -------------------------------
# def even_odd(num): #skaicius lyginis arba nelyginis

#     '''
#     Returns "even" if num is even, and "odd" if num is odd.    #even lyginis #odd nelyginis
#     Parameters:
#         num (int): Any integer    Returns:
#         type (string): "even" if num is even; "odd" if num is odd
#     '''

#     if num % 2 == 0:  # Checks if num/2 has a remainder of 0
#         return "even"  # If it has a remainder of 0, return "even"
#     else:
#         return "odd"  # If it doesn't, return "odd"

# print(even_odd(10)) #patikrina ar irasytas skaicius lyginis ar nelyginis

# def check_if_exist(a=None):  #jei tuscia returne,  tai grazinks nieko
#   if a:
#     return a
#   return
    

# def integer_division(num_one, num_two):
#     return num_one // num_two # sitas // reiskia, kad suapvalins iki sveiko skaiciaus

# integer_division(10, 2) #pagal sita eiliskuma kaip paduosim, taip ir naudos, 


# def integer_division(num_one=10, num_two=2): #tokiu atveju sitie bus kaip default skaiciai
#     return num_one // num_two

# integer_division() 

# print(integer_division())


#bet jei noretume apkeisti vietomis:

# def integer_division(num_one, num_two): 
#     return num_one / num_two


# print(integer_division(num_two=100, num_one=200))



# def integer_division(num_one, num_two): 
#     return num_one / num_two

# print(integer_division(100, 200))

#---------------------------------------

# def add_two_int_numbers(a,b): 
#   return a + b #sudeda su integerius - skaicius, bet gali sudeti ir teksta


# print("labas" + " " + "vakaras")


# def add_two_int_numbers(a: int, b: int) -> int: #jei norime sudeti skaicius, rodiklyte rodo ka norime gauti, ka grazina
#   return a + b

# print(add_two_int_numbers("labas", "vakaras"))


#---------------------------
#galima apsirasyti tipus

# type_annotation_int: int = 43
# type_annotation_float: float = 2.54
# type_annotation_string: str = 'efe'
# type_annotation_bool: bool = True

# from typing import List, Tuple, Dict, Union, Optional
# type_annotation_tuple: Tuple[str] = ('1','2','3') 
# type_annotation_list: List[str] = ['a', 'b', 'c'] #str nurodo, kad viduje tik stringai
# type_annotation_dict: Dict[str, int] = {'a': 1, 'b': 2} #key yra kairej str, value desinej int

# from typing import List, Dict, Union #union - sajunga tarp dvieju integerio ir float
# uniontype_annotation_list: List[Union[float,int]] = [1.23, 3.32, 1, 3]
# type_annotation_dict: Dict[str, Union[float,int]] = {'a': 1, 'b': 2}

# type_annotation_list: List[float | int]= [1.23, 3.32, 1, 3]

# type_annotation_list: List[Optional[int]] = [1, 3]

# from typing import Tuple, Optional, Union #optional gali reiksti, kad paduodamas dalykas arba nepaduodamas, gali buti ir none

# def the_func(x: Union[int, float], y: Tuple[str, str], z: Optional[float] = None) -> str:
#    return 'You called the_func with ' + str(x) + str(y) + str(z)

#-----------------------
#pataisytas variantas

# Correcting type annotations
# type_annotation_int: int = 43
# type_annotation_float: float = 2.54  # Using a dot instead of a comma for the float value
# type_annotation_string: str = 'efe'
# type_annotation_bool: bool = True

# from typing import List, Tuple, Dict, Union, Optional

# # Correcting the variable name and Tuple type annotation
# type_annotation_tuple: Tuple[str, str, str] = ('1', '2', '3')  # Adding multiple types for tuple elements
# type_annotation_list: List[str] = ['a', 'b', 'c']
# type_annotation_dict: Dict[str, int] = {'a': 1, 'b': 2}

# # Including all necessary imports and correcting type annotations
# uniontype_annotation_list: List[Union[float, int]] = [1.23, 3.32, 1, 3]
# type_annotation_dict_union: Dict[str, Union[float, int]] = {'a': 1, 'b': 2}

# # Alternative way of specifying Union types (Python 3.10+)
# type_annotation_list_union: List[float | int] = [1.23, 3.32, 1, 3]

# # Using Optional type annotation
# type_annotation_list_optional: List[Optional[int]] = [1, 3, None]  # Added None to illustrate Optional

# # Correcting function definition
# def the_func(x: Union[int, float], y: Tuple[str, str], z: Optional[float] = None) -> str:
#     return 'You called the_func with ' + str(x) + str(y) + str(z)
