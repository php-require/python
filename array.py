#-------------------
# category:algorithm
# *** fast learn python3 ***
# author:jury
#-------------------
# ~File config~
# -*- coding: utf-8 -*-  
#-------------------

A=[1,2,3,4,5] # массив
C=A
print("array",list(C))

for x in A:
	print(A, type(A)) #получаем тип list


for x  in A: # проход массива
	x+=1	
	print(x)
print(A)


for k in range(5):
	A[k]=A[k]+A[k] # [1, . . . . ] + [1, . . . . ] 
	print(A[k])
 
A=[0]*1000 # размер контейнера массива
top=0 #номер в контейнере
 
x=int(input("input nubmer:"))
while  x!=0:
	A[top]=x
	top+=1
	x=int(input("input 0 to stop:")) # набиваем масив

for k in range(5,-1,-1):  # начинай печатать с позиции  5
	print(A[k])

# создаем функцию array_search 
def array_search(A:list,N:int,x:int): 
	""" Протокол взаимодействия:
		-----------------------
		Осуществяет поиск числа х в массиве А
		от 0 до N-1 включительно.
		Возвращает индекс элемента х в массиве А
		Или -1 если такого нет.
		Если в массиве несколько одинаковых элементов,
		равных x, то венуть индекс первого по счету
		"""
	for k in range(N): # перебираем диапозон чисел от 0 до N невключительно
		if A[k]==x: # если x найден в массиве или A[k] будет равным x
			return k # выходим и возвращаем индекс k
	return -1
		
# тест функции array_search,  поиск 8 в массиве
def test_arrat_search(): # функция линейного поиска
	A1=[1,2,3,4,5]
	m=array_search(A1,5,8)	#ищем в A1 с позиции 5, число 8
	if m==-1: # -1 = нет такой позиции
		print("ok") # значит ок
	else: # иначе false
		print("false")

	# тест поиска -4 в массиве	
	A2=[-1,-2,-3,-4,-5]
	m=array_search(A2,5,-4)	#ищем в A2 с позиции 5, число -4
	if m==3: # индекс массива, (*массив c 0)
		print("ok") # значит ок
	else: # иначе false
		print("false")	

	# тест поиска нескольких одинаковых элементов в массиве	
	A3=[10,20,30,10,10]
	m=array_search(A3,5,10)	#ищем в A2 с позиции 5, число -4
	if m==0: # индекс массива, (*массив c 0)
		print("ok") # значит ок
	else: # иначе false
		print("false")			

test_arrat_search() # start test		


def invert_array(A:list,N:int):
	"""реверс массива
	в рамка индекса от 0 до N-1
	"""
	for k in range(N//2):
		A[k], A[N-1-k] = A[N-1-k], A[k] # меняем местами A[k], A[N-1-k]
 
def test_invert_array():
	A6=[1,2,3,4,5,9,10]
	print(A6)
	invert_array(A6,5) # до куда переворачиваем (индекс)
	print(A6)
pass

test_invert_array()	

# Цикличный сдвиг в лево
A7=[1,2,3,4,5,6,7]
N=2
tmp=A7[0]

for k in range(N-1):
	A7[k]=A7[k+1]
A7[N-1]=tmp
print(A7)

# Решето Эратосфена	
A[True]*N # N = число индексов в массиве
A[0]=A[1]=False
for k in range(2,N):
	if A[k]:
		for m in range(2*k,N,k):
			A[m]=False
#print(A) покажет все
for k in range(N):
	print(k,'-',"prostoe"if A[k]else"sostavnoe") # условие в принте
	