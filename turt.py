from turtle import Turtle
class Turt(Turtle):
	def __init__(self):
		super().__init__()
		self.shape("turtle")
		self.left(90)
		self.color("brown","green")
		self.penup()
		self.goto(0,-280)
		
	def move(self):
		if self.ycor()==-280:
			self.goto(self.xcor(),-200)
		elif self.ycor()==200:
			self.goto(self.xcor(),280)
		else:
			self.goto(self.xcor(),self.ycor()+100)
			
	def lef(self):
		self.goto(self.xcor()-10,self.ycor())
		
	def rig(self):
		self.goto(self.xcor()+10,self.ycor())
