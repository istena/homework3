# Задача 18: Требуется найти в массиве A[0..N-1] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих строках записаны N целых чисел A[i]. Последняя строка содержит число X
# 5
# 1 2 3 4 5
# 6
# -> 5
n=int(input('Введите количество чисел: '))
l=[0]*n
for i in range(n):
    l[i]=int(input(f"{i+1}) "))
x=int(input('Введите число x: '))
mini=abs(l[0]-x)
count=0
for i in range(1,n):
    if abs(l[i]-x)<mini:
        mini=abs(l[i]-x)
        count=i
print(l[count])
