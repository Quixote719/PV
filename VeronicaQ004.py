import turtle

p = turtle

for i in range(4):
    for i in range(4):
        p.forward(80)
        p.dot(5)
    p.goto(0, 0)
    p.left(90)

p.dot(5)
p.hideturtle()
turtle.done()