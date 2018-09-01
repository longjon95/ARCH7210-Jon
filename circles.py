import rhinoscriptsyntax as rs

origin = [0,0,0]

rs.AddPoint(origin)

plane = rs.WorldXYPlane()

circle = rs.AddCircle( plane, 10.0 )

move = rs.MoveObject(circle, [0,0,20])

points = rs.DivideCurve(circle, 20)
for point in points: rs.AddPoint(point)

rs.DeleteObject(circle)

start = origin
if start:
    end = points
    if end: rs.AddLines(start, end)