def hearts(color,ang1,front,x,y,ang2):
    t.up()
    t.goto(0,-50)
    t.down()
    t.begin_fill()
    t.fillcolor(color)
    t.left(ang1)
    t.forward(front)
    t.circle(x,y)
    t.left(ang2)
    t.circle(x,y)
    t.forward(front)
    t.end_fill()
    
    
    


import turtle
t = turtle.Turtle()
turtle.title("Hearts")
screen = turtle.Screen()
screen.bgcolor("black")
t.color("white")

t.speed(6)
#hearts("red",140,180,-90,200,120)
hearts("yellow",120,160,-80,180,90)
hearts("pink",120,160,-80,180,90)
hearts("red",120,160,-80,180,90)
hearts("blue",120,160,-80,180,90)
hearts("violet",120,160,-80,180,90)
hearts("purple",120,160,-80,180,90)
hearts("green",120,160,-80,180,90)

hearts("brown",120,120,-60,180,90)
hearts("red",120,120,-60,180,90)
hearts("blue",120,120,-60,180,90)
hearts("green",120,120,-60,180,90)
hearts("yellow",120,120,-60,180,90)

#t.right(40)
t.up()
t.goto(0,-13)
t.begin_fill()
t.circle(-40)
t.fillcolor("black")
t.end_fill()
t.goto(0,-32)
t.begin_fill()
t.circle(-20)
t.fillcolor("grey")
t.down()
t.end_fill()
t.hideturtle()

#hearts("blue",160,220,-110,180,90)
#hearts("pink",160,220,-110,180,90)
