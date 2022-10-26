# 1 Тізімдерді, кортеждерді, жиындарды және сөздіктерді бір бағдарламаның ішінде көрсететін бағдарлама жаз. 
# Мәлеметтер ретінде әр студент өзіне байланысты ақпарат немесе резюмесін ұсыну қажет.
full_name = [] 
print('Введите ваше Ф. И. О. построчно ')
for i in range(3):
    fln = input()
    full_name.append(fln)

tuple = ('Алматы','Алатау','Дарабоз')

skills = set()

print('По очередно введите три навыка которыми вы облдаете :')
for i in range(3):
    ie = input()
    skills.add(ie)

education = {'university': 'Satbayev university', 'speciality': 'computer science'}

print('Здравствуйте меня зовут {0} я живу в городе {1} . Владею такими навыками как : {2} . Учусь в университете {3} по специальности {4}'.format(full_name,tuple[0],skills,education['university'],education['speciality']))

# Тізімдердегі, кортеждердегі, жиындардағы және сөздіктердегі әдістерді қарастырып,
# барлығына ортақ 5 әдісті және ерекшеленетін бірнеше (2-3) әдістерді қолдананатын бағдарлама жаз.  

d = {}
print('Введите слова через пробел: ')
while True:
    s = input()
    if s == ' ':
        break
    else:
        a, b, c = s.split()
        if a in d.keys():
            d[a].update({b: c})
        else:
            d[a] = {b: c}
 
for key in d.keys():
    print(f'{key}:')
    for k, v in d[key].items():
        print(k, v)

# Вам дан словарь, состоящий из пар слов. Каждое слово является синонимом к парному ему слову. 
# Все слова в словаре различны. Для одного данного слова определите его синоним. 
n = int(input())
data = dict(input().split() for i in range(n))
word = input()
if word in data.keys():
    print(data[word])
else:
    for k, v in data.items():
        if v == word:
            print(k)
            break

# Выборы в США ( поменяйте все на выборы в Казахстане) 
result = {}
for i in range(int(input())):
    key, val = input().split()
    result[key] = result.get(key, 0) + int(val)
 
for key, val in sorted(result.items()):
    print(key, val)

# 