#Дано целое число. Если оно является положительным, то прибавить к нему 20, в
#противном случае вычесть из него 5.
while True:
    try:
        num = int(input("Введите число: "))
        if num>0:
            print(num + 20)
        else:
            print(num -5)
        break
    except ValueError:
        print("Введите целое число")
        continue