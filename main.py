from turtle import Screen
import time
from snake import Snake
from food import Food
from score_board import ScoreBoard

# Initializing canvas
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

# Creating objects
snake1 = Snake(snake_len=5)
food = Food()
score = ScoreBoard()


# Screen commands, listen for key strokes
screen.listen()
screen.onkey(snake1.up, "Up")
screen.onkey(snake1.down, "Down")
screen.onkey(snake1.left, "Left")
screen.onkey(snake1.right, "Right")

# Main program starts
game_on = True

while game_on:
    screen.update()
    time.sleep(0.1)
    score.show_score()
    snake1.move()

    # Detect collision with food
    if snake1.head.distance(food) < 25:
        food.refresh()
        snake1.add_segment()
        score.add_score()

    # Detect collision with wall
    if abs(snake1.head.xcor()) > 290 or abs(snake1.head.ycor()) > 290:
        game_on = False
        score.game_over()

    # Detect collision with itself
    for segment in snake1.segments[1:]:
        if snake1.head.distance(segment) < 10:
            game_on = False
            score.game_over()

screen.exitonclick()


# # Slicing and how the position works
# key = ["a", "b", "c", "d", "e", "f", "g"]
#
#
# # print (key[start_position : end_position : step_size])
# print(key[2:5])
# print(key[ :5])
# print(key[2: ])
# print(key[2:5:2])
# print(key[::-1])
