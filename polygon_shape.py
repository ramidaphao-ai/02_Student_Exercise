"""Reusable regular Polygon class. Each instance encapsulates its Turtle pen."""
import math
import numbers
import turtle


def _finite_number(value, name):
    if isinstance(value, bool) or not isinstance(value, numbers.Real):
        raise ValueError(f"{name} must be a finite number")
    if not math.isfinite(value):
        raise ValueError(f"{name} must be a finite number")
    return float(value)


class Polygon:
    def __init__(self, x, y, sides, side_length, color, pen_size=3, angle=0):
        if isinstance(sides, bool) or not isinstance(sides, int) or sides < 3:
            raise ValueError("sides must be an integer greater than or equal to 3")
        side_length = _finite_number(side_length, "side_length")
        pen_size = _finite_number(pen_size, "pen_size")
        angle = _finite_number(angle, "angle")
        if side_length <= 0:
            raise ValueError("side_length must be positive")
        if pen_size <= 0:
            raise ValueError("pen_size must be positive")
        if not isinstance(color, str) or not color.strip():
            raise ValueError("color must be a non-empty string")

        self._x = _finite_number(x, "x")
        self._y = _finite_number(y, "y")
        self._sides = sides
        self._side_length = side_length
        self._color = color
        self._pen_size = pen_size
        self._angle = angle
        self._pen = turtle.Turtle(visible=False)
        self._pen.speed(0)
        self._pen.penup()

    def draw(self):
        self._pen.penup()
        self._pen.goto(self._x, self._y)
        self._pen.setheading(self._angle)
        self._pen.pencolor(self._color)
        self._pen.pensize(self._pen_size)
        self._pen.pendown()
        for _ in range(self._sides):
            self._pen.forward(self._side_length)
            self._pen.left(360 / self._sides)
        self._pen.penup()

    def move_to(self, x, y):
        new_x = _finite_number(x, "x")
        new_y = _finite_number(y, "y")
        self._x = new_x
        self._y = new_y
        self._pen.clear()
        self.draw()
