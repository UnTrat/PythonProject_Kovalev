# Вариант 13. Дано двузначное число. Вывести число, полученное при перестановке цифр исходного числа 
Cycle = True
while Cycle == True:
    try:
        while True:
            num = int(input("Введите двузнаачное число: "))
            # Проверка на принадлежность к 2-х значному числу
            if num//10 >= 1 and num//10 <=10:
            # Перестановка чисел
                a, b = divmod(num, 10)
                print(b*10 + a)
                Cycle = False
                break
            else:
                continue
    #Предотвращение ошибки значения 
    except  ValueError:
            print("Что-то пошло не так!")
            continue



