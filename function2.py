#-------------------
# category:algorithm
# *** fast learn python3 ***
# author:jury
#-------------------
# ~File config~
# -*- coding: utf-8 -*-  
#-------------------

#for formatting a date 
print('09','12','2016', sep='-') 

def separator_my(name="john",separator="-"):
	print("hi",name, sep=separator)

separator_my(separator="***",
			name="John2")

def function_pass():
	pass # пустышка

def is_simple_nuber(x):
	""" Определяет являеться ли число простым
		x - целое положительное цисло (int)
		если простое, то возвращает true,
		а иначе - false
	"""

	divaisor=2
	while divaisor<x:
		if x%divaisor==0:
			return False
		divaisor+=1	
	return True

# Факторизация целых чисел
n = int(input("Integer: "))
factors = []
d = 2
m = n # Запомним исходное число
while d * d <= n:
        if n % d == 0:
            factors.append(d)
            n//=d
        else:
            d += 1
factors.append(n) # Добавим последнеё простое число
print('{} = {}' .format(m, factors)) # Выводим исходное число и все простые множители.

def build_house(window, upper_left_corner, width):
	""" функция которая рисует дом """
	height=calculate_height(width)# вычесляем высоту дома по ширине

