import turtle as t
import random as rd

colors = ['red','blue','green','orange','yellow','purple']
y_positions = [-70,-40,-10,20,50,80]

all_turtles = []
is_race_on = False

screen = t.Screen()

screen.setup(width=500,height=400)

for turtle_index in range(6):
    new_turtle = t.Turtle(shape='turtle')
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

user_pet = screen.textinput(title='Make your pet',prompt='Which turtle will win the race? Enter a colour: ')

if user_pet:
    is_race_on = True

while is_race_on:
    for turtle_index in all_turtles:
        turtle_index.setx(turtle_index.xcor() + rd.randint(0,10))

        if turtle_index.xcor() >= 230:
            if turtle_index.pencolor() == user_pet:
                print(f'Your pet wins the race. The {turtle_index.pencolor()} turtle is the winner.')
                break
            else:
                print(f'You lose the race. The {turtle_index.pencolor()} turtle is the winner.')
                break
    if turtle_index.xcor() >= 230:
        break

screen.exitonclick()
