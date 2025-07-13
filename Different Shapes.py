import turtle as t
import random as r

colours = ['green','yellow','orange','pink','purple','CornflowerBlue','DarkOrchid','IndianRed','DeepSkyBlue','LightSeaGreen','wheat','SlateGray','SeaGreen']

artist = t.Turtle()

def polygon(n):
  colour = r.choice(colours)
  artist.color(colour)

  for i in range(n):
      artist.forward(100)
      artist.right(360/n)

n = int(input('Enter number of sides: '))
polygon(n)

screen=t.Screen()
screen.exitonclick() oh
