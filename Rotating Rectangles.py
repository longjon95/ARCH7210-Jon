import rhinoscriptsyntax as rs

plane = rs.WorldXYPlane()



for curves in range(20):
    for rect in range(20):
        rect = rs.AddRectangle(plane, 5.0, 5.0 )
        plane = rs.RotatePlane(plane, 18, [0,0,1])
    move = rs.MoveObject(curves, [0,0,y])