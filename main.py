# Drawing some Dots
# Author >>> Yago Goltara
import turtle as t          # Import turtle module as "t"
from random import choice   # Import choice method from random module


def line(space_between_dots):                   # Method that draws a line with 10 dots
    for i in range(10):
        painter.color(choice(color_list))       # Choose a color from the color_list list
        painter.forward(1)
        painter.penup()
        painter.forward(space_between_dots)     # Space_between_dots represents literally what it says :p
        painter.pendown()


def get_painter_in_right_place():               # Put the painter in the right place (in left down corner the screen)
    painter.penup()
    painter.right(180)
    painter.forward(280)
    painter.left(90)
    painter.forward(270)
    painter.left(90)
    painter.pendown()


def climb_the_line():                           # Climb one line a time and return to
    painter.penup()                             # the right point to continue the other
    painter.left(90)                            # lines
    painter.forward(60)
    painter.left(90)
    painter.forward(610)
    painter.left(180)
    painter.pendown()


t.colormode(255)                        # Activate the rgb color mode
screen = t.Screen()
screen.setup(width=600, height=600)     # Set the screen size
screen.bgcolor(255, 255, 230)           # Set the screen background color

# The list below contains 27 colors
# that I extract from the image in the bin
color_list = [(232, 251, 242), (198, 12, 32), (250, 237, 17), (39, 76, 189), (38, 217, 68),
              (238, 227, 5), (229, 159, 46), (27, 40, 157), (215, 74, 12), (15, 154, 16), (199, 14, 10),
              (243, 33, 165), (229, 17, 121), (73, 9, 31), (60, 14, 8), (224, 141, 211),
              (10, 97, 61), (221, 160, 9), (17, 18, 43), (46, 214, 232), (11, 227, 239), (81, 73, 214), (238, 156, 220),
              (74, 213, 167), (77, 234, 202), (52, 234, 243), (3, 67, 40)]

painter = t.Turtle()
painter.width(18)       # Set the line width
painter.speed(7)        # Set the painter speed
painter.hideturtle()    # Hide the painter pointer

get_painter_in_right_place()
for lines in range(10):         # Draw the 10x10-dot square
    line(60)
    climb_the_line()

screen.exitonclick()
