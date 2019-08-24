import turtle
turtle.shape('turtle')
""" 
for i in range(1,10):
		turtle.circle(i, 90) 

def hello(name):
	print('hello, ',name, '!')
hello('petja')

def sum(a,b):
	return a + b
sum(5,2) # need print

a=60
b=60
for i in range(0,100):
		if a==60:
			turtle.left(a-1)
			turtle.forward(b+i)

		else:
			turtle.left(a+i)
			turtle.forward(b)	
#turtle.left(120)
#turtle.forward(60)
#turtle.left(120)
#turtle.forward(60)
turtle.up()
turtle.goto(20,0)
turtle.mainloop() 	
 

#tutor 11 
turtle.color("brown", "orange")
turtle.begin_fill()
turtle.circle(50, 180)
turtle.circle(50, 180)
turtle.circle(-50, 180)
turtle.circle(-50, 180)
turtle.end_fill()
turtle.left(30)
turtle.begin_fill()
turtle.color("brown", "blue")
turtle.circle(50, 180)
turtle.circle(50, 180)
turtle.circle(-50, 180)
turtle.circle(-50, 180)
turtle.end_fill()
turtle.left(30)
turtle.begin_fill()
turtle.color("brown", "gray")
turtle.circle(50, 180)
turtle.circle(50, 180)
turtle.circle(-50, 180)
turtle.circle(-50, 180)
turtle.end_fill()
turtle.left(30)
turtle.begin_fill()
turtle.color("brown", "yellow")
turtle.circle(50, 180)
turtle.circle(50, 180)
turtle.circle(-50, 180)
turtle.circle(-50, 180)
turtle.end_fill()
turtle.left(30)
turtle.begin_fill()
turtle.color("brown", "red")
turtle.circle(50, 180)
turtle.circle(50, 180)
turtle.circle(-50, 180)
turtle.circle(-50, 180)
turtle.end_fill()
turtle.left(30)
turtle.begin_fill()
turtle.color("brown", "green")
turtle.circle(50, 180)
turtle.circle(50, 180)
turtle.circle(-50, 180)
turtle.circle(-50, 180)
turtle.end_fill()


# tutor 13
for i in range(0,10):
		turtle.left(100)
		turtle.circle(50, 180)

#tutor 14

turtle.begin_fill()
turtle.color("black", "yellow")
turtle.circle(100, 360)
turtle.end_fill()
t=turtle
t.up()
t.goto(-30,135)
turtle.begin_fill()
turtle.color("black", "blue")
turtle.circle(20, 360)
turtle.end_fill()
t.goto(30,135)
turtle.begin_fill()
turtle.color("black", "blue")
turtle.circle(20, 360)
turtle.end_fill()
t.goto(0,120)
t.down()
turtle.begin_fill()
turtle.color("black", "green")
turtle.pensize(10)
t.goto(0,70)
turtle.end_fill()
t.up()
t.goto(30,20)
t.down()
turtle.color("red", "red")
t.left(90)
turtle.circle(30, 180)

"""
#tutor 15
for i in range(9):
     turtle.stamp(); turtle.fd(130)
     turtle.left(160)
turtle.up()
turtle.goto(-100,-60)
turtle.left(180)
turtle.down()
turtle.fd(150)
turtle.left(150)
turtle.fd(150)
turtle.left(140)
turtle.fd(150)
turtle.left(140)
turtle.fd(150)
turtle.left(140)
turtle.fd(150)       
turtle.mainloop()       

#рекурсия  смотреть файл matryoshka.py
def matryoshka(n):
	if n == 1:
		turtle.mainloop() 
	else:
		turtle.left(140)
		turtle.fd(150)
		matryoshka(n-1)

		turtle.right(140)
		turtle.fd(150)

matryoshka(15)	