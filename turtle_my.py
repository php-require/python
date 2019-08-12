import turtle
turtle.shape('turtle')
#turtul 1

turtle.forward(50)
turtle.left(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(50)
turtle.right(90)
turtle.forward(50)
turtle.right(90)
turtle.forward(50)	 

#turtul 2
turtle.forward(90)
turtle.left(90)
turtle.forward(90)
turtle.left(90)
turtle.forward(90)
turtle.left(90)
turtle.forward(90)
turtle.left(90)
turtle.forward(90)	 
 
#turtul 3
"""
while 1==1:
	for k in range(1,100):
		k=+3.6
		if k<100:
			print(k)
			turtle.left(k)
			turtle.forward(k)
		else: 
			k=1
"""
 
#turtul 4
 
f=30
s=90
x=0
def functionQ(f:int,s:int):
	turtle.forward(f)
	turtle.left(s)
	 
while x<10:
	functionQ(f,s)
	f=f+10
	x=x+1


#turtul 8
z=90
zz=1
y=0
while y<10*4:

	y=y+1
	print(zz)
 
	turtle.forward(zz)
	turtle.left(z)
	zz=zz+2

