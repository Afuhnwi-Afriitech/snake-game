from turtle import Turtle
import time
starting_position = [(0, 0), (-20, 0), (-40, 0)]
all_tinos = []


class Snake:
    def __init__(self):
        self.create_snake()
        self.head = all_tinos[0]


    def create_snake(self):
        # add each tino to tinos
        for position in starting_position:
            self.add_segment(position)

    def add_segment(self, position):
        tino = Turtle()
        tino.color('white')
        tino.shape('square')
        tino.penup()
        tino.goto(position)
        all_tinos.append(tino)

    def extent_segment(self):
        self.add_segment(all_tinos[-1].position())


    def move(self):
        # moving the snake
        for tino in range(len(all_tinos) - 1, 0, -1):
            x_coordinate = all_tinos[tino - 1].xcor()
            y_coordinate = all_tinos[tino - 1].ycor()
            all_tinos[tino].goto(x_coordinate, y_coordinate)
        all_tinos[0].forward(20)
        time.sleep(0.05)


    def up(self):
        if all_tinos[0].heading() != 270:
            all_tinos[0].setheading(90)

    def down(self):
        if all_tinos[0].heading() != 90:
            all_tinos[0].setheading(270)

    def left(self):
        if all_tinos[0].heading() != 0:
            all_tinos[0].setheading(180)

    def right(self):
        if all_tinos[0].heading() != 180:
            all_tinos[0].setheading(0)

