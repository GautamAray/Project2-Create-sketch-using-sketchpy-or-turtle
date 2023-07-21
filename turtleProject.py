import turtle
turtle.bgcolor("black")
turtle.pencolor("yellow")
turtle.color("yellow","green")
turtle.pensize(10)
mycolor = ["red","blue","yellow","green"]
k = 0
j = 200
for i in range(20):
    turtle.pencolor(mycolor[k])
    k += 1
    if k == 4:
        k = 0
    turtle.forward(j)
    j -= 10
    turtle.left(90)
turtle.done()
