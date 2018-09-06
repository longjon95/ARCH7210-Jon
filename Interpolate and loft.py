import rhinoscriptsyntax as rs
import math

y = math.sin(math.radians(90))

s1 = rs.AddPoint(0,0,20)
e1 = rs.AddPoint(20,0,0)

s2 = rs.AddPoint(0,40,10)
e2 = rs.AddPoint(30,40,0)


#lineFrom = rs.GetPoint("Plane From:")
#lineTo = rs.GetPoint("Plane To:")
#distance = rs.Distance(lineFrom, lineTo)
#plane = rs.LinePlane([lineFrom, lineTo])
#rs.AddPlaneSurface( plane, distance, distance )

distance = rs.Distance(s1, e1)
plane = rs.LinePlane([s1, e1])
p1 = rs.AddPlaneSurface( plane, distance, distance )
rs.HideObject(p1)

distance = rs.Distance(s2, e2)
plane = rs.LinePlane([s2, e2])
p2 = rs.AddPlaneSurface( plane, distance, distance )
rs.HideObject(p2)

l1 = rs.AddLine(s1,e1)
l2 = rs.AddLine(s2,e2)

if l1:
    points1 = rs.DivideCurve(l1,20)
    for point in points1: rs.AddPoint(point)
    rs.MoveObjects(points1, y) 

if l2:
    points2 = rs.DivideCurve(l2,20)
    for point in points2: rs.AddPoint(point)






