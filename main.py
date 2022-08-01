from turtle import Turtle,Screen
from random import randint,choice
from divider import Divider
import time
from turt import Turt
from cars import Cars
from scoreboard import Scoreboard
s=Screen()
s.tracer(0)
s.colormode(255)
s.listen()
s.bgcolor("black")
s.setup(width=800,height=600)
s.title("TURTLE CROSSING")
t=Turt()
score=Scoreboard()
cs=[]
level=1
d1=Divider((0,-250))
d2=Divider((0,-150))
d3=Divider((0,-50))
d4=Divider((0,50))
d5=Divider((0,150))
d6=Divider((0,250))
game_is_on=True
s.onkey(t.move,"Up")
s.onkey(t.lef,"Left")
s.onkey(t.rig,"Right")
while(game_is_on):
	s.update()
	time.sleep(0.1)
	c=Cars(choice((-200,-100,0,100,200)),level)
	flag=0
	for i in cs:
		if i.distance(c)<=150:
			flag=1
			break;
	if flag==0:
		cs.append(c)
	for i in cs:
		i.move()
	for i in cs:
		if i.distance(t)<=40:
			game_is_on=False
	if t.ycor()>=250:
		level+=1
		t.goto(0,-280)
		score.inc_score()

score.gameover()





s.exitonclick()
