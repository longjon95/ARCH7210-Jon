import rhinoscriptsyntax as rs
import random as rd

#allObjs = rs.AllObjects()
#rs.DeleteObjects(allObjs)



class Turtle:
    def __init__(self, pos = [0,0,0], heading = [1,0,0]):
        self.point = rs.AddPoint(pos)
        pointPos = rs.PointCoordinates(self.point)
        self.direction = rs.VectorCreate(heading,pointPos)
        self.lines = []
    
    def forward(self,magnitude):
        print self.direction
        movement = rs.VectorScale(self.direction,magnitude)
        prevPos = rs.PointCoordinates(self.point)
        rs.MoveObject(self.point,movement)
        currentPos = rs.PointCoordinates(self.point)
        forwardLine = rs.AddLine(prevPos,currentPos)
        rs.DeleteObject(forwardLine)
        
    def left(self,angle):
        self.direction = rs.VectorRotate(self.direction, angle, [0,0,1])
        print(self.direction)
        
    def right(self,angle):
        self.direction = rs.VectorRotate(self.direction, -angle, [0,0,1])
        print(self.direction)
    
    def goto(self, x, y):
        prevPos = rs.PointCoordinates(self.point)
        movement = rs.VectorCreate([x,y,0],prevPos)
        rs.MoveObject(self.point,movement)
        currentPos = rs.PointCoordinates(self.point)
        gotoLine = rs.AddLine(prevPos,currentPos)
        rs.DeleteObject(gotoLine)
    
    
    def jitter(self, x , y, step):
        initialPosition = rs.PointCoordinates(self.point)
        for i in range(step):
            xJitter = initialPosition[0] + rd.uniform(0 , x)
            yJitter = initialPosition[1] + rd.uniform(0 , y)
            self.goto(xJitter, yJitter)
        self.goto(initialPosition[0], initialPosition[1])
    
    
    def curveJitter(self, x , y, step):
        initialPosition = rs.PointCoordinates(self.point)
        points = []
        degree = 3
        knots = step + degree - 1
        for i in range(step):
            xJitter = initialPosition[0] + rd.uniform(0,x)
            yJitter = initialPosition[1] + rd.uniform(0 , y)
            pt = rs.AddPoint([xJitter, yJitter, 0])
            points.append([xJitter, yJitter, 0])
            rs.DeleteObjects(pt)
        rs.AddCurve(points)

start = rs.GetPoint("Select initial position")
steps = input("Determine number of steps")

obj01 = Turtle(start)
#obj01 = obj01.jitter(20, 10, steps)
for i in range(10):
    obj01.goto((rd.uniform(0 , 100)),(rd.uniform(0 , 100)))
    obj01.curveJitter(20, 10, steps)