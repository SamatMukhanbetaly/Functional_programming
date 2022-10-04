# 4 лабороторная работа
# 1 есеп кай регистрдагы символдар коп сол аркылы букил сойлемди сол регистрге аудар
string = str(input())
upper = 0
lower = 0
for i in string:
    if i.isupper():
        upper += 1
    else:
        lower += 1
if upper > lower:
    print(string.upper())
else:
    print(string.lower())

# 2 есеп енгизген сандардын сан екенин тексеру егер сандар болса косындысын шыгару
a, b = input(), input()
while not(a.isdigit() and b.isdigit()):
    a, b = input(), input()
print(int(a) + int(b))

# 3 есеп еки созди енгиземиз жане олардын орынын ауыстырамыз
s = input()
first_word = s[:s.find(' ')]
second_word = s[s.find(' ') + 1:]
print(second_word + ' ' + first_word)

# 4 есеп сойлем енгизиледи сол сойлемнин ишинде еки s символы болса осы аралык ошириледи
s = input()
s = s[:s.find('s')] + s[s.rfind('s') + 1:]
print(s)

# 5 есеп индекстері 3-ке бөлінген барлық таңбаларды алып тастаймын 
s = input()
t = ''
for i in range(len(s)):
    if i % 3 != 0:
        t = t + s[i]
print(t)

# 6 есеп артык символдарды оширу
s = "Бирак , бул даналыкты айткан ким ?"
s = s.lower()
for char in " ,.;:-?!":
    s = s.replace(char, "")
print(s)

# 7 есеп енгизилген сойлемнин ишинде биз сурастырган индексте цифра барма жокпа карастырамыз
def IsCharDigit(s, index):
    if (index<0)or(index>len(s)-1):
        return False
    return (s[index]>='0')and(s[index]<='9')
s = input("s = ")
index = int(input("index = "))
if IsCharDigit(s, index):
    print("Yes")
else:
    print("No")

# 8 есеп енгизилген сойлемде канша биз издеген символ бар екенин табу
def IsCharOp(s):
    sAll = "+-*/%"
    k = 0 
    for c1 in s:
        for c2 in sAll:
            if c1==c2:
                k = k+1
    return k
s = input("s = ")
k = IsCharOp(s)
print("k = ", k)

# 9 есеп енгизилген сойлемде канша енгизилген болшектер бар екенин корсетеди
s1 = input()
s2 = input()
k = s1.count(s2)
print("k = ", k)

# 10 есеп кейбир функцияларды зерттеу 
string = 'Def Python. Wellcome to my blog about python'
print(string.capitalize())
print(string.title())
print(string.swapcase())
