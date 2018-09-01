import rhinoscriptsyntax as rs

import random

point = []

z = 0

for i in range(10):
    x = random.random() * 30
    y = random.random() * 30
    p = rs.AddPoint(x,y,z)
    point.append(p)

curve1 = rs.AddCurve(point)


for i in range(10):
    x = random.random() * 30
    y = random.random() * 30
    p = rs.AddPoint(x,y,z)
    point.append(p)

curve2 = rs.AddCurve(point)
move = rs.MoveObject(curve2, [0,0,10])

curves = [curve1,curve2]

if curves: rs.AddLoftSrf(curves)
