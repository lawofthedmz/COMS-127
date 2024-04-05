# Murphy Glawe          9/5/2023

# Lab Week 3 Section 6

# The goal of this code is to draw my initials using turtle fucntions

import turtle
pen_M = turtle.Turtle()
pen_G = turtle.Turtle()
bg = turtle.Screen()
bg.bgcolor("lawngreen")

# 
# Code for the letter "M"
#

pen_M.pencolor("orange")
pen_M.left(180)
pen_M.pensize(15)
pen_M.penup()
pen_M.forward(200)
pen_M.right(90)
pen_M.pendown()
pen_M.forward(150)
pen_M.right(135)
pen_M.forward(100)
pen_M.left(90)
pen_M.forward(100)
pen_M.right(135)
pen_M.forward(150)
pen_M.penup()

#
# Code for the letter "G"
#

pen_G.pencolor("red")
pen_G.pensize(15)
pen_G.penup()
pen_G.forward(100)
pen_G.pendown()
pen_G.circle(75, 90)
pen_G.penup()
pen_G.circle(75, 60)
pen_G.pendown()
pen_G.circle(75, 210)
pen_G.penup()
pen_G.circle(75, 90)
pen_G.left(90)
pen_G.pendown()
pen_G.forward(75)


bg.exitonclick()



