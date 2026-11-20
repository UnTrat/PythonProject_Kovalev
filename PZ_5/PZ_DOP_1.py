#1. Даны три целых числа. Определить у какого числа больше сумма цифр. Вывод
#результата предусмотреть в основной программе. Расчет суммы цифр оформить в
#функции.
def summa(a):
    g = 0
    while a > 0:
        g += a % 10
        a //= 10
    return g

def compare1(a,b):
    if a>b:
        return a
    else:
        return b
def compare2(a,b,c):
    return compare1(a, (compare1(b,c)))

a,b,c = int(input("Введите число A: ")), int(input("Введите число B: ")), int(input("Введите число C: "))
print(summa(a), summa(b), summa(c))
print(compare2(summa(a), summa(b), summa(c)))