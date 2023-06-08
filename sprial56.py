import turtle

from itertools import cycle
colors=cycle(['red','orange','black','green','pink','purple'])


def draw_circle(size,angle,shift):
  turtle.bgcolor(next(colors))
  turtle.pencolor(next(colors))
  turtle.circle(size)
  turtle.right(angle)
  turtle.forward(shift)
  draw_circle(size+1,angle+1,shift+1)

turtle.bgcolor('black')
turtle.speed('fast')
turtle.pensize(46)
draw_circle(30,0,1)
