#3. Написать программу, подсчитывающую количество цифр числа, используя для этого функцию

def podshet(a):
    i = 0
    while a > 0:
        a //= 10
        i += 1
    return i
numbert = int(input("Введите число: "))
print(podshet(numbert))
