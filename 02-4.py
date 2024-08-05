# Homework for topic 04, 07-21

#1. Parašykite python programą, kuri paprašytų vartotojo įvesti vardą, pavardę, amžių. 
# Įrašykite šias reikšmes į dict duomenų struktūrą ir ją išspausdinkite.

name = input("Enter your name: ")
surname = input("Enter your surname: ")
age = input("Enter your age: ")
print(f"Your name is {name}, your surname is {surname}, and you are {age} years old")

user_info = {
	"vardas": name,
	"pavarde": surname,
	"amzius": age, }

print(list(user_info.items())) 
#cia praso duoti visas zodinelio dalis: ir dimensija ir kas viduje - reiksmes


# 2. Pabandykite sukurti dict struktūrą, kurioje turite panaudoti visas jums žinomas duomenų struktūras ir tipus.

#Duomenu strukturos:
    #list
    #sets
    #tuple
    #dict


#Duomenu tipai
    #string 
    #int
    #float


my_dict = {
    "name": "Gabi",  # string 
    "age": 35, #int turi buti be kabuciu
    "vacation_days": 2.5, #float turi buti be kabuciu ir negali buti kablelio, o turi buti tas
}

print(list(my_dict.items())) #list

my_set = {2024}
print(my_set) #set ideti galima i dictionary, galima sukurti papildoma dictionary

my_tuple = (99,) #galima ideti tuple i dictionary, galima sukurti papildoma dictionary
print(my_tuple)
print(my_dict, my_set, my_tuple)



# 3. Sukurkite programą, kuri iš sakinių, kuriuos jus įvedėt, sukurtų dict, kuriame keys reikštų raides, 
# o values šių raidžių dažnumą tuose sakiniuose. Programa turi reikalauti, kad vartotojas įvestų ne mažiau kaip 3 sakinius.

feels = input("How do you feel today - answer in a sentence: ")
breakfast = input("What did you eat for breakfast - answer in a sentence: ")
plans = input("What are your plans for today - answer in a sentence: ")


# kito studento pvz


sentence1 = input("Please insert first sentence ")
sentence2 = input("Please insert second sentence ")
sentence3 = input("Please insert third sentence ")
all_sentences = sentence1 + sentence2 + sentence3
 
char_amount = {}
 
for char in all_sentences: #char yra kitamasis - for each
    if char not in char_amount:
        char_amount[char] = 1
    else:
        char_amount[char] += 1
 
print(char_amount)
#cia svarbu buvo kad dictionary sukurtu ir raides butu keys o raidziu kiekis butu key value


#nepabaigiau, reikia pagalbos

#text = feels + " " + breakfast + " " + plans
#letter_count = {}

#for char in text:
    #if char.isalpha():  # Tik skaičiuojame raides, ne tarpus ar skyrybos ženklus
     #   char = char.lower()  # Ignoruojame didžiąsias ir mažąsias raides
       # if char in letter_count:
        #    letter_count[char] += 1
        #else:
         #   letter_count[char] = 1

# Atspausdinti rezultatus
#print(letter_count)


#d = {'feelings': feels, 'food': breakfast, 'activities': plans}
#print(d)

#for key, value in d.items():
#    print(key, value)
    
#a = feels
#print(len(a))
#b = breakfast
#print(len(b))
#c = plans
#print(len(c))
#print(type(a), type(b), type(c))

#my_list = [len(a), len(b), len(c)]
#print(my_list)


#nepabaigiau, reikia pagalbos

# 4. Sukurkite studentų vardų ir jų pažymių žodyną:

#Studentų vardus saugokite kaip raktus, o jų pažymius - kaip reikšmes žodyne.
#Apskaičiuokite visų studentų vidutinį pažymį:

#Naudokite sum() ir len() funkcijas apskaičiuoti bendrą ir pažymių skaičių, atitinkamai, 
# o tada bendrąjį skaičių padalinkite iš skaičiaus, kad gautumėte vidurkį.
#Pašalinti studentus, kuriems pažymėjimai mažesni nei 80, iš žodyno:

#Naudokite set, kad sukurtumėte studentų vardų rinkinį, kurių pažymėjimai yra mažesni nei 80.

#Pažiūrėti, ar konkretus studentas egzistuoja žodyne:

#Įveskite studento vardą iš vartotojo.
#Naudokite in operatorių, norėdami patikrinti, ar studento vardas egzistuoja žodyne.
#Spausdinkite pranešimą, rodantį, ar studento vardas yra rastas, ar ne.


my_dict3 = {
    "Jonas": [10, 10, 9],
    "Ona": [2, 3, 6],}

print(list(my_dict3.items()))


#nepabaigiau, reikia pagalbos

