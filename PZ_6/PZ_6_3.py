#3. Дан список размера N и целое число K (1 < K < N). Осуществить сдвиг элементов
#списка влево на K позиций (при этом AN перейдет в AN-K, AN-1 — в AN-K-1, ..AK+1 — в
#A1, а исходное значение K первых элементов будет потеряно). Последние K
#элементов полученного списка положить равными 0.
import random

listt = []
N = int(input("Введите размер списка: "))
K = int(input("Введите число 1 < K < N: "))

def shiftleftK(a,b):
    for i in range(N-b):
        a[i] = a[i+b]
    for g in range(N-K, N):
        a[g] = 0
    return a

for i in range(N):
  listt.append(random.randint(-4,4))
print(listt)
print(shiftleftK(listt, K))
