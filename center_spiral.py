import turtle

side = 20 # Change here
expand = 7 # Change here
angle = 92 # Change here

myPen = turtle.Turtle()
myPen.speed(0)
myPen.color("#FF0000")

myPen.penup()
myPen.goto(0,0)
myPen.pendown()

for i in range (1,50):
  myPen.forward(side)
  myPen.left(angle)
  side=side+expand

turtle.done()