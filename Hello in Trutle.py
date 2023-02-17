import turtle

# membuat turtle
pen = turtle.Turtle()
x = -450
y = 0

# tulisan "H"
pen.color("red")
pen.pu()  # mengangkat pena
pen.goto(x,y)  # pindah ke koordinat (-150, 0)
pen.pd()  # menurunkan pena
pen.left(90)  # memutar turtle 90 derajat ke kiri
pen.forward(250)  # maju 100 piksel
pen.right(90)  # memutar turtle 90 derajat ke kanan
pen.forward(50)
pen.right(90)
pen.forward(100)

pen.left(90)
pen.forward(50)
pen.left(90)
pen.forward(100)
pen.right(90)
pen.forward(50)
pen.right(90)
pen.forward(250)

pen.right(90)
pen.forward(50)
pen.right(90)
pen.forward(100)
pen.left(90)
pen.forward(50)
pen.left(90)
pen.forward(100)
pen.right(90)
pen.forward(50)

# huruf E
pen.color("white")
x = x + 200
y = y + 250
pen.goto(x,y)
pen.color("red")
pen.left(90)
pen.forward(250)
pen.left(90)
pen.forward(150)
pen.left(90)
pen.forward(50)
pen.left(90)
pen.forward(100)
pen.right(90)
pen.forward(50)
pen.right(90)
pen.forward(100)
pen.left(90)
pen.forward(50)
pen.left(90)
pen.forward(100)
pen.right(90)
pen.forward(50)
pen.right(90)
pen.forward(100)
pen.left(90)
pen.forward(50)
pen.left(90)
pen.forward(150)

#huruf L
pen.color("white")
x = x + 200
pen.goto(x,y+50)
pen.goto(x,y)
pen.color("red")
pen.left(90)
pen.forward(250)
pen.left(90)
pen.forward(150)
pen.left(90)
pen.forward(50)
pen.left(90)
pen.forward(100)
pen.right(90)
pen.forward(200)
pen.left(90)
pen.forward(50)

#huruf L
pen.color("white")
x = x + 200
pen.goto(x,y+50)
pen.goto(x,y)

pen.color("red")
pen.right(270)
pen.forward(250)
pen.left(90)
pen.forward(150)
pen.left(90)
pen.forward(50)
pen.left(90)
pen.forward(100)
pen.right(90)
pen.forward(200)
pen.left(90)
pen.forward(50)

#huruf o
pen.color("white")
x = x + 200
pen.goto(x,y+50)
pen.goto(x,y)

pen.color("red")
pen.left(90)
pen.forward(250)
pen.left(90)
pen.forward(150)
pen.left(90)
pen.forward(250)
pen.left(90)
pen.forward(150)
pen.left(90)
pen.forward(50)
pen.left(90)
pen.color("white")
pen.forward(50)
pen.color("red")
pen.forward(50)
pen.right(90)
pen.forward(150)
pen.right(90)
pen.forward(50)
pen.right(90)
pen.forward(150)

turtle.done()


