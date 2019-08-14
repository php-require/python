import turtle
turtle.shape('turtle')
#turtul 1
"""
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
 
while 1==1:
	for k in range(1,100):
		k=+3.6
		if k<100:
			print(k)
			turtle.left(k)
			turtle.forward(k)
		else: 
			k=1
 
 
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
 
#tutop 5 
turtle.reset()
turtle.color("green","orange")
def turtle_q(k:int):
	while k<50:
		k=k+10	 	 
		turtle.forward(40)
		turtle.color("red", "blue")
		turtle.width(2)
		turtle.left(90)
	turtle.up()	
	turtle.goto(-10,-10)

def turtle_q2(k:int):
	while k<50:
		k=k+10	 	 
		turtle.forward(60)
		turtle.color("green", "red")
		turtle.width(2)
		turtle.left(90)
	turtle.up()	
	turtle.goto(-10,-10)


turtle_q(10)
turtle.down()
turtle_q2(10)
"""
# tutor 6
n=0
while n<12:
	turtle.goto(0,0)
	turtle.down()
	turtle.left(30)
	turtle.forward(60)
	n=n+1

turtle.color("red", "green")
turtle.up()
turtle.goto(-450, 0)
turtle.down()
turtle.setheading(270)
for i in range(5):
    turtle.circle(50, 180)
    turtle.begin_fill()
    turtle.circle(-50, 180)
    turtle.end_fill() 
 
n=0
while n<12:
	turtle.goto(-400,0)
	turtle.down()
	turtle.left(30)
	turtle.forward(60)
	n=n+1
n=0
turtle.goto(-400,0)
turtle.color("red", "yellow")
while n<12:

	turtle.goto(-200,0)
	turtle.color("blue", "yellow")
	turtle.down()
	turtle.left(30)
	turtle.forward(60)
	n=n+1
n=0

turtle.goto(-200,0)
turtle.color("red", "purple")
while n<12:

	turtle.goto(200,0)
	turtle.color("purple", "brown")
	turtle.down()
	turtle.left(30)
	turtle.forward(60)
	n=n+1	

n=0

turtle.goto(200,0)
turtle.color("purple", "orange")
while n<12:

	turtle.goto(400,0)
	turtle.color("brown", "orange")
	turtle.down()
	turtle.left(30)
	turtle.forward(60)
	n=n+1	 
turtle.goto(400,0)
turtle.color("red", "black")
turtle.goto(500,0)
turtle.goto(-450,0)
turtle.left(180)
turtle.begin_fill()
turtle.circle(50, 180)
turtle.color("red", "green")
turtle.end_fill()
turtle.goto(0,0)
turtle.goto(0,-300)
turtle.up()
turtle.goto(0,-330)
turtle.write("Готово = ", True, align="center")
turtle.write((0,0), True)
turtle.mainloop() 