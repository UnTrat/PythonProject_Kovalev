#Вариант 13.
#1. Даны три целых числа: A, B, C. Проверить истинность высказывания: «Хотя бы одно
#из чисел A, B, C положительное».
A, B, C = (input("Введите число A: ")),(input("Введите число B: ")), (input("Введите число C: "))
while type(A) != int:
    try:
        A = int(A)
    except ValueError:
        print("Неправильно ввели число")
        A = input("Введите число A: ")
while type(B) != int:
    try:
        B = int(B)
    except ValueError:
        print("Неправильно ввели число")
        B = input("Введите число B: ")

while type(C) != int:
    try:
        C = int(C)
    except ValueError:
        print("Неправильно ввели число")
        C = input("Введите число C: ")
if (A>0) or (B>0) or (C>0):
    print("Хотя бы 1 число положительное")
else:
    print("Нет положительных чисел")