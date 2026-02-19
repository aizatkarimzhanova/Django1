#try

day = int(input("Введите день вашего рождения: "))
month = int(input("Введите месяц вашего рождения (числом): "))

if (21 <= day <= 31 and month == 3) or (1 <= day <= 20 and month == 4):
    print("Овен")
elif (21 <= day <= 30 and month == 4) or (1 <= day <= 21 and month == 5):
    print("Телец")
elif (22 <= day <= 31 and month == 5) or (1 <= day <= 21 and month == 6):
    print("Близнецы")
elif (22 <= day <= 30 and month == 6) or (1 <= day <= 22 and month == 7):
    print("Рак")
elif (23 <= day <= 31 and month == 7) or (1 <= day <= 21 and month == 8):
    print("Лев")
elif (22 <= day <= 31 and month == 8) or (1 <= day <= 23 and month == 9):
    print("Дева")
elif (24 <= day <= 30 and month == 9) or (1 <= day <= 23 and month == 10):
    print("Весы")
elif (24 <= day <= 31 and month == 10) or (1 <= day <= 22 and month == 11):
    print("Скорпион")
elif (23 <= day <= 30 and month == 11) or (1 <= day <= 22 and month == 12):
    print("Стрелец")
elif (23 <= day <= 31 and month == 12) or (1 <= day <= 20 and month == 1):
    print("Козерог")
elif (21 <= day <= 31 and month == 1) or (1 <= day <= 19 and month == 2):
    print("Водолей")
elif (20 <= day <= 29 and month == 2) or (1 <= day <= 20 and month == 3):
    print("Рыбы")
else:
    print("Неверная дата! Попробуйте снова.")


