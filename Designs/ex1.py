import turtle
t=turtle.Turtle()
screen=turtle.Screen()
screen.bgcolor('black')
screen.setup(400,400)
t.pensize(2)
t.speed(0)
t.color('blue')
for i in range(150):
    if i%10==0:
        t.lt(24)
    t.fd(90)
    t.lt(360/5)
turtle.done()