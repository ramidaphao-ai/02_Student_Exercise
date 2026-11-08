
"""Drawing a Cat Face."""
import turtle

screen = turtle.Screen()
screen.title("Drawing a Cat Face")
screen.bgcolor("white")


"""Example 2: Repetition and methods of a Turtle object."""
import turtle
from polygon_shape import Polygon

screen = turtle.Screen()
screen.title("Example 2 - Drawing a Square")

artist = Polygon("khaki", -200, 100, 5, 100)
artist2 = turtle.Turtle()
artist2.shape("turtle")
artist2.pencolor("olive")
artist2.pensize(100)
artist2.penup()
artist2.goto(60, 80)
artist2.pendown()

artist3 = Polygon("tan", 50, -280, 8, 100)
artist4 = Polygon("cornsilk", -200, -280, 6, 100)
artist5 = Polygon("#8c564b", -100, -100, 4, 100)
artist6 = Polygon("#c49391", 200, 100, 7, 100)
artist7 = Polygon("#7D683C", -300, 0, 3, 100)

artist8 = turtle.Turtle()
artist8.shape("turtle")
artist8.pencolor("#C9DBC1")
artist8.pensize(100)
artist8.penup()
artist8.goto(280, 0)
artist8.pendown()

artist_cat = turtle.Turtle()
artist_cat.shape("turtle")
artist_cat.pencolor("#3A2311")
artist_cat.pensize(5)
artist_cat.speed(0)
artist_cat.penup()
artist_cat.goto(0, -100)
artist_cat.pendown()
artist_cat.fillcolor("#FFF0C9")
artist_cat.begin_fill()
artist_cat.circle(120)
artist_cat.end_fill()

artist_cat.penup()
artist_cat.goto(-100, 80)
artist_cat.pendown()
artist_cat.fillcolor("#FFF0C9")
artist_cat.begin_fill()
artist_cat.goto(-130, 180)
artist_cat.goto(-30, 130)
artist_cat.goto(-100, 80)
artist_cat.end_fill()

artist_cat.penup()
artist_cat.goto(100, 80)
artist_cat.pendown()
artist_cat.begin_fill()
artist_cat.goto(130, 180)
artist_cat.goto(30, 130)
artist_cat.goto(100, 80)
artist_cat.end_fill()

artist_cat.penup()
artist_cat.goto(-45, 30)
artist_cat.pendown()
artist_cat.dot(15, "#795548")

artist_cat.penup()
artist_cat.goto(45, 30)
artist_cat.pendown()
artist_cat.dot(15, "#795548")

artist_cat.penup()
artist_cat.goto(0, -5)
artist_cat.pendown()
artist_cat.dot(15, "#F28BA8")

artist_cat.penup()
artist_cat.goto(0, -15)
artist_cat.pendown()
artist_cat.goto(0, -35)
artist_cat.goto(-20, -50)

artist_cat.penup()
artist_cat.goto(0, -35)
artist_cat.pendown()
artist_cat.goto(20, -50)

artist_cat.penup()
artist_cat.goto(-35, -20)
artist_cat.pendown()
artist_cat.goto(-100, -10)

artist_cat.penup()
artist_cat.goto(-35, -35)
artist_cat.pendown()
artist_cat.goto(-100, -45)

artist_cat.penup()
artist_cat.goto(35, -20)
artist_cat.pendown()
artist_cat.goto(100, -10)

artist_cat.penup()
artist_cat.goto(35, -35)
artist_cat.pendown()
artist_cat.goto(100, -45)
artist_cat.hideturtle()

artist9 = Polygon("#b2996e", 280, -250, 7, 100)

artist10 = Polygon("#CAB0B8", 0, 250, 5, 100)

artist11 = turtle.Turtle()
artist11.shape("turtle")
artist11.pencolor("#BDB76B")
artist11.pensize(100)
artist11.penup()
artist11.goto(265, 190)
artist11.pendown()

artist12 = Polygon("#FFF5EE", -265, 190, 6, 100)

artist13 = turtle.Turtle()
artist13.shape("turtle")
artist13.pencolor("#A9A9A9")
artist13.pensize(100)
artist13.penup()
artist13.goto(-300, -300)
artist13.pendown()

artist.draw()
artist2.circle(50)
artist3.draw()
artist4.draw()
artist5.draw()
artist6.draw()
artist7.draw()
artist8.circle(50)
artist9.draw()
artist10.draw()
artist11.circle(25)
artist12.draw()
artist13.circle(120)

screen.mainloop()
