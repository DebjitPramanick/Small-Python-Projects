import turtle

turtle.bgcolor('black')
turtle.pensize(2)
turtle.speed(0)
turtle.color('white')
angle = 90

for i in range(100):
    turtle.left(12)
    turtle.forward(150)
    turtle.left(90)
    turtle.forward(150)
    turtle.left(90)
    turtle.forward(150)
    turtle.left(90)
    turtle.forward(150)
    turtle.left(90)

turtle.exitonclick()
