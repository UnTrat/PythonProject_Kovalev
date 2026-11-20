# 1 Дан список A размера N. Вывести в начале его элементы с четными номерами (в
# порядке возрастания номеров), а затем - элементы с нечетными номерами (также в
# порядке возрастания номеров) : A2, A4, A6, ..., A1, A3, A5, ... . Условный оператор не использовать
import  random
Listik = []
N = int(input("Введите размер списка: "))
for i in range(N):
    Listik.append(random.randint(-4, 4))
def chetn(A):
    B = []
    for i in range(len(A)):
        if A[i] % 2 ==0:
            B.append(A[i])
    B.sort()
    return B
def nechetn(A):
    C = []
    for i in range(len(A)):
        if A[i] % 2 !=0:
            C.append(A[i])
    C.sort()
    return C
print(Listik)
print(chetn(Listik))
print(nechetn(Listik))