from turtle import Turtle
ALLIGMENT = 'center'
FONT = ('Verdana', 14, 'normal')

#creating file to save highscore
f = open('data.txt', 'w')
f.write('0')
f.close()

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open('data.txt') as data:
            self.high_score = int(data.read())
        self.color('white')
        self.penup()
        self.goto(0,280)
        self.hideturtle() # to hide turtle that was in the center of scoreboard
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear() #delete previous scoreboard
        self.write(f'Score: {self.score} High score: {self.high_score}', align=ALLIGMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open('data.txt', mode='w') as data:
                data.write(f'{self.high_score}')
        self.score = 0
        self.update_scoreboard()
     

    