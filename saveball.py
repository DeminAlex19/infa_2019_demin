from tkinter import *
from random import randrange as rnd, choice
import time
root = Tk()
wall_right = 600
wall_left = 0
r_geometry = str(wall_right) + 'x' + str(wall_right + 53)
root.geometry(r_geometry)
time_new = 1000
time_reaction = 3000
delay_drawing = 20
max_radius = 40
min_radius = 30
max_velocity = 5
num_epochs = 10
iteration = 0
score = 0
cost_circle = 15
cost_square = 10
canv = Canvas(root, bg = 'white')
canv.pack(fill = BOTH, expand = 1)
colors = ['red', 'orange', 'green', 'blue', 'yellow', 'purple', 'maroon']
type_obj = ['circle', 'square']
fig = []
l = Label(root, bg = 'cyan', fg = 'black', width = 40, font="Arial 32")



class figure:
    s = 0
    ss = 0
    iteration_move = 0
    def __init__(self, num):
        self.x = rnd(wall_left + 120, wall_right - 150)
        self.y = rnd(wall_left + 120, wall_right - 150)
        self.vx = rnd(-max_velocity, max_velocity)
        self.vy = rnd(-max_velocity, max_velocity)
        self.r = rnd(min_radius, max_radius)
        self.color = choice(colors)
        self.num = num
        self.create()
        self.move()

    def delete(self):
        root.after_cancel(self.ss)
        canv.delete(self.s)
        for el in fig:
            if (el.num > self.num):
                el.num -= 1
        fig.pop(self.num)

    def move(self):
        if (self.x + self.r + self.vx >= wall_right):
            self.x = wall_right - self.r + (wall_right - self.r - self.x)
            self.vx = - self.vx
            canv.delete(self.s)
            self.create()
        if (self.x - self.r + self.vx <= wall_left):
            self.x = wall_left + self.r + (wall_left + self.r - self.x)
            self.vx = - self.vx
            canv.delete(self.s)
            self.create()
        if (self.y + self.r + self.vy >= wall_right):
            self.y = wall_right - self.r + (wall_right - self.r - self.y)
            self.vy = - self.vy
            canv.delete(self.s)
            self.create()
        if (self.y - self.r + self.vy <= wall_left):
            self.y = wall_left + self.r + (wall_left + self.r - self.y)
            self.vy = - self.vy
            canv.delete(self.s)
            self.create()
        canv.move(self.s, self.vx, self.vy)
        self.x += self.vx
        self.y += self.vy
        if (self.iteration_move < time_reaction / delay_drawing):
            self.iteration_move += 1
            self.ss = root.after(delay_drawing, self.move)
        else:
            self.delete()




class circle(figure):
    cl = 'circle'
    def create(self):
        self.s = canv.create_oval(self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r, fill = self.color, width = 0)



class square(figure):
    cl = 'square'
    def create(self):
        self.s = canv.create_rectangle(self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r, fill = self.color, width = 0)



def save():
    global score
    l['text'] = 'Total', 'score:', score
    f = open('Scores.txt', 'a')
    f.write("%s\n" % str(score))
    f.close



def gif():
    global num_epochs, type_obj, iteration
    s = choice(type_obj)
    if(iteration == 0):
        l['text'] = 'Score:', score
    if(s == 'circle'):
        fig.append(circle(len(fig)))
    else:
        fig.append(square(len(fig)))
    if (iteration == num_epochs):
        root.after(time_reaction + delay_drawing, save)
    if(iteration < num_epochs):
        iteration += 1
        root.after(time_new, gif)



def click(event):
    global score, cost_circle, cost_square, iteration
    for el in fig:
        if(el.cl == 'circle' and (event.x - el.x)**2 + (event.y - el.y)**2 <= el.r**2):
            score += cost_circle
            el.delete()
        elif(el.cl == 'square' and event.x <= el.x + el.r and event.x >= el.x - el.r and event.y <= el.y + el.r and event.y >= el.y - el.r):
            score += cost_square
            el.delete()

    if(iteration <= num_epochs):
        l['text'] = 'Score:', score



gif()
l.pack()
canv.bind('<Button-1>', click)
root.mainloop()