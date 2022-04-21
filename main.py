from turtle import Turtle, Screen
import random
import time

screen = Screen()
screen.setup(width=600, height=600, startx=0, starty=0)
screen.bgcolor("white")
screen.tracer(0)

colors = ["red", "black", "pink", "green", "blue", "yellow", "orange", "turquoise", "grey"]
positions = []
for i in range(-250, 270, 40):
    positions.append(i)

turtle: Turtle = Turtle("turtle")
turtle.penup()
turtle.setheading(90)

turtle.speed("fastest")
turtle.goto(0, -280)


def move():
    y = turtle.ycor() + 10
    turtle.goto(turtle.xcor(), y)


screen.listen()
screen.onkey(move, "w")

cars = []
score = 0
speed = 10
playing = True
while playing:
    screen.update()
    time.sleep(0.1)
    random_chance = random.randint(1, 100)
    if random_chance == 1:
        car = Turtle("square")
        car.penup()
        car.goto(280, random.randint(-260, 280))
        color = random.choice(colors)
        car.color(color)
        cars.append(car)
        for i in range(len(cars)):
            cars[i].backward(speed)
    for car in cars:
        if car.distance(turtle) < 20:
            print("lost")
            playing = False
    if turtle.ycor() > 290:
        score += 1
        print(f"your score is  {score}")
        turtle.goto(0, -290)
        speed += 10


screen.exitonclick()
