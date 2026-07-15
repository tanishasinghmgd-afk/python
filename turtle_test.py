"""import turtle #importing library
turtle.Screen().bgcolor("orange")
turtle.Screen().setup(300,400)
polygon = turtle.Turtle() #defined variable

num_sides = 6 #variable
side_length = 70
angle = 360.0/num_sides
#iterate loop for total number of side
for i in range(num_sides):
    polygon.forward(side_length)
    polygon.right(angle)

turtle.done()"""




import turtle
turtle.Screen().bgcolor("Aqua")
board = turtle.Turtle()

#first tirangle of star
board.forward(100) #draw base

board.left(120)
board.forward(100)

board.left(120)
board.forward(100)

board.penup()
board.right(150)
board.forward(50)

#second triangle for star
board.pendown()
board.right(90)
board.forward(100)

board.right(120)
board.forward(100)

board.right(120)
board.forward(100)

turtle.done()



"""import turtle
my_wn = turtle.Screen()
my_wn.bgcolor("light blue")
my_wn.title("turtle")
my_pen = turtle.Turtle()
size = 0
while True:
    for i in range(4):
        my_pen.fd(size + 1)
        my_pen.left(90)
        side = size - 5
    size = size + 1"""


"""import turtle
screen = turtle.Screen()
screen.bgcolor("light pink")

my_turtle = turtle.Turtle()
my_turtle.color("purple")
my_turtle.pensize(5)
my_turtle.speed(3)

for i in range(4):
    my_turtle.forward(100)
    my_turtle.right(90)

screen.exitoncl"""


