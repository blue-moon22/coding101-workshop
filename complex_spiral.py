import turtle

myPen = turtle.Turtle()
myPen.speed(0) 
myPen.pensize(2)

myPen.color("purple")
for i in range(36):
    for j in range(4):
        myPen.forward(200)
        myPen.right(90)
    myPen.right(10)

myPen.color("blue")
size = 1
for i in range(300):
    myPen.forward(size)
    myPen.right(91)
    size += 1

turtle.done()