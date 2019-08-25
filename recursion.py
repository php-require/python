import graphics as gr
window = gr.GraphWin("Russin game", 600, 600)
alpha = 0.1
# рекурсия алгебра
def fractal_rectangle(A, B, C, D, deep=10):
    if deep < 1:
        return
    for M, N in (A, B), (B, C), (C, D), (D, A):
        gr.Line(gr.Point(*M), gr.Point(*N)).draw(window)
    A1 = (A[0]*(1-alpha) + B[0]*alpha, A[1]*(1-alpha) + B[1]*alpha)
    B1 = (B[0]*(1-alpha) + C[0]*alpha, B[1]*(1-alpha) + C[1]*alpha)
    C1 = (C[0]*(1-alpha) + D[0]*alpha, C[1]*(1-alpha) + D[1]*alpha)
    D1 = (D[0]*(1-alpha) + A[0]*alpha, D[1]*(1-alpha) + A[1]*alpha)
    fractal_rectangle(A1, B1, C1, D1, deep-1)

#fractal_rectangle((100, 100), (500, 100), (500, 500), (500, 100),800)

# две линии а и б разной длинны. находим общий делитель 
def gcd(a,b):
	if b==0:
		return a
	else:
		return gcd(b, a%b)	

# тоже самое в 2 строки
def gcd(a,b):
	return(a if b==0 else gcd(b, a%b))		

# рекурсия, возведение в степень
def pow(a:float,n:int):
    if n == 0:
        return 1
    elif n%2 ==1: #говорим нечетное число
        return pow(a,n -1)*a    
    else:# (призрак n равно четное)
        return pow(a**2, n//2)
print(pow(-2,5)) # - 2 в степени 5


# строковый пример генерации 
def gen_bin(Z, prefix=""):
    if Z == 0:
        print(prefix)
        return
    gen_bin(Z-1, prefix+"0")
    gen_bin(Z-1, prefix+"1")     

gen_bin(6)

# выводим работ рекурсии 
def generate_number(N:int,M:int, prefix=None):
    """ Генерирует все числа (с лидирующими незначащими нулями)
        в N-ричной системы счисления (N <= 10) длины М
    """
    prefix = prefix or []
    if M == 0:
        print(prefix)
        return
    for digit in range(N):
        prefix.append(digit)    
        generate_number(N, M-1, prefix)
        prefix.pop()

generate_number(4,3)        

