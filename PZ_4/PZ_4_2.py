# Дано целое число N (> 1). Вывести наименьшее K, для которого
# сумма 1 + 2 + ... + K >= N, и саму эту сумму

N = input("Введите целое число ")

while type(N) != int:
    try:
        N = int(N)
    except ValueError:
        print("Неправильно ввели!")
        N = input("Введите целое число: ")

K = 0
S = 0
while S < N:
    K += 1
    S += K

print("K =", K)
print("Сумма =", S)