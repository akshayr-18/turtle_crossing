from turtle import Turtle
class Scoreboard(Turtle):
	def __init__(self):
		super().__init__()
		self.color("white")
		self.penup()
		self.hideturtle()
		self.level=0
		self.goto(0,280)
		self.updatescoreboard()
		
	def updatescoreboard(self):
		self.write(f"LEVEL : {self.level}",align="center",font=("Courier",10,"normal"))
	
	def inc_score(self):
		self.level+=1
		self.clear()
		self.updatescoreboard()
	
	def gameover(self):
		self.goto(0,0)
		self.color("teal")
		self.write(f"GAME OVER.",align="center",font=("Courier",50,"normal"))
