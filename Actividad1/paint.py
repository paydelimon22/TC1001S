"""Paint, for drawing shapes.

Exercises

1. Add a color.
2. Complete circle.
3. Complete rectangle.
4. Complete triangle.
5. Add width parameter.
"""

from turtle import *

from freegames import vector

# Needed for precise math calculations
import math

def line(start, end):
    """Draw line from start to end."""
    up()
    goto(start.x, start.y)
    down()
    goto(end.x, end.y)


def square(start, end):
    """Draw square from start to end."""
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(4):
        forward(end.x - start.x)
        left(90)

    end_fill()

def circle(start, end):
    """Draw cirlce with center at start, and circumference at end
    
    Parameters:
        start: Center of the circle
        end: Point in the circumference of the circle.
    """
    radius = math.dist(end, start)
    up()
    goto(start.x, start.y + radius)
    begin_fill()
    down()
    times_y_crossed = 0
    x_sign = 1.0
    # While the turtle hasn't crossed the middle of the circle more than once.
    # (While the turtle hasn't drawn both halves of the circle)
    while times_y_crossed <= 1:
        # Advance 1 degree of rotation of the circle.
        forward(2 * math.pi * radius/360.0)
        # Turn right 1 degree.
        right(1.0)
        # Compare if the turtle has changed sides of the circle.
        x_sign_new = math.copysign(1,xcor()-start.x)
        if(x_sign_new != x_sign):
            times_y_crossed += 1
            x_sign = x_sign_new
    end_fill()
    up()

def rectangle(start, end):
    """Draw rectangle with opposite corners start and end.

    Parameters:
        start: starting corner of rectangle.
        end: opposite corner of rectangle.
    """

    # Go to starting corner
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    # Go to rest of corners
    goto(end.x, start.y)
    goto(end.x, end.y)
    goto(start.x, end.y)
    goto(start.x, start.y)

    # End fill area
    end_fill()


def triangle(start, end):
    """Draw a triangle contained in a rectangular bounding box.

    Parameters:
        start: First corner of the bounding box.
        end: Opposite corner of the bounding box.
    """

    # Go to starting corner of the bounding box
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    # Draw base of triangle
    goto(end.x, start.y)

    # Draw tip of triangle
    goto((end.x - start.x) / 2 + start.x, end.y)

    # Return to start
    goto(start.x, start.y)

    end_fill()



def tap(x, y):
    """Store starting point or draw shape."""
    start = state['start']

    if start is None:
        state['start'] = vector(x, y)
    else:
        shape = state['shape']
        end = vector(x, y)
        shape(start, end)
        state['start'] = None


def store(key, value):
    """Store value in state at key."""
    state[key] = value


state = {'start': None, 'shape': line}
setup(420, 420, 370, 0)
onscreenclick(tap)
listen()
onkey(undo, 'u')
onkey(lambda: color('black'), 'K')
onkey(lambda: color('white'), 'W')
onkey(lambda: color('green'), 'G')
onkey(lambda: color('blue'), 'B')
onkey(lambda: color('red'), 'R')
onkey(lambda: color('pink'), 'P')

onkey(lambda: store('shape', line), 'l')
onkey(lambda: store('shape', square), 's')
onkey(lambda: store('shape', circle), 'c')
onkey(lambda: store('shape', rectangle), 'r')
onkey(lambda: store('shape', triangle), 't')
done()
