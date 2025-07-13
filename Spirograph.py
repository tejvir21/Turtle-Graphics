import turtle as t
import random as rd
import math

artist = t.Turtle()
t.colormode(255)

def random_color():
    r = rd.randint(0,255)
    g = rd.randint(0,255)
    b = rd.randint(0,255)
    random_colour = (r, g, b)
    return random_colour

def spirograph(n):
    for i in range(math.ceil(360/n)):
        artist.color(random_color())
        artist.circle(100)
        artist.speed('fastest')
        current_heading = artist.heading()
        artist.setheading(current_heading + n)
'''
for i in range(36):
    artist.color(random_color())
    artist.circle(100)
    artist.speed('fastest')
    current_heading = artist.heading()
    artist.setheading(current_heading + 10)
'''

spirograph(4)

screen = t.Screen()
screen.exitonclick()
