from turtle import Turtle,Screen,onkey
tim=Turtle()
screen=Screen()
def movefd():
    tim.forward(5)
def movebd():
    tim.backward(5)
def clock():
    tim.right(5)
def aclock():
    tim.left(5)
def clear():
    tim.reset()
screen.onkey(key="w",fun=movefd)
screen.listen()
screen.onkey(key="s",fun=movebd)
screen.listen()
screen.onkey(key="a",fun=aclock)
screen.listen()
screen.onkey(key="d",fun=clock)
screen.listen()
screen.onkey(key="c",fun=clear)
screen.listen()
screen.exitonclick()