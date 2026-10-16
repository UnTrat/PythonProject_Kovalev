#Ввести двухзначное число. Если сумма цифр числа четная, то увеличить число на 2,
#в противном случае уменьшить на 2.
while True:
    num = int(input("Введите двузначное число: "))
    if num>9 and num<100:
        a,b = divmod(num, 10)
        if (a+b)%2 == 0:
            print(num+2)
        else:
            print(num-2)
        break
    else:
        continue
