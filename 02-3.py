# lesson 04 - Dictionary #Homework 0721
# Tai labai pravarti duomenų struktūra, kuri bus dažnai naudojama kodo struktūrizavimo procese. 
# Dictionary yra sudaromas iš rakto (key) ir vertės (value) porų (pairs): {key: value}.

#du budai kaip sukurti dictionary
# my_dictionary = {}
# my_dictionary["name"] = "Tom"
# print(my_dictionary["name"])

#arba antras:
# my_dictionary = {"name": "Tom"}
# print(my_dictionary["name"])

# my_dictionary = {"name": "Tom", "surname": "Edison"} #cia sukuriamas dictionary
# print(f"name: {my_dictionary['name']}") #cia paprasome duoti reiksmes
# print(f"surname: {my_dictionary['surname']}") #ir cia

# my_dictionary = {"name": "Tom", "surname": "Edison"} 
# print(f"favourite car: {my_dictionary['car']}") 
#jei zodinely nera ivestos reiksmes, tai duos Keyerror
# KeyError: 'car' 

# my_dictionary = {"name": "Tom", "surname": "Edison"}
# my_dictionary["name"] = "Charles" #kaip pakeisti reiksmes
# print(f"name: {my_dictionary["name"]}") #atgal duoda Charles, nes pakeiteme is Tom zodinelyje

# my_dictionary = {"name": "Tom", "surname": "Edison"}
# del my_dictionary ["name"] #kaip istrinti reiksme is zodinelio, siuo atveju name dali
# print(my_dictionary) #rodo visa zodineli

user_info = { #neprivaloma vadinti dictionary, gali buti ir user_info arba bet kas kitas
#svarbu, kad butu su { } skliaustais, reiksmes kabutese " " ir po dimensijos : o tada reiksme
	"name": "Albert",
	"surname": "Einstein",
	"occupation": {
		"role": "Professor",
		"workplace": "University of Berlin"
	},
        "languages": ["German", "Latin", "Italian", "English", "French"] 
        #reiksmes galima isvardyti dedant siuos skliaustus [ ], kableli po kiekvienos ir nepamirsti uzdaryti siuo skliaustu }
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
    print(language) #isspausdina visas kalbas, t.y. pasirinktas reiksmes

#zodinelio iteravimui 
d = {'a': 10, 'b': 20, 'c': 30} #cia pakurtas naujas zodinelis
print(list(d.items())) #cia praso duoti visas zodinelio dalis: ir dimensija ir kas viduje - reiksmes

list(d.keys()) #duoda visus pavadinimus dimensiju
print(list(d.keys()))  #juos isspausdina

list(d.values()) #duoda visus pavadinimus reiksmiu
print(list(d.values()))  #juos isspausdina


result = d.pop('a') 
print(result)  #duoda a reiksme, bet tada ja ismeta is zodinelio
print(d) #grazina zodineli jau be sitos dimensijos ir reiksmes

#kaip papildyti zodineli kitu zodineliu ir pakeisti reiksmes
dict_one = {'a': 10, 'b': 20, 'c': 30} 
dict_two = {'b': 200, 'd': 400} #sukuriamas antras zodinelis
dict_one .update(dict_two) 
#pridedamos antro zodinelio reiksmes, b yra pakeiciamas kita reiksme, t.y. vietoje 20, i 200
# o d pridedamas, nes tokio nebuvo
print(dict_one) #printinamas nauja zodinelio versija

#cia tas pats, tik kitas variantas
dict_one .update([('b', 200), ('d', 400)]) 
print(dict_one)

#cia tas pats, tik dar kitas variantas
dict_one = {'a': 10, 'b': 20, 'c': 30}
dict_one .update(b=200, d=400)
print(dict_one)

# kaip iteruoti per dict - t.y. kad ismetytu visas reiksmes atskirai po viena apacioje
d = {'a': 10, 'b': 20, 'c': 30}
for key, value in d.items():
    print(key, value)

# Dviejų list konvertavimas į dict - kaip apjungti du sarasus, bet sukuriant atskiras savybes, t.y. dimensijas ir reiksmes
test_keys = ["Albert", "Tom", "Stephen"] #sitie yra dimensijos
test_values = [1, 4, 5] #o sitie reiksmes
my_dictionary= dict(zip(test_keys, test_values))
print(my_dictionary)

#sets - aibes, kurios nekeiciamos, bet galima jas istrinti
my_set = {1, 2, 3}
my_set = {1, 2, 3, 1} #negali buti dublikatu, neduos antrojo vieneto
print(my_set)
# {1, 2, 3}

numbers_list = [1, 2, 3, 4, 5, 5, 5, 5, 6] #tai galima naudoti gauti unikales reiksmes
numbers_set = set(numbers_list)
print(numbers_set)
# {1, 2, 3, 4, 5, 6}

