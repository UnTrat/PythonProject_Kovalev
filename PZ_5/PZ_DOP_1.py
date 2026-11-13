#1. Даны три целых числа. Определить у какого числа больше сумма цифр. Вывод
#результата предусмотреть в основной программе. Расчет суммы цифр оформить в
#функции.
g = 0
f = 0
h = 0

a,b,c = int(input("Введите число A: ")), int(input("Введите число B: ")), int(input("Введите число C: "))
def compare1(a,b):
    if a>b:
        return a
    else:
        return b
def compare2(a,b,c):
    return campare1(a, (compare1(b,c)))
while a > 0:
    g += a%10
    a //= 10
while b > 0:
    h += b%10
    b //= 10
while c > 0:
    f += c%10
    c //= 10
print(compare2(g,h,f))