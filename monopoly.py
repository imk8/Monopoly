import turtle

t = turtle.Turtle()

sc = turtle.Screen()
sc.bgcolor('cadet blue')
sc.setup(width=550,height=550)


pen = t
pen.penup()
pen.goto(-225,225)
pen.pendown()
for i in range(4):
    t.forward(450)
    t.right(90)
turtle.done()
