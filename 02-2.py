# lesson 03 List ir Tuple #Homework 0721
my_list = ["dog", "cat"] # Instantiating empty list
print(my_list)

my_list = []

name = "Good boy"
my_list.append(name)
print(my_list)

my_list2 = [9, 8, 7 ,5 ,3 ,1]
print(my_list2.count(1)) # 2
my_list2.insert(0, 50) # pirmas skaicius nurodo kur itraukti, antras skaicius yra reiksme
print(my_list2) 
# [1, 50, 1, 2, 3, 4, 5]

my_list2.remove(5) #sitas jau nurodo ka konkreciai ismesti, o ne kuri
print(my_list2)

my_list2.remove(my_list2[-1]) # removing last item from the list - atskaiciuoja atbulai
print(my_list2) 
 
my_list3 = ["name", 123, None, True] # len reiskia length
print(len(my_list3)) # rodo kiek realiai yra objektu, siuo atveju keturi

my_list4 = [50, 99, 1, -50]
print(max(my_list4)) #siuo atveju pasako koks skaicius yra didziausias
print(min(my_list4)) #siuo atveju pasako koks skaicius yra maziausias

my_list5 = [1, 2, 3]
for item in my_list5:
    print(item) #isvardina reiksmes paeiliui

for item in my_list5:
    print(item + 20) #prideda prie reiksmiu 20

my_list5[0] = 100 #vietoje nurodyto is eiles skaiciaus pakeicia reiksme i lauztiniuose skliaustuose esancia
print(my_list5) 

my_list6 = ["first", "second", "third"]
print(my_list6[-1]) #pasako kuri reiksme yra paskutine - t.y. pirma nuo galo
print(my_list6[:1]) #grąžina sąrašą su pirmąja reikšme
print(my_list6[::2]) #grąžina kiekvieną antrą reikšmę sąraše.
print(my_list6[::-1]) #isvardina atvirkstine eiles tvarka
print(my_list6[0:2]) #duoda nuo pradzios ir dvi reiksmes

my_list7 = ["dog", 2, 3] 
print("dog" in my_list7) #pasitikrinti, ar yra ta reiksme sarase, atsakys true arba false, veikia ir su stringais

#TUPLE - nekintantis, statinems, nesikeiciancioms reiksmems
empty_tuple = ()
tuple_single_item = (1,) # Atkreipkite dėmesį, kad po kiekvieno elemento tuple turi būti kablelis, nors gali būti tik vienas elementas. Visa kita yra tas pats, kaip ir list'e.
another_tuple = (1, 2, 3)
my_tuple = (1, 2, 3)

number1 = int(input("Ivesk pirma skaiciu: "))
number2 = int(input("Ivesk antra skaiciu: "))
number3 = int(input("Ivesk trecia skaiciu: "))
my_tuple2 = (5)
number4 = my_tuple2
print(max(number1, number2, number3, number4))

