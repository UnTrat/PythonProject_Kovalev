# Дано число R и список размера N. Найти два соседних элемента списка, сумма
# которых наиболее близка к числу R, и вывести эти элементы в порядке возрастания
# их индексов (определение наиболее близких чисел - то есть такой элемент Ак, для
# которого величина Ак-R является минимальной
import random
listt = []
R = int(input("число R: "))
N = int(input("Размер списка: "))

for i in range(N):
    listt.append(random.randint(-4, 4))
def poisk(a, r):
    best_dist = 0
    best_index = 0
    dist = 0
    for i in range(1, len(a)-1):
        dist == a[i] + a[i+1] - r
        if dist < best_dist:
            best_dist = dist
            best_index = i
    ans = [a[best_index], a[best_index+1]]
    ans.sort()
    return ans  
print(listt)      
print(poisk(listt, R))
