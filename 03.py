# is 5os paskaitos
number_one = 700
number_two = 600
if number_one > number_two :
    print("number_one is greater than number_two !")

elif number_one == number_two: #else if 
    print("Numbers are equal !")

# jei jau viena atspaudina, toliau nebeina

number_one = 500
number_two = 600
if number_one < number_two :
    print("number_one is greater than number_two  !")
elif number_one == number_two :
    print("numbers are equal !")
else: #else yra visais kitais atvejais (galutinis), jei pries tai buve nesiaktyvuoja
    print("number_two is greater than number_one !")


# pasizaidimas:

number_one = 1
number_two = 2
if number_one > number_two :
    print("number_one is greater than number_two !")

elif number_one != number_two: #else if 
    print("Numbers are not equal !")

else: #else yra visais kitais atvejais (galutinis), jei pries tai buve nesiaktyvuoja
    print("number_two is greater than number_one !")

score = int(input("Score: "))
 
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")

#budas viena eilute, bet dev nemegsta sito
a = 200
b = 450
print("A") if a > b else print("B") #one line naudojamas jei naudosi viena karta

a = 200
b = 200
print("A") if a > b else print("=") if a == b else print("B") 

#and
a = 200
b = 400
c = 500
if c > a and c > b:
    print("C is the greatest of them all!")

#or
a = 200
b = 400
c = 500
if b > a or b > c:
    print("B is at least greater than one of the values !")



#nested if
x = 15

if x > 10:
  print("Above 10")
  if x > 20:
    print("and also above 20!")
  else:
    print("Above 10 but bellow 20!.")

# pass reiskia nieko nedaryk, praleisk

a = 50
b = 80

if b > a:
  pass

# o ka galima padaryti su tekstu - stringais

name = "Tom"

if name == "Tom":
    print("Nice to see you Tom")
else:
    print("welcome, user")

#jei yra priveligijuoti vartotojai arba adminai
user = "Johnny"
privileged_users = ["Tom", "Albert", "Stephen"]
if user in privileged_users:
    print(f"Welcome home {user}")
else:
    print("INTRUDER ALLERT. Silently calling police...")

my_dict = {"name": "Steven", "born": "1955-02-24", "interests": "Apples"}
if my_dict["name"] == "Steven":
    print("This guy does not like Windows")
else:
    print("No clue who this is")

my_dict = {"name": "Bill", "born": "1955-10-28", "interests": "small software"}
if "Bill" in my_dict.values():
    print("This guy hates apples")
else:
    print("No clue who this is")

...
if name != "":
  print("Name was not entered")
...

...
if len(name) == 0:
  print("Name was not entered")
...

if not name:
  print("Name was not entered")

my_list = []
if not my_list:
  print("oh no, list is empty")

#is 8os paskaitos
i = 0
while i < 10:
  print(i)
  i += 1

#endless loop
while True:
    user_input = input("Enter your name: ") #prasys ivesti, kol neives, tol ismes
    if len(user_input) != 0:
        break #sitas sako, kad isstojame is ciklo
print(f"You entered {user_input }")

#for leidzia iteruoti per elementus, listus, dict, ciklus ir generatorius
names = ["Albert", "Tom", "Leonardo"]
for name in names:
    print(f"Greetings, {name}")

name = "Code Academy" #iteruoti per kiekviena raide
for character in name :
    print(character)

my_dict = {"name": "Albert", "role": "scientist"} #per dict

for key, value in my_dict.items():
    print(key, value)

#range nuo kur iki kur
x = range(3, 6) #nuo 3 iki 6
for n in x:
  print(n)

i = 1
while i < 6:
  print(i)
  if i == 3:
    break #visiskai sustabdo loopa
  i += 1

i = 0
while i < 6:
  i += 1
  if i == 3:
    continue #tai vadinasi sok atgal i loopo pradzia
  print(i)


  