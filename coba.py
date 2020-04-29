import turtle

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

turtles[0].goto(200, 100)
turtles[1].goto(165, 125)

if ((turtles[1].xcor()-turtles[0].xcor() == 25) or (turtles[1].xcor()-turtles[0].xcor() == -25) or (turtles[1].ycor()-turtles[0].ycor() == -25) or (turtles[1].ycor()-turtles[0].ycor() == 25)):
    turtles[1].color('red')
    # for k in range(len(turtles)):
    #     if (turtles[j].color() == 'red'):
    #         # if (turtles[k].xcor()-turtles[j].xcor() == 25) or (turtles[k].xcor()-turtles[j].xcor() == -25) or (turtles[k].ycor()-turtles[j].ycor() == -25) or (turtles[k].ycor()-turtles[j].ycor() == 25):
    #         if (turtles[k])
    #         turtles[k].color('red')
    #         # terinfeksi = random.Random()
    #         # if (terinfeksi <= 0.05):


screen.exitonclick()
