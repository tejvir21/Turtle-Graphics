import turtle as t
import random as rd

t.colormode(255)

artist = t.Turtle()

colour_list = [(213, 154, 96), (52, 107, 132), (179, 77, 31), (202, 142, 31),
               (115, 155, 171), (124, 79, 99),
               (122, 175, 156), (229, 236, 239), (226, 198, 131),
               (242, 247, 244), (192, 87, 108), (11, 50, 64), (55, 38, 19),
               (45, 168, 126), (47, 127, 123), (200, 121, 143), (168, 21, 29),
               (228, 92, 77), (244, 162, 160), (38, 32, 35), (2, 25, 24),
               (78, 147, 171), (170, 23, 18), (19, 79, 90), (101, 126, 158),
               (235, 166, 171), (177, 204, 185), (49, 62, 84)]

artist.penup()
artist.hideturtle()
artist.setx(-250)
artist.sety(-250)

for j in range(10):

    for i in range(10):
        artist.showturtle()
        artist.pendown()
        artist.dot(20, rd.choice(colour_list))
        artist.penup()
        artist.forward(50)

    artist.hideturtle()
    artist.setx(-250)
    artist.sety(-250 + 50 * (j + 1))

screen = t.Screen()
screen.exitonclick()
