

import turtle

ekran = turtle.Screen()
ekran.bgcolor("black")
ekran.setup(width = 800 , height = 600)
ekran.title("DENEME EKRANI")
ekran.tracer(0)

#cubuk

cubuk = turtle.Turtle()
cubuk.speed(0)
cubuk.shape("square")
cubuk.color("white")
cubuk.shapesize(stretch_wid= 0.5 , stretch_len= 5)
cubuk.penup()
cubuk.goto(0, -220)

#ball

ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("red")
ball.shapesize(stretch_wid=1 , stretch_len= 1)
ball.penup()
ball.goto(0 , 0)
ball.dx = 0.2
ball.dy = 0.2


#function

def cubuk_left():
    if cubuk.xcor() > -350:
        x = cubuk.xcor()
        x -= 30
        cubuk.setx(x)
    

def cubuk_right():
    if cubuk.xcor() < 350:
        x = cubuk.xcor()
        x += 30
        cubuk.setx(x)
       
           

        

    

#binds

ekran.listen()
ekran.onkeypress(cubuk_left, "Left")
ekran.onkeypress(cubuk_right, "Right")




while True:
    ekran.update()

    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)


    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.setx(390)
        ball.dx *= -1


    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() < -390:
        ball.setx(-390)
        ball.dx *= -1


    if ball.ycor() < cubuk.ycor() + 12 and (cubuk.xcor() + 60 > ball.xcor() and ball.xcor() > cubuk.xcor() - 60):
        ball.dy *= -1
    
