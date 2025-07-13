import turtle as t
import random as rd
#import differentshapes as ds

colours = ['green','yellow','orange','pink','purple','CornflowerBlue','DarkOrchid','IndianRed','DeepSkyBlue','LightSeaGreen','wheat','SlateGray','SeaGreen']
t.colormode(255)
def random_color():
    r = rd.randint(0,255)
    g = rd.randint(0,255)
    b = rd.randint(0,255)
    random_color = (r, g, b)
    return random_color

artist = t.Turtle()
artist.pensize(15)
'''
def turn_right():
    colour = r.choice(colours)
    artist.color(colour)
    artist.right(90)

def turn_left():
    colour = r.choice(colours)
    artist.color(colour)
    artist.left(90)

def turn_around():
    colour = r.choice(colours)
    artist.color(colour)
    artist.back(30)
'''
for i in range(2000):
    artist.setheading(rd.choice([0,90,180,270]))
    '''
    start_walk = r.choice(['l', 'r', 'b'])
    if start_walk == 'l':
        turn_left()
    elif start_walk == 'r':
        turn_right()
    else:
        turn_around()
    '''
    #colour = rd.choice(colours)
    artist.color(random_color())

    artist.speed('fastest')

    artist.forward(30)

screen = t.Screen()
screen.exitonclick()
