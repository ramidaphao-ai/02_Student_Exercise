# Student Polygon Art

Python Turtle Graphics exercise: a static collage and an animation built with an object-oriented `Polygon` class.

## Files

- `polygon_shape.py`: reusable regular Polygon class with validated state and a private-by-convention Turtle pen.
- `05_polygon_art_starter.py`: static collage containing 20 Polygon objects.
- `06_animated_polygon_art_starter.py`: animation that reuses those 20 objects for 90 frames.

## Run

Use Python 3 on a computer with a graphical desktop and Tkinter:

```bash
python3 05_polygon_art_starter.py
python3 06_animated_polygon_art_starter.py
```

The animation uses `screen.tracer(0)`, `Polygon.move_to()`, and `screen.update()`. Each Polygon owns its own Turtle, so clearing and moving one object does not erase another.
