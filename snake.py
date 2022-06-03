from turtle import Turtle,Screen
START_POSITION = (0,0)
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self,snake_len):
        self.snake_len = snake_len
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def add_segment(self):
        self.tail = self.segments[-1] # Find the last segment
        tail_position = self.tail.position()
        new_block = Turtle(shape="square")
        new_block.color("white")
        new_block.penup()
        new_block.setposition(tail_position)
        self.segments.append(new_block)

    def extend(self):
        self.add_segment(self)

    def create_snake(self):
        for i in range(0, self.snake_len):
            new_block = Turtle(shape="square")
            new_block.color("white")
            new_block.penup()
            new_block.setposition(x=START_POSITION[0] - i * 20, y=START_POSITION[1])
            self.segments.append(new_block)

    def move(self):

        # go thru the blocks in reverse order, move block3 into block2 position, etc
        for seg_num in range(len(self.segments)-1, 0, -1):
            self.segments[seg_num].goto(self.segments[seg_num-1].position())

        self.head.forward(20)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
            self.move()

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
            self.move()

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
            self.move()

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
            self.move()