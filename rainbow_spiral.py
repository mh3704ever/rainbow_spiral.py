import turtle

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtle.speed(0)
turtle.penup()
turtle.goto(0, 0)
turtle.pendown()

for i in range(500):
    color = colors[i % len(colors)]
    turtle.color(color)
    turtle.width(i/100+1)
    turtle.forward(i)
    turtle.right(181)

turtle.hideturtle()
turtle.done()
