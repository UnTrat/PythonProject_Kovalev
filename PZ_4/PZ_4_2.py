#Дано целое число N (> 1). Вывести наименьшее из целых чисел K, для которых
#сумма 1 + 2 + . . . + K будет больше или равна N, и саму эту сумму

N, K = input("Введите целое число "), input("Введите число K")

while type(N) != int:
    try:
        N = int(N)
    except ValueError:
        print("Неправильно ввели!")
        N = input("Введите целое число: ")
while type(K) != int:
    try:
        K  = int(K)
    except ValueError:
        print("Неправильно ввели!")
        K = input("Введите число K: ")
a = 0
num = 1
num1 = 1
try_count = 0
while try_count != K:
    print(num)
    num += num1
    num1 += 1
    try_count += 1
    if num > N or num == N:
        a += num
        break
print("наименьшее из целых чисел K, для которых сумма 1 + 2 + . . . + K будет больше или равна N: ",a)


