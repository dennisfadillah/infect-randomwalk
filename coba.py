import turtle
import random

screen = turtle.Screen()
turtles = []

pen = turtle.Turtle()
pen.color('red')
pen.pu()
turtles.append(pen)

pen = turtle.Turtle()
pen.color('green')
pen.pu()
turtles.append(pen)

terinfeksi = random.random()
print(terinfeksi)
print(turtles[1].pencolor())

turtles[0].goto(200, 100)
turtles[1].goto(165, 125)

haris = []
imuns = []
terjangkits = []

terjangkits.append(False)
imuns.append(False)
haris.append(0)

print(len(terjangkits))
print(len(imuns))
print(len(haris))


screen.exitonclick()
