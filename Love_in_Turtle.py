import turtle

# mengatur ukuran layar
turtle.setup(width=600, height=400)

def love(x,y):
    x= x + 0
    y= y - 150

    turtle.color("white")
    turtle.hideturtle()
    turtle.pensize(1)
    turtle.goto(x,y)

    j=0
    i=0
    turtle.color("red")
    turtle.left(33)
    turtle.begin_fill()
    for i in range (23):
        turtle.forward(20)
        turtle.left(i)
    turtle.end_fill()

    turtle.color("white")
    turtle.goto(x,y)

    j=1
    i=0
    turtle.color("red")
    turtle.begin_fill()
    turtle.right(142)
    for i in range (23):
        turtle.forward(20)
        turtle.right(i)
    turtle.left(30)
    turtle.forward(30)
    turtle.end_fill()

love(0,0)

turtle.done()


