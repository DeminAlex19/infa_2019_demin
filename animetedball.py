from graph import*
import random
windowSize(800, 800)
canvasSize(800, 800)
ballr = 20
ballcolor = "black"
ballvelx = random.randint(0, 20)
ballvely = 0



hs = 5
hr = 495

ballx = random.randint(ballr + hs, hr - ballr)
bally = random.randint(ballr + hs, hr - ballr)

brushColor("white")
penColor("black")
penSize(5)
bg = rectangle(hs - 5, hs - 5, hr + 5, hr + 5)
penColor(ballcolor)
brushColor(ballcolor)
ball = circle(ballx, bally, ballr)


def changecolor():
    global ballcolor
    ballcolor = randColor()

def drawwall():
    global bg
    brushColor("white")
    penColor("black")
    penSize(5)
    deleteObject(bg);
    bg = rectangle(hs - 5, hs - 5, hr + 5, hr + 5)


def drawball():
    global ballx, bally, ballcolor, ballvelx, ballvely, ballr, hs, hr, ball
    if(ballx + ballvelx + ballr <= hr and ballx + ballvelx - ballr >= hs):
        ballx += ballvelx
    elif(ballx + ballvelx + ballr > hr):
        ballx = ballx - ballvelx // (hr - ballx)
        ballvelx = - ballvelx
        changecolor()
    else:
        ballx = ballx - ballvelx // (ballx - hs)
        ballvelx = - ballvelx
        changecolor()
    if(bally + ballvely + ballr <= hr and bally + ballvely - ballr >= hs):
        bally += ballvely
    elif(bally + ballvely + ballr > hr):
        bally = bally - ballvely // (hr - bally)
        ballvely = - ballvely
        changecolor()
    else :
        bally = bally - ballvely // (bally - hs)
        ballvely = - ballvely
        changecolor()
    if(bally < hr - ballr or ballvely != 0):
        ballvely += 1

    penColor(ballcolor)
    brushColor(ballcolor)
    deleteObject(ball);
    ball = circle(ballx, bally, ballr)


def draw():
    drawwall()
    drawball()


onTimer(draw, 20)
run()