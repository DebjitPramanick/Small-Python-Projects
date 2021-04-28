import turtle

turtle.bgcolor('black')
turtle.pensize(2)
turtle.speed(0)
turtle.color('white')

for i in range(50):
    turtle.circle(2*i)
    turtle.circle(-2*i)
    turtle.left(i)

turtle.exitonclick()
