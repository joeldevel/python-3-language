from turtle import *

shape('turtle')

def square(sidelength):
    for i in range(4):
        forward(sidelength)
        left(90)

def circleOfSquares():
    for i in range(60):
        square(100)
        left(30)

def triangle(sidelength = 100):
    for i in range(3):
        forward(sidelength)
        left(120)


def polygon(sides):
    for i in range(sides):
        forward(100)
        left(180 - 180/sides)
#circleOfSquares()

#triangle(200)

# works with 3 but not with 4
polygon(3)
