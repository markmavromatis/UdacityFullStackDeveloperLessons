#Copied from here: http://www.algorithm.co.il/blogs/computer-science/fractals-in-10-minutes-no-6-turtle-snowflake/
from turtle import *
 
def f(length, depth):
   if depth == 0:
     forward(length)
   else:
     f(length/3, depth-1)
     right(60)
     f(length/3, depth-1)
     left(120)
     f(length/3, depth-1)
     right(60)
     f(length/3, depth-1)

window = Screen()

window.bgcolor("yellow")
color("blue")


speed(0)
left(30)

for i in range(4):
    f(100, 4)
    left(90)

window.exitonclick()
