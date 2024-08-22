import turtle

turtle.bgcolor("black")
turtle.speed(0)

colors = ["red", "orange", "white", "yellow", "green", "blue", "cyan"]

for i in range(5):
    for color in colors:
        turtle.color(color)
        turtle.pensize(3)
        turtle.left(12)
        for _ in range(4):  # This will create a square
            turtle.forward(200)
            turtle.left(270)

turtle.done()
