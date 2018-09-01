import rhinoscriptsyntax as rs

n = 0

plane = rs.WorldXYPlane()

for rect in range(20):
    rect = rs.AddRectangle( plane, 5.0, 5.0 )
    plane = rs.RotatePlane(plane, 18, [0,0,1])

move = rs.MoveObject(rect, [0,0,2])