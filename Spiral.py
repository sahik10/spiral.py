import turtle

turtle.speed(0)
turtle.bgcolor("Yellow")

for i in range(10) :
        for colours in ["red", "magenta", "blue", "cyan", "yellow", "white"] :
                turtle.color(colours)
                turtle.pensize(3)
                turtle.left(12)
                turtle.forward(200)
                turtle.left(90)
                turtle.forward(200)
                turtle.left(90)
                turtle.forward(200)
                turtle.left(90)
                turtle.forward(200)
                turtle.left(90)
