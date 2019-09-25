from graph import *
from math import *
height=400
width=500
canvasSize(width, height)
windowSize(width, height)
brushColor('cyan')
rectangle(0,0,width, 0.5*height)
brushColor('blue')
rectangle(0,0.5*height,width, 0.75*height)
brushColor('yellow')
penColor('yellow')
rectangle(0,0.75*height,width, height)
def sun(x, y, r):
	penColor('yellow')
	brushColor('yellow')
	circle(width*x,height*y,r)
	penSize(1)
	B=[(width*x,height*y-r*1.2)]
	angle=0
	for i in range (10):
		angle=angle+pi/10
		B.append((width*x+r*1.2*sin(angle),height*y+r*1.2*cos(angle)))
		B.append((width*x-r*1.2*sin(angle),height*y-r*1.2*cos(angle)))
	polygon(B)
sun(0.88, 0.15, 40)
penColor('black')
def cloud(x, y, size):
	brushColor('white')
	penColor('black')
	circle(x,y,size*20)
	circle(x+20*size,y,size*20)
	circle(x+40*size,y,size*20)
	circle(x-10*size,y+20*size,size*20)
	circle(x+10*size,y+20*size,size*20)
	circle(x+30*size,y+20*size,size*20)
	circle(x+50*size,y+20*size,size*20)
cloud(50, 50, 0.75)
cloud(200, 45, 1.5)
def yacht(x, y, size):
	brushColor('brown')
	penColor('black')
	rectangle(x-40*size,y+70*size,x+60*size,y+100*size)
	polygon([(x+60*size,y+70*size),(x+110*size,y+70*size),(x+60*size,y+100*size),(x+60*size,y+70*size)])
	A=[(x-40*size,y+70*size)]
	for i in range(5):
		A.append((x-40*size-30*cos(i*pi/8)*size,y+70*size+30*sin(i*pi/8)*size))
	A.append((x-40*size,y+70*size))
	polygon(A)
	penSize(3*size)
	brushColor('white')
	circle(x+74*size,y+80*size,6*size)
	penSize(5*size)
	line(x,y+70*size,x,y)
	brushColor('grey')
	penSize(1)
	polygon([(x,y),(x+50*size,y+35*size),(x+20*size,y+35*size),(x,y)])
	polygon([(x,y+70*size),(x+50*size,y+35*size),(x+20*size,y+35*size),(x,y+size*70)])
yacht(340,150,1)
yacht(180,180,0.5)
def umb(x, y, size):
	penColor('brown')
	penSize(5*size)
	line(x,y,x,y-125*size)
	penSize(1)
	penColor('black')
	brushColor('red')
	for i in  range (50, 0,-10):
		polygon([(x,y-125*size),(x-i*size,y-85*size),(x+i*size,y-85*size),(x,y-125*size)])
umb(60, 350, 1)
umb(150, 340, 0.75)
run()
