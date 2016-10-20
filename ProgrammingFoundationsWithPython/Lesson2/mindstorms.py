import turtle
def draw_square():
    
    brad = turtle.Turtle()
    brad.shape("triangle")
    brad.shapesize(5, 3, 11)
    brad.pensize(10)
    brad.color("magenta")
    for x in range(4):
        brad.forward(100)
        brad.right(90)

def draw_circle():
    
    angie = turtle.Turtle()
    angie.shape("classic")
    angie.shapesize(5, 3, 11)
    angie.pensize(10)
    angie.circle(100)

def draw_triangle():
    
    jenny = turtle.Turtle()
    jenny.shape("turtle")
    jenny.color("green")
    jenny.shapesize(5, 3, 11)
    jenny.right(180)
    jenny.pensize(15)
    jenny.forward(100)
    jenny.right(90)
    jenny.forward(100)
    jenny.right(135)
    jenny.forward(141.42)

    

window = turtle.Screen()
window.bgcolor("blue")
draw_square()
draw_circle()
draw_triangle()

window.exitonclick()
