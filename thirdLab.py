# 1 есеп шыгарылуы
print([k for k in range(int(input("Введите цифру A = :")),int(input("Введите цифру B = :"))+1)])
# 2 есеп шыгарылуы
A = int(input("Введите цифру A = :"))
B = int(input("Введите цифру B = :"))
if A < B :
    for i in range(A,B+1):
        print(i)
else :
    for i in range(B,A+1):
        print(i)
# 3 есеп шыгарылуы
A = int(input("Введите цифру A = :"))
B = int(input("Введите цифру B = :"))
for i in range(A - (A + 1) % 2, B - B % 2, -2):
    print(i)
# 4 есеп шыгарылуы
N = int(input("Введите количество карточек :"))
sum = 0
for i in range(1, n + 1):
    sum += i
for i in range(n - 1):
    sum -= int(input())
print(sum)