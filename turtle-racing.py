import random
import turtle as t
from turtle import Turtle,Screen
timmy = Turtle()
tommy = Turtle()
becky = Turtle()
steve = Turtle()
rock = Turtle()
screen = Screen()
screen.setup(width=1000,height=1000)
x = screen.textinput(title="TURTLE RACE BETTING ASSOCIATION\n",prompt="Make your bet.\n[ Green, Blue, Red, Orange, Yellow ]\nChoose your color:\n").lower()
turtles = [timmy,tommy,becky,steve,rock]
def turtles_penup():
    for i in turtles:
        i.penup()
turtles_penup()
def turtles_shape():
    for i in turtles:
        i.shape("turtle")
turtles_shape()
def turtles_shapesize():
    for i in turtles:
        i.shapesize(2)
turtles_shape()
def position_them():
    timmy.goto(-500, 100)
    tommy.goto(-500, 50)
    becky.goto(-500, 0)
    steve.goto(-500, -50)
    rock.goto(-500, -100)
position_them()
timmy.color("green")
tommy.color("blue")
becky.color("red")
steve.color("orange")
rock.color("yellow")
winner = list()
def random_forward_movement():
    return random.randint(5,30)
j=0
def race():
    global j
    while(j==0):
        for i in turtles:
            if i.xcor()>=500:
                j=1
                winner.append(i)
            i.forward(random_forward_movement())
race()

if x==winner[-1]:
     print("Congrats You Won!!")
else :
     print("You lost the bet!!")
screen.exitonclick()
