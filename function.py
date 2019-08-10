#-------------------
# category:algorithm
# *** fast learn python3 ***
# author:jury
#-------------------

# пример с инпутами
name = input("whats is your name:")

age=int(input("How old a you:")) # ввод только цифр

year=str((2019-age)+100)

print(name+"will be 100 years old in the year"+year)


# duck type = если что то крякает как утка или ходит как утка, = это утка
def max2(x,y): # создаем функцию max2 = 6>5 = x иначе = y
	if x>y:
		return x
	return y # ruturn завершает функцию

def max3(x,y,z):# функция max3
	return max2(x, max2(y,z))# первый вызов max2(y,z), после x, max2(x, max2(y,z))
print(max3('ab','abc','abd'))# распечатать текст


#найдет самое большое число 322
def max3(x,y,z):
	return max2(x, max2(y,z))

a,b,c=10,25,17 # каскаднае присваивание переменных*

f=max3 # ссылка на функцию 

print(max3(322,224,2))

print(f(a,b,c))
