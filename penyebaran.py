import matplotlib
import random
import turtle
import random
import time

start_time = time.time()
screen = turtle.Screen()
screen.setworldcoordinates(-20, -20, 550, 520)

x_max = 500
y_max = 500
y_min = 0
x_min = 0
x_range = x_max - x_min
y_range = y_max - y_min

# jumlah pergerakan
pergerakan = 100

# membuat grid
grid = turtle.Turtle()
grid.ht()
grid.color('black')

grid.pu()
grid.goto(0, 0)
grid.pd()
grid.speed(7)

for x in range(4):
    grid.forward(500)
    grid.left(90)


# membuat turtle
# colors = ["gold", "red", "lightgreen", "magenta", "blue",
#           "orange", "darkgreen", "cyan", "brown", "gray"]

# colors = ["green"]

turtles = []
haris = []
imuns = []
terjangkits = []
# membuat pen
for j in range(10):

    pen = turtle.Turtle()
    pen.speed(9)
    pen.shape('circle')
    pen.shapesize(0.3)
    pen.pensize(2)
    pen.color('green')
    imun = False

    terjangkits.append(False)
    imuns.append(False)
    haris.append(0)
    turtles.append(pen)
# buat yang terinfeksi
pen = turtle.Turtle()
pen.speed(7)
pen.shape('circle')
pen.shapesize(0.3)
pen.pensize(2)
pen.color('red')
turtles.append(pen)

# perulangan menaruh semua turtle yang telah dibuat pada posisi masing masing
for j in range(len(turtles)):

    turtles[j].pu()
    turtles[j].ht()
    # random antara x_min hingga x_max begitu pula pada y dengan kelipatan 25
    turtles[j].goto(random.randrange(x_min, x_max, 25),
                    random.randrange(y_min, y_max, 25))
    turtles[j].st()
    # turtles[j].pd()


for i in range(pergerakan-1):
    for j in range(len(turtles)):

        x = turtles[j].xcor()
        y = turtles[j].ycor()

        # menggunakan method random karena rangerange berisi integer
        turn = random.random()

        # menentukan arah
        if turn <= 0.25:
            x = x + 25
        elif turn <= 0.5:
            y = y + 25
        elif turn <= 0.75:
            x = x - 25
        else:
            y = y + 25

        if x > x_max:
            turtles[j].ht()
            turtles[j].pu()
            turtles[j].goto(x_min, y)
            x = x - x_range

        elif x < x_min:
            turtles[j].ht()
            turtles[j].pu()
            turtles[j].goto(x_max, y)
            x = x + x_range

        elif y > y_max:
            turtles[j].ht()
            turtles[j].pu()
            turtles[j].goto(x, y_min)
            y = y - y_range

        elif y < y_min:
            turtles[j].ht()
            turtles[j].pu()
            turtles[j].goto(x, y_max)
            y = y + y_range

        if (turtles[j].pencolor() == 'red'):
            for k in range(len(turtles)):
                if ((turtles[k].xcor()-turtles[j].xcor() == 25) or (turtles[k].xcor()-turtles[j].xcor() == -25) or (turtles[k].ycor()-turtles[j].ycor() == -25) or (turtles[k].ycor()-turtles[j].ycor() == 25)) and imuns[k] == False:
                    terinfeksi = random.random()
                    terinfeksi = terinfeksi/10
                    if (terinfeksi <= 0.05):
                        turtles[k].color('red')

        if (imuns[j] == False) and (terjangkits[j] == True):
            haris[j] = haris[j] + 1

        if (haris[j] == 10 and terjangkits[j] == True):
            turtles[j].color('green')
            imuns[j] = True

        turtles[j].st()
        # turtles[j].pd()
        turtles[j].goto(x, y)

print("time\t: %s" % (time.time() - start_time))
screen.exitonclick()
