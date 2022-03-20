from turtle import Turtle

STARTING_POSITIONS = [(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def add_segment(self, position):
        new_segment = Turtle(shape='square')
        new_segment.color('green')
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def extend(self):
        self.add_segment(self.segments[-1].position()) #positions() (method from Turtle) indicates the position of the segment[-1]

    def reset(self):
        for segment in self.segments:
            segment.goto(1000,1000) #make old snake disappear in location off the screen
        self.segments.clear() #delete all elements from segmentslist
        self.create_snake()
        self.head = self.segments[0]

    def move(self):
        for segment_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[segment_num -1].xcor() #move a segment in the position od previous segment 
            new_y = self.segments[segment_num -1].ycor() #move segment 2 in position of segment 1, and segment 1 in position of segment 0
            self.segments[segment_num].goto(new_x,new_y)
        self.segments[0].forward(MOVE_DISTANCE) #move only segment 0
            
    def up(self):
        if self.head.heading() != DOWN: # Turtle should not torate by 180 degrees
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

