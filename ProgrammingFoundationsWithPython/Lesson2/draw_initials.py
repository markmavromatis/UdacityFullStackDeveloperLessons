import turtle
def draw_m(some_turtle):

    some_turtle.forward(100)
    some_turtle.right(135)
    some_turtle.forward(50)
    some_turtle.left(90)
    some_turtle.forward(50)
    some_turtle.right(135)
    some_turtle.forward(100)
    some_turtle.right(180)

def draw_space(some_turtle):
    some_turtle.right(90)
    some_turtle.forward(50)
    some_turtle.left(90)
    
def draw_a(some_turtle):
    print "placeholder"

def draw_r(some_turtle):
    print "placeholder"

def draw_k(some_turtle):
    print "placeholder"
    

mark = turtle.Turtle()
mark.shape("turtle")
# mark.shapesize(5, 3, 11)
mark.pensize(5)
mark.color("red")
mark.left(90)
window = turtle.Screen()
window.bgcolor("blue")
draw_m(mark)
mark.penup()
draw_space(mark)
mark.pendown()
draw_m(mark)

window.exitonclick()
