from turtle import Turtle
import random as rd
START_POS=[(0,0),(-20,0),(-40,0)]
MOVE_DIST=20
UP=90
DOWN=270
LEFT=180
RIGHT=0
class Snake():
    def __init__(self) -> None:
        self.segments=[]
        self.create_snake()
        self.color=(rd.randint(0,255),rd.randint(0,255),rd.randint(0,255))
        
    def create_snake(self):
        for pos in START_POS:
            new_segment=Turtle(shape='square')
            new_segment.color('white')
            new_segment.shapesize(1,1,1)
            new_segment.penup()
            new_segment.goto(pos)   
            self.segments.append(new_segment)
        self.header=self.segments[0]
            
    def move(self):
        for i in range(len(self.segments)-1,0,-1):
            xpos=self.segments[i-1].xcor()
            ypos=self.segments[i-1].ycor()
            self.segments[i].goto(xpos,ypos)   
            self.segments[i-1].forward(MOVE_DIST)       
            
    def up(self):
        if self.header.heading()!=DOWN:
            self.header.setheading(UP)
    
    def down(self):
        if self.header.heading()!=UP:
            self.header.setheading(DOWN)
        
    def left(self):
        if self.header.heading()!=RIGHT:
            self.header.setheading(LEFT)
        
    def right(self):
        if self.header.heading()!=LEFT:
            self.header.setheading(RIGHT)
            
    def xpos(self):
        return self.header.xcor()
    
    def ypos(self):
        return self.header.ycor()
    
    def grow(self):
        new_segment=Turtle(shape='square')
        new_segment.hideturtle()
        new_segment.color((self.color))
        new_segment.shapesize(1,1,1)
        new_segment.penup()
        new_segment.speed('fastest')
        new_segment.goto(self.segments[-1].position())
        new_segment.showturtle()
        self.segments.append(new_segment)
    
    def border(self):
        if self.xpos()>300 or self.xpos()<-300 or self.ypos()>300 or self.ypos()<-300:
            return True
    
    def tail(self):
        for seg in self.segments[1:len(self.segments)]:
            if seg.distance(self.header)<5:
                return True
    
    
                