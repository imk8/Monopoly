import turtle
import random

t = turtle.Turtle()
t.speed(0)
p1c = turtle.Turtle()
p2c = turtle.Turtle()
r = turtle.Turtle()


def screen(): # SCREEN COLOUR, SIZE
    sc = turtle.Screen()
    sc.bgcolor('dark sea green')
    sc.setup(width=600,height=600)

def square(length, breadth, dist): #BORDERS
    t.penup()
    t.goto(length, breadth)
    t.pendown()
    for i in range(4):
        t.forward(dist)
        t.right(90)
    t.hideturtle()
    
def htile(x,y,colour,name): #HORIZONTAL PROPERTIES
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

    t.speed(0)
    t.color('black')
    t.penup()
    if y<0:
        t.goto(x+25,y-30)
    else:
        t.goto(x+25,y+10)
    t.write(name, align='center', font=('Courier', 8, 'bold'))
    t.hideturtle()

def vtile(x,y,colour,name): #VERTICAL PROPERTIES
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

    t.speed(0)
    t.color('black')
    t.penup()
    if x<0:
        t.goto(x-10,y-25)
    else:
        t.goto(x+30,y-25)
    t.write(name, align='center', font=('Courier', 8, 'bold'))
    t.hideturtle()

def h_lines(x,y): #HORIZONTAL GRID LINES
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

def v_lines(x,y): #VERTICAL LINES
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

def centre(): #words in centre
    t.penup()
    t.goto(0,0)
    t.write("MONOPOLY", align='center', font=('Courier', 35, 'bold'))
    t.hideturtle()

def roll_dice():
    return (random.randint(2,12))

def p1_cash_display(c):
    p1c.hideturtle()
    p1c.penup()
    p1c.goto(-100,-75)
    to_be_printed = "P1 Cash=" + str(c)
    p1c.write(to_be_printed, align='center', font=('Courier', 15, 'bold'))

def p2_cash_display(c):
    p2c.hideturtle()
    p2c.penup()
    p2c.goto(100,-75)
    to_be_printed = "P2 Cash=" + str(c)
    p2c.write(to_be_printed, align='center', font=('Courier', 15, 'bold'))
    
def rent_display(p,rent_cost):
    r.hideturtle()
    r.penup()
    r.goto(0,75)
    to_be_printed = "P{} owns this,${} charged".format(p,rent_cost)
    r.write(to_be_printed, align='center', font=('Courier', 15, 'bold'))

class Tile: 
    def __init__(self, price, rent, ownership, design):
        self.p = price
        self.r = rent
        self.o = ownership
        self.d = design        


#SCREEN, GRID
t.hideturtle()
centre()
screen()
square(-225,225,450)
square(-275,275,550)
h_lines(-275,225)
h_lines(225,225)
v_lines(-225,275)
v_lines(-225,-225)
t.hideturtle()



t0 = Tile(00,0,3,htile(225,-225,"dark magenta","GO")) 
t1 = Tile(60,6,0,htile(175,-225,"brown","BR1"))
t2 = Tile(00,-100,3,htile(125,-225,"dark magenta","$100"))
t3 = Tile(60,6,0,htile(75,-225,"brown", "BR2"))
t4 = Tile(00,200,3,htile(25,-225,"light slate gray", "-$200"))
t5 = Tile(200,20,0,htile(-25,-225,"black", "T1"))
t6 = Tile(100,10,0,htile(-75,-225,"medium turquoise","LB1"))
t7 = Tile(0,100,3,htile(-125,-225,"light slate gray","-$100"))
t8 = Tile(100,10,0,htile(-175,-225,"medium turquoise","LB2"))
t9 = Tile(120,12,0,htile(-225,-225,"medium turquoise","LB3"))

t10 = Tile(0,0,3,htile(-275,-225,"light slate gray","JAIL"))

t11 = Tile(140,14,0,vtile(-240,-175,"deep pink","P1"))
t12 = Tile(150,15,0,vtile(-240,-125,"white","U1"))
t13 = Tile(140,14,0,vtile(-240,-75,"deep pink","P2"))
t14 = Tile(160,16,0,vtile(-240,-25,"deep pink","P3"))
t15 = Tile(200,20,0,vtile(-240,25,"black","T2"))
t16 = Tile(180,18,0,vtile(-240,75,"orange","O1"))
t17 = Tile(00,-50,3,vtile(-240,125,"dark magenta","$50"))
t18 = Tile(180,18,0,vtile(-240,175,"orange","O2"))
t19 = Tile(200,20,0,vtile(-240,225,"orange","O3"))

t20 = Tile(0,-200,3,htile(-275,240,"dark magenta","$200"))

