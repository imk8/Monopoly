import turtle

t = turtle.Turtle()
t.speed(0)


def screen():
    sc = turtle.Screen()
    sc.bgcolor('dark sea green')
    sc.setup(width=600,height=600)



def square(length, breadth, dist):
    t.penup()
    t.goto(length, breadth)
    t.pendown()
    for i in range(4):
        t.forward(dist)
        t.right(90)
    

def htile(x,y,colour,name):
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.fillcolor(colour)
    t.begin_fill()
    for i in range(2):
        t.forward(50)
        t.right(90)
        t.forward(15)
        t.right(90)
    t.end_fill()

    pen = turtle.Turtle()
    pen.speed(0)
    pen.color('black')
    pen.penup()
    if y<0:
        pen.goto(x+25,y-25)
    else:
        pen.goto(x+25,y+25)
    pen.write(name, align='center', font=('Courier', 8, 'bold'))
    pen.hideturtle()

def vtile(x,y,colour,name):
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.fillcolor(colour)
    t.begin_fill()
    for i in range(2):
        t.forward(15)
        t.right(90)
        t.forward(50)
        t.right(90)
    t.end_fill()

    pen = turtle.Turtle()
    pen.speed(0)
    pen.color('black')
    pen.penup()
    if x<0:
        pen.goto(x-10,y-25)
    else:
        pen.goto(x+25,y-25)
    pen.write(name, align='center', font=('Courier', 8, 'bold'))
    pen.hideturtle()

def h_lines(x,y):
    t.penup()
    t.goto(x,y)
    for i in range(9):
        t.pendown()
        t.forward(50)
        t.right(90)
        t.forward(50)
        t.right(90)
        t.forward(50)
        t.right(180)

def v_lines(x,y):
    t.penup()
    t.goto(x,y)
    for i in range(9):
        t.pendown()
        t.right(90)
        t.forward(50)
        t.left(90)
        t.forward(50)
        t.left(90)
        t.forward(50)
        t.right(90)



screen()
square(-225,225,450)
square(-275,275,550)
h_lines(-275,225)
h_lines(225,225)
v_lines(-225,275)
v_lines(-225,-225)

#Horizontal Colour Tiles

htile(175,-225,"dark red","BR1\n60")
htile(75,-225,"dark red", "BR2\n60")
htile(-225,-225,"medium turquoise","LB3")
htile(-175,-225,"medium turquoise","LB2")
htile(-75,-225,"medium turquoise","LB1")
htile(-225,240,"red","R1")
htile(-125,240,"red","R2")
htile(-75,240,"red","R3")
htile(25,240,"yellow","Y1")
htile(75,240,"yellow","Y2")
htile(175,240,"yellow","Y3")

#Vertical Colour Tiles
vtile(-240,225,"orange","O3")
vtile(-240,175,"orange","O2")
vtile(-240,75,"orange","O1")

vtile(-240,-25,"deep pink","P3")
vtile(-240,-75,"deep pink","P2")
vtile(-240,-175,"deep pink","P1")

vtile(225,225,"green","G1")
vtile(225,175,"green","G2")
vtile(225,75,"green","G3")

vtile(225,-75,"blue","B1")
vtile(225,-175,"blue","B2")


turtle.done()





