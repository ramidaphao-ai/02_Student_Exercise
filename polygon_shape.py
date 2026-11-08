
import turtle

class Polygon(turtle.Turtle):
    def __init__(self, color, x, y, sides, length):
        super().__init__()

        self.shape("turtle")
        self.pencolor(color)
        self.pensize(100)
        self.penup()
        self.goto(x, y)
        self.pendown()

        self.sides = sides
        self.length = length

    def draw(self):
        for _ in range(self.sides):
            self.forward(self.length)
            self.left(360 // self.sides)

