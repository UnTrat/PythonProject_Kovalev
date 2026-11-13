#2. Рассчитать и вывести периметр и площадь прямоугольника. Расчеты оформить в функции.

def perimetr(a,b):
    return (a+b)*2
def ploshad(a,b):
    return a*b
a,b = int(input("Введите длину прямоуголника")), int(input("Введите ширину прямоуголника"))
print(perimetr(a,b))
print(ploshad(a,b))