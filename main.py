import random
import turtle
from turtle import Turtle, Screen

#
# def move_forward():
#     tim.forward(10)

# def move_back():
#     tim.backward(10)
#
#
# def turn_left():
#     tim.setheading(tim.heading() - 10)
#     tim.forward(10)
#
#
# def turn_right():
#     tim.setheading(tim.heading() + 10)
#     tim.forward(10)
# def clear():
#     tim.clear()
#     tim.penup()
#     tim.home()


turtle.colormode(255)
screen = Screen()
screen.listen()
# screen.onkeypress(move_forward, "w")
# screen.onkeypress(move_back, "s")
# screen.onkeypress(turn_left, "a")
# screen.onkeypress(turn_right, "d")
# screen.onkey(clear,'c')
alex = Turtle()
alex.shape('turtle')
alex.pensize(7)
alex.penup()
alex.setpos(280, 260)
alex.stamp()
alex.pendown()
alex.right(90)
alex.forward(500)
alex.left(90)
alex.stamp()
alex.penup()

names = ('alex', 'benji', 'chris', 'dan', 'ellie')
t = {alex: names[0]}

for i in range(1, 5):
    p = Turtle()
    p.shape('turtle')
    t[p] = names[i]

# print(t)
colors = [(246, 223, 240), (204, 215, 121), (70, 123, 86), (134, 226, 158), (205, 219, 242), (108, 101, 189),
          (56, 41, 147), (117, 31, 112), (228, 164, 210), (175, 172, 236), (185, 102, 88), (70, 154, 168), (26, 47, 81),
          (72, 24, 67), (234, 172, 161), (87, 89, 18), (137, 214, 226), (67, 47, 20), (27, 90, 57), (23, 62, 39),
          (115, 44, 32), (198, 218, 19), (18, 83, 97)]
i = -2
for turtle in t.keys():
    turtle.penup()
    turtle.setpos(-300, 50 * i)
    turtle.color(random.choice(colors))
    i += 1

play = True
while play:
    rule = True
    winner = None
    guess = screen.textinput("Place your bet!", "Who will win(alex,benji,chris,dan,ellie)?")
    while rule:
        for turtle in t.keys():
            turtle.forward(random.randint(1, 10))
            pos = turtle.pos()
            if pos[0] >= 280:
                rule = False
                winner = turtle
                break

    if t[winner] == guess:
        print("YOU WON")
    else:
        print(f"YOU LOST, The Winner is {t[winner]}")

    i = -2
    for turtle1 in screen.turtles():
        turtle1.setpos(-300, 50 * i)
        i += 1
    choice = screen.textinput('Want to play again?', 'Yes/No')
    if choice.lower() == 'no':
        play = False

screen.exitonclick()
