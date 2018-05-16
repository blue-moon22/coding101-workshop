import turtle

# Parameters
side = 400 # Change here
gap = 5 # Change here

myPen = turtle.Turtle()
myPen.speed(0)
myPen.color("#FF0000")

myPen.penup()
myPen.goto(-side/2,-side/2) # position cursor at the bootom right of the screen
myPen.pendown()

# Start Spiral
iterations = int(round(abs(side) / abs(gap)))
for i in range (1,iterations):
   myPen.forward(side)
   myPen.left(90)
   side=side-gap

turtle.done()