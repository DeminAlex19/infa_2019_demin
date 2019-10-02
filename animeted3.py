from graph import *

windowSize(500,250)

def person(x, shirtcolor, haircolor):
	penColor("orange")
	penSize(0)
	brushColor(shirtcolor)
	circle(x+250/2,500/2,150/2)
	brushColor("pink")
	penColor("pink")
	circle(x+250/2,250/2,150/2)
	penSize(10)
	line(375/2+x,425/2,475/2+x,10/2)
	line(125/2+x,425/2,25/2+x,10/2)
	penSize(0)
	circle(35/2+x, 50/2, 25/2)
	circle(465/2+x, 50/2, 25/2)
	circle(35/2+x, 40/2, 25/2)
	circle(465/2+x, 40/2, 25/2)
	penColor("black")
	brushColor("blue")
	circle(300/2+x,225/2,30/2)
	circle(200/2+x,225/2,30/2)
	brushColor("black")
	circle(300/2+x,227/2,10/2)
	circle(200/2+x,227/2,10/2)
	brushColor("red")
	polygon([(250/2+x,350/2), (170/2+x,300/2), (330/2+x,300/2), (250/2+x,350/2)])
	brushColor("brown")
	polygon([(250/2+x,290/2), (235/2+x,260/2), (265/2+x,260/2), (250/2+x,290/2)])
	brushColor(shirtcolor)
	polygon([(140/2+x,430/2), (105/2+x,425/2), (90/2+x,400/2), (130/2+x,360/2), (150/2+x,400/2), (140/2+x,430/2)])
	polygon([(360/2+x,430/2), (395/2+x,425/2), (410/2+x,400/2), (370/2+x,360/2), (350/2+x,400/2), (360/2+x,430/2)])
	brushColor(haircolor)
	polygon([(215/2+x,110/2),(250/2+x,35),(285/2+x,110/2),(215/2+x,110/2)])

i=0

def drawpic():
	global i
	penColor("white")
	brushColor("white")
	rectangle(0,0,500, 250)
	if(i%2 == 0):
		person(0, "green", "yellow")
		person(250, "orange", "purple")
		penSize(1)
		penColor("black")
		brushColor("green")
		rectangle(0,0,500,25)
		label("PYTHON is REALLY AMAZING!", 150, 1, font=('Courier', 12), bg="green")
	else:
		person(0, "yellow", "green")
		person(250, "purple", "orange")
		penSize(1)
		penColor("black")
		brushColor("red")
		rectangle(0, 0, 500, 25)
		label("PYTHON is REALLY AMAZING!", 150, 1, font=('Courier', 12), bg="red")
	if(i==0):
		i=1
	else:
		i=0


onTimer(drawpic, 1000)
run()