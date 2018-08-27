import turtle

turtle.setup(1000,1000)

sq=turtle.Turtle()

turtle.hideturtle()

n = 0

sq.speed(0)


while n < 12:

    sq.color('#33FFF6')
    for i in range(6):
        sq.forward(100)
        sq.right(60)
    sq.color('#33E0FF')
    for i in range(6):
        sq.forward(80)
        sq.right(60)
    sq.color('#33B2FF')
    for i in range(6):
        sq.forward(60)
        sq.right(60)
    
    sq.color('#FF33A8')
    for i in range(3):
        sq.forward(120)
        sq.right(120)
    sq.color('#FF3374')
    for i in range(3):
        sq.forward(100)
        sq.right(120)
    sq.color('#FF3352')
    for i in range(3):
        sq.forward(80)
        sq.right(120)
    sq.left(30)
    n+=1

turtle.exitonclick()

#'#FF338D','#FF3377','#33C7FF'
