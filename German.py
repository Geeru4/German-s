import turtle

mainTurtle = turtle.Turtle()

mainTurtle.pensize(6)
#квадрат
mainTurtle.color("green")
mainTurtle.pendown()
mainTurtle.right(45)
mainTurtle.forward(150)
mainTurtle.left(90)
mainTurtle.forward(150)
mainTurtle.left(90)
mainTurtle.forward(150)
mainTurtle.left(90)
mainTurtle.forward(150)
mainTurtle.penup()
mainTurtle.goto(-350,0)
#треугольник 
mainTurtle.color("red")
mainTurtle.pendown()
mainTurtle.left(120)
mainTurtle.forward(150)
mainTurtle.left(120)
mainTurtle.forward(150)
mainTurtle.left(120)
mainTurtle.forward(150)
mainTurtle.penup()
mainTurtle.goto(-130,-50)
#круг
mainTurtle.color("blue")
mainTurtle.pendown()
mainTurtle.circle(90)

mainTurtle.hideturtle()
turtle.exitonclick()
