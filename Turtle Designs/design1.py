import turtle

turtle.bgcolor('black')
turtle.pensize(2)
turtle.speed(0)

for i in range(6):
    for colours in ['red','blue','yellow','cyan','green','white']:
        turtle.color(colours)
        turtle.circle(100)
        turtle.left(10)
    
turtle.hideturtle()
