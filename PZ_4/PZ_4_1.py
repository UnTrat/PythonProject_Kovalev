#Вариант 14.
#1. Дано вещественное число A и целое число N (>0). Используя один цикл, вывести все
#целые степени числа A от 1 до N.

A, N = input("Введите вещественное число A: "), input("Введите число N, для обозначенния степени: ")

while N < 0 or N == 0:
    print("Степень должна быть больше нуля")
    N = input("Введите число N, для обозначенния степени: ")

while type(A) != int:
    try:
        A = int(A)
    except ValueError:
        print("Неправильно ввели!")
        A = input("Введите вещественное число A: ")
while type(N) != int:
    try:
        N = int(N)
    except ValueError:
        print("Неправильно ввели!")
        N = input("Введите вещественное число A: ")

try_count = 0
B = A
while try_count != N:
    print(A)
    A *= B
    try_count += 1





