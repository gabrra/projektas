feels = input("How do you feel today - answer in a sentence: ")
breakfast = input("What did you eat for breakfast - answer in a sentence: ")
plans = input("What are your plans for today - answer in a sentence: ")

d = {'feelings': feels, 'food': breakfast, 'activities': plans}
print(d)

for key, value in d.items():
    print(key, value)
    
a = feels
print(len(a))
b = breakfast
print(len(b))
c = plans
print(len(c))