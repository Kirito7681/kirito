# Space Invaders 
# Set up the screen
import turtle
import os

# set up the creen
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Space Invaders")
# Draw border
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-300, -300)
border_pen.pendown()
border_pen.pensize(3)
for side in range(4):
    border_pen.fd(600)
    border_pen.lt(90)
border_pen.hideturtle()
#Create the player turtle
player = turtle.Turtle()
player.color("blue")
player.shape("triangle")
player.penup()
player.speed(0)
player.setposition(0, -250)
player.setheading(90)
playerspeed = 15
#Move the player left and right
def move_left():
    x = player.xcor()
    x -= playerspeed
    if x < -280:
        x = -280
    player.setx(x)
def move_right():
    x = player.xcor()
    x += playerspeed
    if x > 280:
        x = 280
    player.setx(x)
def fire_bullet():
    #Declare bulletstate as a global if it need changed
    global bulletstate
    if bulletstate == "ready":
        bulletstate = "fire"
        #Move the bullet to the just above the player
        x = player.xcor()
        y = player.ycor()
        bullet.setposition(x, y + 10)
        bullet.showturtle()
def isCollision(t1, t2):
    distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
    
#Create the enemy
enemy = turtle.Turtle()
enemy.color("red")
enemy.shape("circle")
enemy.penup()
enemy.speed(0)
enemy.setposition(-200, 250)
enemyspeed = 2
#Create the player's bullet
bullet = turtle.Turtle()
bullet.color("yellow")
bullet.shape("triangle")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5, 0.5)
bullet.hideturtle()
bulletspeed = 20
#Define bullet state
#ready - ready to fire
#fire - bullet is firing
bulletstate = "ready"
#Create keyboard bindings
turtle.listen()
turtle.onkey(move_left, "Left")
turtle.onkey(move_right, "Right")
turtle.onkey(fire_bullet, "space")

#Main game
while True:
    #Move the enemy
    x = enemy.xcor()
    x += enemyspeed
    enemy.setx(x)
    #Move the enemy back and down
    if enemy.xcor() > 280:
        y = enemy.ycor()
        y -= 40
        enemyspeed *= -1
        enemy.sety(y)

    if enemy.xcor() < -280:
        y = enemy.ycor()
        y -= 40
        enemyspeed *= -1
        enemy.sety(y)
    #Move the bullet
    if bulletstate == "fire":
        y = bullet.ycor()
        y += bulletspeed
        bullet.sety(y)
    #Check to see if the bullet has reached the top
    if bullet.ycor() > 275:
        bullet.hideturtle()
        bulletstate = "ready"
    #Check for a collision between the bullet and the enemy
    if isCollison(bullet, enemy):
        #Reset the bullet
        bullet.hideturtle()
        bullet.setposition(0, - 400)
        #Reset the enemy
        enemy.setposiont(-200, 250) 



