import  turtle as t

sketcher = t.Turtle()

# press W to move forward
def move_forward():
    sketcher.forward(10)

# press S to move backward
def move_backward():
    sketcher.back(10)

# press A to move anticlockwise
def move_anticlockwise():
    sketcher.left(10)

# press D to move clockwise
def move_clockwise():
    sketcher.right(10)

# press C to clear screen
def screen_clear():
    sketcher.clear()
    sketcher.penup()
    sketcher.home()
    sketcher.pendown()

screen = t.Screen()

screen.listen()

sketcher.speed('fastest')

screen.onkey(key='w',fun=move_forward)
screen.onkey(key='s',fun=move_backward)
screen.onkey(key='d',fun=move_clockwise)
screen.onkey(key='a',fun=move_anticlockwise)
screen.onkey(key='c',fun=screen_clear)

screen.exitonclick()
