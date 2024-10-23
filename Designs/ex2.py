import turtle
t=turtle.Turtle()
s = turtle.Screen()
colors=['orange','red','magenta','blue','magenta','yellow','green','yan','purple']
s.bgcolor('black')
t.pensize('2')
t.speed(0)
for i in range (360):
    t.pencolor(colors[i%6])
    t.width(i//100+1)
    t.forward(i)
    t.right(50)
    turtle.hideturtle()
turtle.done()
