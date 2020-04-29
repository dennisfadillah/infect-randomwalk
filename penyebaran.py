import matplotlib
import random
import turtle
import random
import time

start_time = time.time()
screen = turtle.Screen()
screen.setworldcoordinates(-5, -5, 25, 30)

x_max = 20
y_max = 20
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
    grid.forward(20)
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
for j in range(100):

    pen = turtle.Turtle()
    pen.speed(11)
    pen.shape('circle')
    pen.shapesize(0.3)
    pen.pensize(2)
    pen.color('green')

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
imuns.append(False)
haris.append(0)
terjangkits.append(True)

# perulangan menaruh semua turtle yang telah dibuat pada posisi masing masing
for j in range(len(turtles)):

    turtles[j].pu()
    turtles[j].ht()
    # random antara x_min hingga x_max begitu pula pada y dengan kelipatan 25
    turtles[j].goto(random.randrange(x_min, x_max, 1),
                    random.randrange(y_min, y_max, 1))
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
            x = x + 1
        elif turn <= 0.5:
            y = y + 1
        elif turn <= 0.75:
            x = x - 1
        else:
            y = y + 1

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
                if (((turtles[k].xcor()-turtles[j].xcor() == 0) and (turtles[k].ycor()-turtles[j].ycor() == 0)) and imuns[k] == False) and turtles[k] != turtles[j]:
                    terinfeksi = random.random()
                    # terinfeksi = terinfeksi/10
                    turtles[k].color('red')
                    terjangkits[k] = True
                    # if (terinfeksi <= 0.4):

        if (imuns[j] == False) and (terjangkits[j] == True):
            haris[j] = haris[j] + 1

        if (haris[j] == 10 and terjangkits[j] == True):
            turtles[j].color('green')
            imuns[j] = True
            terjangkits[j] = False

        turtles[j].st()
        # turtles[j].pd()
        turtles[j].goto(x, y)

print("time\t: %s" % (time.time() - start_time))
screen.exitonclick()
