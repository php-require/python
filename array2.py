#-------------------
# category:algorithm
# *** fast learn python3 ***
# author:jury
#-------------------
# ~File config~
# -*- coding: utf-8 -*-  
#-------------------


#list comprehension
C=[x**2 for x in range(10)]
C.append(100*2) # добавляем в конец массива элемент
print(C,'добавили 200')
C.pop() # удаляем последний элемент массива
print(C,'удалили 200')

# находим чкетные числа и записываем в массив B (пример 1)
A =[1,2,3,4,5,6,7,8,9,10] 
for x in A:
	B=[]
	if x%2==0:
		B.append(x**2) # возводим в квадрат или можно x*x

#list comprehension
B=[x**2 for x in A if x%2==0] # тоже самое что и (пример 1), только в 1 строку
print(B) 


######################################
#СОРТИРОВКИ МАССИВА
#Квадратичные сортировки O(N2)

def insert_sort(A):
	""" сортировка списка А вставками"""
	N = len(A)
	for top in range(1,N): # N = конец масива -1
		k=top
		while k > 0 and A[k-1] > A[k]:
			A[k], A[k-1] = A[k-1], A[k]
			k -=1


def choise_sort(A):
	""" сортировка списка А выбором"""
	N = len(A)
	for pos in range(0,N-1): # N = конец масива -1
		for k in range(pos+1, N):
			if A[k] < A[pos]:
				A[k], A[pos] = A[pos], A[k]


def bubble_sort(A):
	""" сортировка списка А пузырька"""
	N = len(A)
	for bypass in range(1,N): # N = конец масива -1
		for k in range(0, N-bypass):
			if A[k] > A[k+1]:
				A[k], A[k+1] = A[k+1], A[k]

def test_sort(sort_algorithm):
	print("Тестируем: ", sort_algorithm.__doc__)
	print("testcase #1: ", end="")
	A = [4,2,5,1,3]
	A_sorted = [1,2,3,4,5]
	sort_algorithm(A)
	print("OK" if A == A_sorted else "Fail")

	print("testcase #2: ", end="")
	list(range(10,20)) + list(range(0,10))
	A_sorted = list(range(20))
	sort_algorithm(A)
	print("OK" if A == A_sorted else "Fail")

	print("testcase #3: ", end="")
	A = [4,2,4,2,1]
	A_sorted = [1,2,2,4,4]
	sort_algorithm(A)
	print("OK" if A == A_sorted else "Fail")

if __name__== "__main__":  
	test_sort(insert_sort)
	test_sort(choise_sort)
	test_sort(bubble_sort)


# Сортировка подсчета (count sort)
def CountSort(list):
    sortedList = [0] * 101
    for i in list:
        sortedList[i] += 1
    for i in range(101):
        print((str(i) + ' ') * sortedList[i], end='')
 
 
list = [int(i) for i in input().split()]
CountSort(list)