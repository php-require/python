def matryoshka(n):
	if n == 1:
		print("Матрешка")
	else:
		print("Верх матрешки n=", n)
		matryoshka(n-1)
		print("Низ матрешки n=", n)

matryoshka(15)

print(matryoshka)
			