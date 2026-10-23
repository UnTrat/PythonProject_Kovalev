#Найти и вывести на экран S=1!+2!+3!+4!+…+n! (n>1)
n = int(input("Введите N>3: "))
ans = 0
s = 1
i = 1
while i != n+1:
 print(s)
 s *= i
 ans += s
 i += 1
print(ans)