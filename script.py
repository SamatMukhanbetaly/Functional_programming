from array import *
out_file = open('text.txt', 'w')
print("Введите данные студентов в формате Фамилия Имя Оценка :")
while True:
    text = input()
    if not text:
        break
    out_file.write(text + "\n")
out_file.close()

d1 = []
sum = 0
count = 0

in_file = open('text.txt', 'r')
for line in in_file:
    d1.append(line.rstrip())
    number = line.split()
    sum += int(number[-1])
    count += 1
in_file.close()

with open("text.txt", 'r+') as file:
    file.truncate(0)
file.close()

d1 = sorted(d1)
out_file = open('text.txt', 'w')
for line in d1:
    out_file.write(line+'\n')
out_file.write("Средняя оценка по класу : " + str((sum/count)) + '\n')
out_file.close()