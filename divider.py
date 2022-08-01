from turtle import Turtle
class Divider(Turtle):
	def __init__(self,cord):
		super().__init__()
		self.shape("square")
		self.penup()
		self.shapesize(stretch_wid=0.5,stretch_len=200)
		self.color("white")
		self.goto(cord)
