#Ввести N чисел. Найти и вывести их среднее арифметическое.
a = 0
b = 0
n = 0
while True:
    n = input("Введите число: ")
    if n != "стоп":
        a += int(n)
        b += 1
    else:
        break
print(a//b)
