from random import random

sizeA = int(input("Введите размерность массива A: "))
sizeB = int(input("Введите размерность массива B: "))
A = [0] * sizeA
B = [0] * sizeB  # Аналогично
C = [0] * max(sizeA, sizeB)
def fill(spisok):  # Функция - заполнитель массива
    for n in range(len(spisok)):
        spisok[n] = round(random() * 10, 1)
fill(A)
print("Массив A:", A)
fill(B)
print("Массив B:", B)
N = 0
for i in range(len(A)):
    for j in range(len(B)):
        if A[i] == B[j]:
            C[N] = A[i]
            N += 1
print("Совпадающие элементы (0 не является совпавшим элементом): ")
for N in range(len(C)):
    print(C[N])