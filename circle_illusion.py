import turtle 

gap = 4 # Change here
length1 = 100 # Change here
angle1 = 30 # Change here
length2 = 20 # Change here
angle2 = 60 # Change here
length3 = 50 # Change here
angle3 = 30 # Change here

myPen = turtle.Turtle()
myPen.speed(0)

iterations = int(round(360 / gap))
for i in range(iterations):
    myPen.forward(length1)
    myPen.right(angle1)
    myPen.forward(length2)
    myPen.left(angle2)
    myPen.forward(length3)
    myPen.right(angle3)
    
    myPen.penup()
    myPen.setposition(0, 0)
    myPen.pendown()
    
    myPen.right(gap)
    
turtle.done()