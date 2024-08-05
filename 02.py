# Classwork about 03 and 04 on 0718
my_list = []
name = "Gabriele"
# append padeda nauja elementa i saraso gala
my_list.append(name)
my_list.append(name)
my_list.append(name)
my_list.append(name)

print(my_list)

my_list.insert(1, "Ona")

print(my_list.count("Ona"))

my_list.remove(my_list[-1]) #removing last item from the list

print(my_list)
print(my_list.count("Ona")) # len - kiek elementu sarase (len yra length)

print(len(my_list))

my_list = [49, 89, 2, 48]
print(min(my_list))

# kaip prideti papildoma skaiciu prie kiekvieno skaicius is my_item, galima vadinti ir ne my_item kaip tik norisi
for item in my_list:
    print(f"item's name is ")
    print(item)
    print(f"item + 1 = {item+1}")


my_list = ["first", "third", "second"]
print(my_list)
print(my_list[-1])
print(my_list[:1])
print(my_list[::2])
print(my_list[::-1])
print(my_list[:2])

print(49 in my_list)
my_list.sort()

print(my_list)

my_list.append(5000)
print(my_list)


own_list = []

# 
name = "Tom"
print(name)
own_list.append(name)
print(own_list)
own_list = [1, 2, 3, 3]
print(own_list.count(1)) # 2
own_list = [1, 2, 3]
own_list.insert(4, 5)
print(own_list)

own_list.remove(2)
print(own_list)

my_list3 = [1, 1, 2, 3, 4, 5]
my_list3.remove(my_list3[-3])
print(my_list3)

my_list = ["name", 12346, None, True, "Tom"]
print(len(my_list)) 

my_list = [50, 99, 1, -50]
print(max(my_list))

my_list = [50, 99, 1, -50]
print(max(my_list))

print(min(my_list))

# Exercise 1 Write a python program that sums up all items in the list  - all items are integers or floats in list, create a list yourself.
my_list4 = [1, 1, 9, 1, 5, 5]
print(my_list4)
total1 = sum(my_list4)
print(total1)

# Exercise 2 Write a python program that multiplies all items in the list (all items are integers or floats in list, create a list yourself).my_list4 = [1, 1, 9, 1, 5, 5]
my_list5 = [2, 2, 2]
import math
print(my_list5)
total5 = math.prod(my_list5)
print(total5)

# Exercise 3 Parašykite python programą, kuri iš list'o gauna didžiausią vertę (visi list elementai yra int arba float tipo. List'a sukurkite patys).
my_list4 = [1, 1, 20, 1, 5, 5]
print(my_list4)
total1 = sum(my_list4)
print(max(my_list4))


# Exercise 4 Parašykite python programą, kuri sujungia visas list esančias string duomenų tipo reikšmes (visi elementai yra string tipo, list'a sukurkite patys)
my_list8 = ["dog", "cat"]
my_list9 = ["seventh", "third"]
completed2 = f"{my_list8} {my_list9}"
print(completed2)

#alternatyvus
my_list = ["one", "two", "three", "four"]
 
a = " "
for i in my_list:
    a = a + " " + i
 
print(a)

#alternatyvus
my_list = ["My", "new", "hobby", "is", "learning", "Python"]
sentence = " ".join(my_list)
print(sentence)

# Exercise 5 Sukurkite du list'us ir juos sudėkite, įsitikinkite, kad viskas veikia taip, kaip norite.
my_list10 = [5, 3, 2]
my_list11 = [1, 1, 1]
total2 = sum(my_list10)
print(total2)
total3 = sum(my_list11)
print(total3)
completed3 = total2 + total3
print(completed3)

#alternatyvus
list_a = ["first", "second", "third"]
list_b = [8, 10, 9]
list_c = []
 
j = 0
for i in list_a:
    k = list_b[j]
    list_c.append(i)
    list_c.append(k)
    j = j + 1
 
print(list_c)

# Exercise 6 Parašykite python programą, kuri paprašytų naudotojo įvesti 3 int tipo skaitmenis (1,2,3 etc..) ir rastų didžiausią įvestą reikšmę.
number1 = int(input("Ivesk pirma skaiciu: "))
number2 = int(input("Ivesk antra skaiciu: "))
number3 = int(input("Ivesk trecia skaiciu: "))
print(max(number1, number2, number3))

# Exercise 7 su tuples (konstanta?)
number1 = int(input("Ivesk pirma skaiciu: "))
number2 = int(input("Ivesk antra skaiciu: "))
number3 = int(input("Ivesk trecia skaiciu: "))
my_tuple = (5)
number4 = my_tuple
print(max(number1, number2, number3, number4))

#dictionary
my_dictionary = {"name": "Tom", "surname": "Edison"}
print(f"name: {my_dictionary['name']}")
print(f"surname: {my_dictionary['surname']}")

my_dictionary = {"name": "Tom", "surname": "Edison"}
my_dictionary["name"] = "Charles"
print(f"name: {my_dictionary["name"]}")

my_dictionary = {"name": "Tom", "surname": "Edison"}
del my_dictionary ["name"]
print(my_dictionary)

user_info = {
	"name": "Albert",
	"surname": "Einstein",
	"occupation": {
		"role": "Professor",
		"workplace": "University of Berlin"
	},
        "languages": ["German", "Latin", "Italian", "English", "French"]
}

user_info = {
	"name": "Albert",
	"surname": "Einstein",
	"occupation": {
		"role": "Professor",
		"workplace": "University of Berlin"
	},
        "languages": ["German", "Latin", "Italian", "English", "French"]
}

for language in user_info["languages"]:
    print(language)

print("French" in user_info ["languages"])

#iteravimas
d = {'a': 10, 'b': 20, 'c': 30}
print(list(d.items()))

for key, value in d.items():
    print(f"key is: {key}, value is {value}")



