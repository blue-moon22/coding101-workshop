import turtle 

side = 200 # Change here
angle = 123 # Change here

myPen = turtle.Turtle()
myPen.speed(0)
myPen.pencolor("red")

myPen.penup()
myPen.goto(0,0)
myPen.pendown()

for i in range(50):
    myPen.forward(side)
    myPen.left(angle)
    
turtle.done()