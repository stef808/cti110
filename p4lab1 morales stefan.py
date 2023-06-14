# turtle graphics
# cti 110
# P4LAB1-morales stefan
# 06/14/2023

# initialize
import turtle
win = turtle.Screen()

# make your turtle
t = turtle.Turtle()
t.shape("turtle")

# Draw a square
i = 0
while i < 4:
    t.forward(100)
    t.right(90)
    i += 1

# Move the turtle to a suitable position for triangle
t.penup()
t.right(135)
t.forward(70)
t.pendown()
t.left(135)

# Draw a triangle
i = 0
while i < 3:
    t.forward(100)
    t.right(120)
    i += 1

# at the end, keep the window open until closed
win.mainloop()
