from turtle import Turtle
from random import randint
class Cars(Turtle):
	def __init__(self,start,level):
		super().__init__()
		self.shape("square")
		self.color(randint(0,255),randint(0,255),randint(0,255))
		self.penup()
		self.shapesize(stretch_wid=2,stretch_len=4)
		self.goto(350,start)
		self.start=start
		self.level=level
	
	def move(self):
		self.goto(self.xcor()-3*self.level,self.start)
	
	
