from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)  # tracer turn animation on/off; 0 means off

snake = Snake()
food = Food()
score = ScoreBoard()
screen.listen()

screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.left, key="Left")
screen.onkey(fun=snake.right, key="Right")
game_on = True

while game_on:
    screen.update()  # updates the screen; used when tracer is off to start animation
    time.sleep(0.1)  # used to add delay in execution
    snake.move()

    # collision with food
    if snake.snake_head.distance(food) < 15:
        snake.update_snake()
        food.refresh()
        score.update_score()

    # collision with wall
    if (snake.snake_head.xcor() > 280 or snake.snake_head.xcor() < -280 or snake.snake_head.ycor() > 280 or
            snake.snake_head.ycor() < -280):
        game_on = False
        score.game_over()

    # detect self collision
    for seg in snake.snake_segments:
        if snake.snake_head == seg:
            pass
        elif snake.snake_head.distance(seg) < 10:
            game_on = False
            score.game_over()

screen.exitonclick()
