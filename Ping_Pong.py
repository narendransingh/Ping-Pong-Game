import turtle

wn = turtle.Screen()
wn.bgcolor('black')
wn.setup(width=1000, height=800) #play screen of 800 by 600
wn.tracer(0)


border = turtle.Turtle()
border.color('white')
#border.speed(0)
border.penup()
border.goto(400,0)
border.pensize(2)
border.hideturtle()
border.pendown()
border.left(90)
border.forward(300)
border.left(90)
border.forward(800)
border.left(90)
border.forward(600)
border.left(90)
border.forward(800)
border.left(90)
border.forward(300)


#Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0) #speed of animation, need to be Turtle to max speed.
paddle_a.shape("square") #create shape of 20 px by 20 px
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1) #width will be 5*20 =100
paddle_a.penup()
paddle_a.goto(-350, 0) #to left from center (0,0)

#Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0) #speed of animation, need to be Turtle to max speed.
paddle_b.shape("square") #create shape of 20 px by 20 px
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1) #width will be 5*20 =100
paddle_b.penup()
paddle_b.goto(350, 0) #to left from center (0,0)

#Ball
ball = turtle.Turtle()
ball.speed(0) #speed of animation, need to be Turtle to max speed.
ball.shape("square") #create shape of 20 px by 20 px
ball.color("white")
ball.penup()
ball.goto(0, 0) #to left from center (0,0)
ball.dx = 2
ball.dy = 2

score_a = 0
score_b = 0

#Create score board
pen = turtle.Turtle()
pen.speed(0)
pen.color('white')
pen.penup()
pen.hideturtle() #dont want to see the turtle
pen.goto(0, 350)
pen.write('Player A: 0   Player B: 0', align='center', font=('Courier', 20, 'normal'))

#Function
#move paddle_a up
def paddle_a_up():
    y = paddle_a.ycor() #ycor is func. in turtle to get y corrdinate
    y += 20 #add 20 px.
    paddle_a.sety(y) #sety is func of turtle, we change y to new corodinate

#move paddle_a down
def paddle_a_down():
    y = paddle_a.ycor() #ycor is func. in turtle to get y corrdinate
    y -= 20 #add 20 px.
    paddle_a.sety(y) #sety is func of turtle, we change y to new corodinate

#move paddle_a up
def paddle_b_up():
    y = paddle_b.ycor() #ycor is func. in turtle to get y corrdinate
    y += 20 #add 20 px.
    paddle_b.sety(y) #sety is func of turtle, we change y to new corodinate

#move paddle_a down
def paddle_b_down():
    y = paddle_b.ycor() #ycor is func. in turtle to get y corrdinate
    y -= 20 #add 20 px.
    paddle_b.sety(y) #sety is func of turtle, we change y to new corodinate

#Keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up, "q")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

#Main game loop
while True:
    wn.update()

    #move the ball
    ball_x = ball.xcor() #get the ball x corrdinate
    ball.setx(ball_x + ball.dx) #set the new value of ball with the change
    ball_y = ball.ycor()
    ball.sety(ball_y + ball.dy)

    #Border Checking: Compare the ball y corrdinate afer 300 px it need to bounce also ball is 20 px
    if ball_y > 290:
        ball.sety(290)
        ball.dy *= -1 #this will reverse the direction of ball

    if ball_y < -280:
        ball.sety(-280)
        ball.dy *= -1 #this will reverse the direction of ball

    #for ball going out at x
    if ball_x > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write('Player A: {}   Player B: {}'.format(score_a, score_b), align='center', font=('Courier', 20, 'normal'))


    if ball_x < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write('Player A: {}   Player B: {}'.format(score_a, score_b), align='center', font=('Courier', 20, 'normal'))

        if score_a > 2 and score_b > 2:
            ball.dx = 2.5
            ball.dy = 2.5

        if score_a > 5 and score_b > 5:
            paddle_a.shapesize(stretch_wid=4, stretch_len=1)
            paddle_b.shapesize(stretch_wid=4, stretch_len=1)

            if (ball_x > 340 and ball_x < 350) and (ball_y < paddle_b.ycor() + 40 and ball_y > paddle_b.ycor() - 40):
                ball.setx(330)
                ball.dx *= -1

            elif (ball_x < -340 and ball_x > -350) and (ball_y < paddle_a.ycor() + 40 and ball_y > paddle_a.ycor() - 40):
                ball.setx(-330)
                ball.dx *= -1

        if score_a > 8 and score_b > 8:
            ball.dx = 2.9
            ball.dy = 2.9

        if score_a > 10 and score_b > 10:
            paddle_a.shapesize(stretch_wid=3, stretch_len=1)
            paddle_b.shapesize(stretch_wid=3, stretch_len=1)

            if (ball_x > 340 and ball_x < 350) and (ball_y < paddle_b.ycor() + 30 and ball_y > paddle_b.ycor() - 30):
                ball.setx(330)
                ball.dx *= -1

            elif (ball_x < -340 and ball_x > -350) and (ball_y < paddle_a.ycor() + 30 and ball_y > paddle_a.ycor() - 30):
                ball.setx(-330)
                ball.dx *= -1

        if score_a > 12 and score_b > 12:
            ball.dx = 3.4
            ball.dy = 3.4


    #Paddle and ball connect
    if (ball_x > 340 and ball_x < 350) and (ball_y < paddle_b.ycor()+50 and ball_y > paddle_b.ycor()-50):
        ball.setx(330)
        ball.dx *= -1

    elif (ball_x < -340 and ball_x > -350) and (ball_y < paddle_a.ycor()+50 and ball_y > paddle_a.ycor()-50):
        ball.setx(-330)
        ball.dx *= -1


#turtle.exitonclick()
#turtle.update()
turtle.done()