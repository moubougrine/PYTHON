from turtle import *
bgcolor('black')
speed(0)
pensize(2)
hideturtle()
for i in range (300):
    color('olive')
    circle(i)
    color('cyan')
    circle(i*1.5)
    right(5)
    forward(3)
done()