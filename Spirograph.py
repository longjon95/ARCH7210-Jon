#Python Turtle - Spirograph - www.101computing.net/python-turtle-spirograph/

import turtle
from math import cos,sin
from time import sleep
import random

# http://www.101computing.net/python-turtle-spirograph/

window = turtle.Screen()
window.bgcolor("#FFFFFF")

m = turtle.Turtle()

R = random.randint(30,90)
print(R);
r = random.randint(0,360)
print(r);
d = 80

angle = 0

m.penup()
m.goto(R-r+d,0)
m.pendown()

theta = random.uniform(0.3,2.0)
print(theta);

steps = int(100*3.14/theta)

for t in range(0,steps):

    angle += theta

    x = (R - r) * cos(angle) - d * cos(((R-r)/r)*angle)
    y = (R - r) * sin(angle) - d * sin(((R-r)/r)*angle)

    m.goto(x,y)

print(R);
print(r);

turtle.done()

#homework implement other formulas
#make it random and crazy
