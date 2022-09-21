# Функциональное программирование Орындаушы Мұханбеталы Самат Мажитуллаұлы
import datetime
now = datetime.datetime.now()

fullName = "Mukhanbetaly Samat"
yearthOfBirth = 2002
year = now.year - yearthOfBirth

if year < 20:
    print("Вам меньше 20 лет")
elif year >= 20 and year <= 40:
    print("Вам больше 20 лет но вы не достигли 40")
else:
    print("Вам больше 40 лет")