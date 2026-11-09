"""Animate the same 20 Polygon objects for 90 frames."""
import math
import time
import turtle
from polygon_shape import Polygon

screen = turtle.Screen()
screen.title("Animated Student Polygon Art")
screen.setup(width=1400, height=1040)
screen.bgcolor("black")
screen.tracer(0)

# x, y, sides, side_length, color, pen_size, angle
POLYGON_DATA = [[-392,272,6,66,"#35e6df",3,18],[-212,350,5,62,"#9bd32d",8,0],[38,280,3,112,"#dda0dd",10,12],[-70,110,5,90,"#dda0dd",9,8],[242,30,6,118,"#ffb6c8",7,0],[296,74,6,88,"#ff796e",3,12],[-578,55,4,88,"#ffb6c8",3,45],[-401,-66,4,72,"#9bd32d",10,8],[-249,-78,5,82,"#00e5ed",8,18],[-283,-204,3,94,"#36d6c8",8,12],[-145,-156,3,60,"#ff796e",5,20],[-71,-181,5,67,"#00e5ed",8,0],[134,-57,3,85,"#9bd32d",4,20],[99,19,4,31,"#00e5ed",7,12],[242,-301,3,82,"#ffe000",5,15],[240,-218,3,78,"#ffffff",8,0],[276,-227,3,42,"#36d6c8",5,10],[377,-193,4,42,"#ffe000",10,10],[397,-232,6,104,"#ffae00",6,18],[330,-280,3,90,"#ffe000",4,40]]

polygons = [
    Polygon(x, y, sides, side_length, color, pen_size, angle)
    for x, y, sides, side_length, color, pen_size, angle in POLYGON_DATA
]

for polygon in polygons:
    polygon.draw()
screen.update()

for frame in range(90):
    dx = 18 * math.sin(frame / 14)
    dy = 14 * math.cos(frame / 14)
    for index, (polygon, item) in enumerate(zip(polygons, POLYGON_DATA)):
        x, y, sides, side_length, color, pen_size, angle = item
        phase = index * 0.35
        polygon.move_to(
            x + dx * math.cos(phase),
            y + dy * math.sin(phase),
        )
    screen.update()
    time.sleep(0.03)

screen.mainloop()
