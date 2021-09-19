import turtle
def my_turtle():
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.foward(100)
    turtle.left(90)
    turtle.home()
    turtle.circle(25)
def turtle_state():
    print(turtle.isdown())
    print(turtle.heading())
    print(turtle.xcor(),turtle.ycor())
def main():
    turtle_state()
    my_turtle()
    input("Press ENTER Key to Continue..")
    my_turtle()
main()