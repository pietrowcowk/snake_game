from turtle import Screen,  Turtle
import time
from scoreboard import Scoreboard
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0) #turning turtle animation off

snake = Snake()
food = Food()
score_board = Scoreboard()

screen.listen() #allows to detect when the user has hit certain keys on the keyboard
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down,'Down')
screen.onkey(snake.right ,'Right')
screen.onkey(snake.left ,'Left')

game_is_on = True
while game_is_on:
    screen.update() #turning turtle animation on, refreshing screen
    time.sleep(0.1) #delay refreshing screen 
    snake.move()

    #Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh_food()
        snake.extend()
        score_board.increase_score()

    #Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score_board.reset()
        snake.reset()

    #Detect collision with tail
    for segment in snake.segments[1:]: # checks all segments except head - segment[0]
        if snake.head.distance(segment) < 10:
            score_board.reset()
            snake.reset()

 
    









screen.exitonclick()