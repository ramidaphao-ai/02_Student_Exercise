import turtle
import math
import time
from polygon_shape import Polygon

screen = turtle.Screen()
screen.title("Animated Polygon Art")
screen.tracer(0)

polygon_data = [
    ("khaki", -200, 100, 5, 100),
    ("tan", 50, -280, 8, 100),
    ("cornsilk", -200, -280, 6, 100),
    ("#8c564b", -100, -100, 4, 100),
    ("#c49391", 200, 100, 7, 100),
    ("#7D683C", -300, 0, 3, 100),
    ("#b2996e", 280, -250, 7, 100),
    ("#CAB0B8", 0, 250, 5, 100),
    ("#FFF5EE", -265, 190, 6, 100)
]

polygons = []

for color, x, y, sides, length in polygon_data:
    polygon = Polygon(color, x, y, sides, length)
    polygon.speed(0)
    polygons.append(polygon)

circle_data = [
    ("olive", 60, 80, 50),
    ("#C9DBC1", 280, 0, 50),
    ("#BDB76B", 265, 190, 25),
    ("#A9A9A9", -300, -300, 120)
]

circles = []

for color, x, y, radius in circle_data:
    circle = turtle.Turtle()
    circle.shape("turtle")
    circle.pencolor(color)
    circle.pensize(100)
    circle.speed(0)
    circle.penup()
    circle.goto(x, y)
    circle.pendown()
    circles.append((circle, x, y, radius))

artist_cat = turtle.Turtle()
artist_cat.shape("turtle")
artist_cat.pencolor("#3A2311")
artist_cat.pensize(5)
artist_cat.speed(0)
artist_cat.hideturtle()


def draw_cat(x, y):
    artist_cat.clear()

    artist_cat.penup()
    artist_cat.goto(x, y - 100)
    artist_cat.pendown()
    artist_cat.fillcolor("#FFF0C9")
    artist_cat.begin_fill()
    artist_cat.circle(120)
    artist_cat.end_fill()

    artist_cat.penup()
    artist_cat.goto(x - 100, y + 80)
    artist_cat.pendown()
    artist_cat.begin_fill()
    artist_cat.goto(x - 130, y + 180)
    artist_cat.goto(x - 30, y + 130)
    artist_cat.goto(x - 100, y + 80)
    artist_cat.end_fill()

    artist_cat.penup()
    artist_cat.goto(x + 100, y + 80)
    artist_cat.pendown()
    artist_cat.begin_fill()
    artist_cat.goto(x + 130, y + 180)
    artist_cat.goto(x + 30, y + 130)
    artist_cat.goto(x + 100, y + 80)
    artist_cat.end_fill()

    artist_cat.penup()
    artist_cat.goto(x - 45, y + 30)
    artist_cat.pendown()
    artist_cat.dot(15, "#795548")

    artist_cat.penup()
    artist_cat.goto(x + 45, y + 30)
    artist_cat.pendown()
    artist_cat.dot(15, "#795548")

    artist_cat.penup()
    artist_cat.goto(x, y - 5)
    artist_cat.pendown()
    artist_cat.dot(15, "#F28BA8")

    artist_cat.penup()
    artist_cat.goto(x, y - 15)
    artist_cat.pendown()
    artist_cat.goto(x, y - 35)
    artist_cat.goto(x - 20, y - 50)

    artist_cat.penup()
    artist_cat.goto(x, y - 35)
    artist_cat.pendown()
    artist_cat.goto(x + 20, y - 50)

    artist_cat.penup()
    artist_cat.goto(x - 35, y - 20)
    artist_cat.pendown()
    artist_cat.goto(x - 100, y - 10)

    artist_cat.penup()
    artist_cat.goto(x - 35, y - 35)
    artist_cat.pendown()
    artist_cat.goto(x - 100, y - 45)

    artist_cat.penup()
    artist_cat.goto(x + 35, y - 20)
    artist_cat.pendown()
    artist_cat.goto(x + 100, y - 10)

    artist_cat.penup()
    artist_cat.goto(x + 35, y - 35)
    artist_cat.pendown()
    artist_cat.goto(x + 100, y - 45)

    artist_cat.hideturtle()


frame = 0

while True:
    x = 25 * math.sin(frame / 15)
    y = 20 * math.cos(frame / 15)

    for polygon, data in zip(polygons, polygon_data):
        color, start_x, start_y, sides, length = data
        polygon.clear()
        polygon.penup()
        polygon.goto(start_x + x, start_y + y)
        polygon.pendown()
        polygon.draw()

    for circle, start_x, start_y, radius in circles:
        circle.clear()
        circle.penup()
        circle.goto(start_x + x, start_y + y)
        circle.pendown()
        circle.circle(radius)

    draw_cat(x, y)

    screen.update()
    time.sleep(0.03)
    frame += 1

screen.mainloop()
