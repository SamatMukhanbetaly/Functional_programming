# Task 1 нужно ввести номер класса и фамилилю потом их упорядочить
def addStudent():
  a = int(input("Хотите добавить студента ? 1 - ДА / 2 - НЕТ "))
  if(a==1):
    numberClass = int(input("Введите класс ученика :"))
    firstName = input("Введите Фамилию студента :")
    list.append([numberClass,firstName])
    addStudent()
  else:
    showList()

def showList():
  a = sorted(list, key=lambda x: x[0])
  print(a)

list = []
i = int(input("Что хотите сделать? Добавить студента - 1 | Посмотреть список -2 : "))
if(i==1):
  addStudent()
elif(i==2):
  showList()
else:
  print("Извините я на такую команду не запрограммирован !")



# Task 2 Добавление оценки студента по предметам и вывод журнала по имени
def addStudent():
  a = int(input("Хотите добавить оценку по предмету для ученика  ? 1 - ДА / 2 - НЕТ "))
  if(a==1):    
    studentName = input("Введите имя студента : ")
    studentSubject = input("Введите предмет студента : ")
    studentGrade = int(input("ВВедите оценку по этому предмету : "))
    list.append([studentName,studentSubject,studentGrade])
    addStudent()
  else:
    showList()

def showList():
  a = input("Введите имя студента : ")
  for i in list:
    if(i[0]==a):
      print(i[1] + " : "+ str(i[2]))

list = []
i = int(input("Что хотите сделать? Добавить оценку - 1 | Посмотреть журнал -2 : "))
if(i==1):
  addStudent()
elif(i==2):
  showList()
else:
  print("Извините я на такую команду не запрограммирован !")
  
# Task 3 Добавление чисел в список и вывод их в отсортированном виде
list = []
while True:
  n = int(input('Введите число: '))
  if(n!=0):
    list.append(n)
  else:
    listSort = sorted(list)
    for i in listSort:
      print(i)
    break

# Task 4 Вывод списка в обратном порядке
list = []
while True:
  n = int(input('Введите число: '))
  if(n!=0):
    list.append(n)
  else:
    listSort = sorted(list, reverse=True)
    for i in listSort:
      print(i)
    break

# Task 5 
import random
list=range(0,49)
computerList = sorted(random.sample(list,6))
personList = sorted(random.sample(list,6))
print(computerList)
print(personList)
if(computerList == personList):
  print("Поздравляем вы выйграли наш главный приз !")
else:
  print("Извините повезет в следующий раз !")



# Task 6 Нужно выяснить в отсортированном ли виде был введен лист
list = []
while True:
  n = int(input('Введите число: '))
  if(n!=0):
    list.append(n)
  else:
    if(list == sorted(list)):
      print(True)
    else:
      print(False)
    break