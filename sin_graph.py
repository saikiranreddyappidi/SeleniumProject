import turtle
import math

# Set up the turtle screen and window
wn = turtle.Screen()
wn.setup(width=800, height=600)
wn.setworldcoordinates(-math.pi, -1.5, math.pi, 1.5)

# Draw the x and y axes with red color
turtle.pensize(3)
turtle.speed(100)

# Draw the x and y axis grids with light blue color
turtle.pencolor('light blue')
for x in range(-16, 17):
    turtle.penup()
    turtle.goto(x*math.pi/16, -1.5)
    turtle.pendown()
    turtle.goto(x*math.pi/16, 1.5)
for y in range(-16, 17):
    turtle.penup()
    turtle.goto(-math.pi, y/8)
    turtle.pendown()
    turtle.goto(math.pi, y/8)

turtle.penup()
turtle.goto(-math.pi, 0)
turtle.pendown()
turtle.pencolor('red')
turtle.goto(math.pi, 0)
turtle.penup()
turtle.goto(0, -1.5)
turtle.pendown()
turtle.goto(0, 1.5)

# Draw the sine wave
turtle.pencolor('green')
turtle.penup()
turtle.goto(-math.pi, 0)
turtle.pendown()
for x in range(-314, 315):
    turtle.goto(x/100, -math.sin(x/100))
turtle.penup()
turtle.hideturtle()
# Exit on click
turtle.exitonclick()
