from turtle import Turtle
ALLIGMENT = 'center'
FONT = ('Verdana', 14, 'normal')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('white')
        self.penup()
        self.goto(0,280)
        self.hideturtle() # to hide turtle that was in the center of scoreboard
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f'Score: {self.score}', align=ALLIGMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear() #delete previous scoreboard
        self.update_scoreboard()

    def game_over(self):
        self.goto(0,0)
        self.write('GAME OVER', align=ALLIGMENT, font=FONT)
        

    