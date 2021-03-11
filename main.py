from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)
snake = Snake()
food = Food()
scoreboard = ScoreBoard()
screen.listen()
screen.onkey(snake.up, "w")
screen.onkey(snake.down, "s")
screen.onkey(snake.right, "d")
screen.onkey(snake.left, "a")
game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #Detect collision  with food:
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.update_score()


    #Detect collision with wall:
    if snake.head.xcor()>280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset()
        snake.reset()


    #Detect collision with tail:
    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()




screen.exitonclick()