t21 = Tile(220,22,0,htile(-225,240,"red","R1"))
t22 = Tile(00,-50,3,htile(-175,240,"dark magenta","$50"))
t23 = Tile(220,22,0,htile(-125,240,"red","R2"))
t24 = Tile(240,24,0,htile(-75,240,"red","R3"))
t25 = Tile(200,20,0,htile(-25,240,"black","T3"))
t26 = Tile(260,26,0,htile(25,240,"yellow","Y1"))
t27 = Tile(260,26,0,htile(75,240,"yellow","Y2"))
t28 = Tile(150,15,0,htile(125,240,"white","U2"))
t29 = Tile(260,26,0,htile(175,240,"yellow","Y3"))

t30 = Tile(0,0,3,htile(225,240,"light slate gray","GOJAIL"))

t31 = Tile(300,30,0,vtile(225,225,"green","G1"))
t32 = Tile(300,30,0,vtile(225,175,"green","G2"))
t33 = Tile(00,-150,3,vtile(225,125,"dark magenta","$150"))
t34 = Tile(320,30,0,vtile(225,75,"green","G3"))
t35 = Tile(200,20,0,vtile(225,25,"black","T4"))
t36 = Tile(0,100,3,vtile(225,-25,"light slate gray","-$100"))
t37 = Tile(350,35,0,vtile(225,-75,"blue","B1"))
t38 = Tile(00,-50,3,vtile(225,-125,"dark magenta","$50"))
t39 = Tile(400,40,0,vtile(225,-175,"blue","B2"))



dd= {
    0:t0,1:t1,2:t2,3:t3,4:t4,5:t5,6:t6,7:t7,8:t8,9:t9,10:t10,
    11:t11,12:t12,13:t13,14:t14,15:t15,16:t16,17:t17,18:t18,19:t19,20:t20,
    21:t21,22:t22,23:t23,24:t24,25:t25,26:t26,27:t27,28:t28,29:t29,30:t30,
    31:t31,32:t32,33:t33,34:t34,35:t35,36:t36,37:t37,38:t38,39:t39,40:t0
}

#Player Mechanics, info

p1 = turtle.Turtle()
p1.penup()
p1.goto(250,-250)
p1.right(90)
p1.color("blue")
cp1 = 0 #current position
p1_cash = 1000

p2 = turtle.Turtle()
p2.penup()
p2.goto(250,-250)
p2.right(90)
p2.color("red")
cp2 = 0 #current position
p2_cash = 1000




#GAMEPLAY, MOVEMENT
while p1_cash >=0 and p2_cash>= 0:


    #Player 1 Movement
    wn = turtle.Screen()
    answer = wn.textinput("P1 Next Roll", "Press OK to roll the dice, Cancel to quit:")
    r.clear()

    if answer is None:
        break

    for i in range(roll_dice()):
        if cp1 == 0 or cp1 == 10 or cp1 == 20 or cp1 == 30 or cp1 == 40:
            if cp1 == 40:
                cp1 = 0
                p1_cash+=100
            p1.right(90)
            p1.forward(50)
            cp1 += 1 
        else:
            p1.forward(50)
            cp1 += 1
    
    if dd[cp1].o == 0:
        y_n = wn.textinput("P1 Purchase?","Type Y to purchase for ${}".format(dd[cp1].p))

        if y_n == "Y":
            r.clear()
            dd[cp1].o = 1
            p1_cash -= dd[cp1].p

    elif dd[cp1].o == 2:
        rent_display(2,dd[cp1].r)
        p1_cash -= dd[cp1].r
        p2_cash += dd[cp1].r

    else:
        p1_cash -= dd[cp1].r

    
    p1c.clear()    
    p1_cash_display(p1_cash)
    p2c.clear()
    p2_cash_display(p2_cash)
    
    

    #Player 2 Movement
    wn = turtle.Screen()
    answer = wn.textinput("P2 Next Roll", "Press OK to roll the dice, Cancel to quit:")
    r.clear()

    if answer is None:
        break

    for i in range(roll_dice()):
        if cp2 == 0 or cp2 == 10 or cp2==20 or cp2==30 or cp2 ==40:
            if cp2 == 40:
                cp2 = 0
                p2_cash+=100
            p2.right(90)
            p2.forward(50)
            cp2 += 1 
        else:
            p2.forward(50)
            cp2 += 1        

    if dd[cp2].o == 0:
        y_n = wn.textinput("P2 Purchase?","Type Y to purchase for ${}".format(dd[cp2].p))
        if y_n == "Y":
            dd[cp2].o = 2
            p2_cash -= dd[cp2].p
            
    elif dd[cp2].o == 1:
        r.clear()
        rent_display(1,dd[cp2].r)
        p2_cash -= dd[cp2].r
        p1_cash += dd[cp2].r

    else:
        p2_cash -= dd[cp2].r

        
    p1c.clear()    
    p1_cash_display(p1_cash)
    p2c.clear()
    p2_cash_display(p2_cash)
    

if p1_cash <0:
    winner = "P2 Wins !!!"
    r.write(winner, align='center', font=('Courier', 15, 'bold'))
else:
    winner = "P1 Wins !!!"
    r.write(winner, align='center', font=('Courier', 15, 'bold'))

turtle.done()
