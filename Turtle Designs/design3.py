import turtle

turtle.bgcolor('black')
turtle.speed(0)
turtle.pensize(2)


for i in range(31):
    for colours in ['red', 'blue', 'yellow', 'cyan', 'green', 'white']:
        turtle.color(colours)
        turtle.forward(150)
        turtle.left(-181)
        turtle.forward(150)

turtle.exitonclick()
