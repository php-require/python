def max2(x,y):
	if x>y:
		return x
	return y
def max3(x,y,z):
	return max2(x, max2(y,z))
print(max3(10,2,11))

#найдет самое большое число 322
def max2(x,y):
	if x>y:
		return x
	return y
def max3(x,y,z):
	return max2(x, max2(y,z))
print(max3(322,22,2)) 