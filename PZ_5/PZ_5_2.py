#2. Описать функцию ShiftRight3(A, B, C), выполняющую правый циклический сдвиг:
#значение A переходит в B, значение B — в C, значение C — в A (A, B, C —
#вещественные параметры, являющиеся одновременно входными и выходными). С
#помощью этой функции выполнить правый циклический сдвиг для двух данных
#наборов из трех чисел: (A1, B1, C1) и (A2, B2, C2).
def ShiftRight3(a, b, c):
    f = a 
    g = b 
    h = c
    a = g
    b = h
    c = f
    return a,b,c
A1, B1, C1 = input("Введите число A1: "), input("Введите число B1: "), input("Введите число C1: ")
while type(A1) != float:
    try:
        A1 = float(A1)
    except ValueError:
        print("Неправильно ввели!")
        A1 = input("Введите вещественное число A: ")
while type(B1) != float:
    try:
        B1 = float(B1)
    except ValueError:
        print("Неправильно ввели!")
        B1 = input("Введите вещественное число B: ")
while type(C1) != float:
    try:
        C1 = float(C1)
    except ValueError:
        print("Неправильно ввели!")
        C1 = input("Введите вещественное число C: ")

print(ShiftRight3(A1, B1, C1))

A2, B2, C2 = input("Введите число A2: "), input("Введите число B2: "), input("Введите число C2: ")
while type(A2) != float:
    try:
        A2 = float(A2)
    except ValueError:
        print("Неправильно ввели!")
        A2 = input("Введите вещественное число A: ")
while type(B2) != float:
    try:
        B2 = float(B2)
    except ValueError:
        print("Неправильно ввели!")
        B2 = input("Введите вещественное число B: ")
while type(C2) != float:
    try:
        C2 = float(C2)
    except ValueError:
        print("Неправильно ввели!")
        C2 = input("Введите вещественное число C: ")
        
print(ShiftRight3(A2, B2, C2))
