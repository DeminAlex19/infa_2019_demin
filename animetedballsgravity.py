from graph import*
import random
N = random.randint(5, 7)
hs = 5
hr = 695
windowSize(hr+10, hr+10)
canvasSize(hr+10, hr+10)
ballr = 20.0
maxsvel = 3.0
axel = 0.05

def rx():
    global hs, hr, ballr
    return random.randint(2 * ballr + hs, hr - 2 * ballr) / 1.0

def rvel():
    global maxsvel
    return random.randint(0, maxsvel) / 10.0

brushColor("white")
penColor("black")
penSize(5)
bg = rectangle(hs - 5, hs - 5, hr + 5, hr + 5)
balld = [circle(0,0,0), circle(0,0,0), circle(0,0,0), circle(0,0,0), circle(0,0,0), circle(0,0,0), circle(0,0,0)]

ball = []
for i in range(N):
    quickball = [rx(), rx(), rvel(), rvel(), randColor()]
    ball.append(quickball)

def changecolor():
    s = randColor()
    while(s == "white"):
        s = randColor()
    return randColor()

def drawwall():
    global bg
    brushColor("white")
    penColor("black")
    penSize(5)
    deleteObject(bg);
    bg = rectangle(hs-5,hs-5,hr+5,hr+5)

def part(vx, vy, x1, y1, x2, y2):
    global ballr
    d = abs(16 * (ballr ** 2) * (vx ** 2 + vy ** 2) - 4 * (vx * (y1 - y2) - vy * (x1 - x2)) ** 2)
    return (2*(vx*(x1-x2) + vy*(y1-y2)) + (d)**(0.5)) / (2 * (vx**2 + vy**2))

def vel(x1, y1, vx1, vy1, x2, y2, vx2, vy2):

    return

def moveball():
    global ball, N, hs, hr, ballr
    for i in range(N):
        if(ball[i][0] + ball[i][2] + ballr <= hr and  ball[i][0] + ball[i][2] - ballr >= hs):
            ball[i][0] += ball[i][2]
        elif(ball[i][0] + ball[i][2] + ballr > hr):
            ball[i][0] = ball[i][0] - ball[i][2] // (hr - ball[i][0])
            ball[i][2] = - ball[i][2]
            ball[i][4] = changecolor()
        else:
            ball[i][0] = ball[i][0] - ball[i][2] // (ball[i][0] - hs)
            ball[i][2] = - ball[i][2]
            ball[i][4] = changecolor()
        if(ball[i][1] + ball[i][3] + ballr <= hr and ball[i][1] + ball[i][3] - ballr >= hs):
            ball[i][1] += ball[i][3]
        elif(ball[i][1] + ball[i][3] + ballr > hr):
            ball[i][1] = ball[i][1] - ball[i][3] // (hr - ball[i][1])
            ball[i][3] = - ball[i][3]
            ball[i][4] = changecolor()
        else :
            ball[i][1] = ball[i][1] - ball[i][3] // (ball[i][1] - hs)
            ball[i][3] = - ball[i][3]
            ball[i][4] = changecolor()
        for g in range(N):
            if(i != g and (ball[i][0] - ball[g][0])**2 + (ball[i][1] - ball[g][1])**2 < (2 * ballr)**2):
                v1 = (ball[i][2] * (ball[g][0] - ball[i][0]) + ball[i][3] * (ball[g][1] - ball[i][1])) / (2 * ballr)
                v2 = (ball[g][2] * (ball[g][0] - ball[i][0]) + ball[g][3] * (ball[g][1] - ball[i][1])) / (2 * ballr)
                ball[i][0] -= ball[i][2] * part(ball[i][2], ball[i][3], ball[i][0], ball[i][1], ball[g][0], ball[g][1])
                ball[i][1] -= ball[i][3] * part(ball[i][2], ball[i][3], ball[i][0], ball[i][1], ball[g][0], ball[g][1])
                ball[i][2] += (v2 - v1) * (ball[g][0] - ball[i][0]) / (2 * ballr)
                ball[i][3] += (v2 - v1) * (ball[g][1] - ball[i][1]) / (2 * ballr)
                ball[g][2] += (v1 - v2) * (ball[g][0] - ball[i][0]) / (2 * ballr)
                ball[g][3] += (v1 - v2) * (ball[g][1] - ball[i][1]) / (2 * ballr)
                ball[i][4] = changecolor()
                ball[g][4] = changecolor()
        ball[i][3] += axel


def drawball():
    global ball, ballr, balld
    for i in range(N):
        penColor(ball[i][4])
        brushColor(ball[i][4])
        deleteObject(balld[i])
        balld[i] = circle(ball[i][0], ball[i][1], ballr)

def draw():
    moveball()
    drawwall()
    drawball()

onTimer(draw, 10)
run()