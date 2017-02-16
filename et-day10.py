import turtle
t = turtle
t=turtle.Turtle()
t.speed(10)

def box():
    t.forward(100)
    t.right(90)
    t.forward(100)
    t.right(90)
    t.forward(100)
    t.right(90)
    t.forward(100)
    t.right(90)

for i in range(18):
    box()
    t.right(360/18)
