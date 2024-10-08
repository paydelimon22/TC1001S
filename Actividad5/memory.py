"""Memory, puzzle game of number pairs.

Exercises:

1. Count and print how many taps occur.
2. Decrease the number of tiles to a 4x4 grid.
3. Detect when all tiles are revealed.
4. Center single-digit tile.
5. Use letters instead of tiles.
"""

from random import *
from turtle import *

from freegames import path

number_of_taps = 0
car = path('car.gif')
tiles = list(range(32)) * 2
state = {'mark': None}
hide = [True] * 64

colors = [
    "Red",
    "Green",
    "Blue",
    "Yellow",
    "Cyan",
    "Magenta",
    "Maroon",
    "Olive",
    "DarkGreen",
    "Purple",
    "Teal",
    "Navy",
    "Orange",
    "Pink",
    "Silver",
    "Gray",
    "Coral",      
    "Gold",       
    "Brown",
    "Beige",
    "LightBlue",
    "LightGreen",
    "LightPink",
    "LightYellow",
    "Crimson",
    "Orchid",
    "DarkSlateBlue",
    "SeaGreen",
    "Chocolate",
    "Tomato",
    "LightSlateGray",
    "MediumSlateBlue"
]



def square(x, y, sqr_color=None):
    """Draw white square with black outline at (x, y)."""
    up()
    goto(x, y)
    down()
    if sqr_color is None:
        color('black', 'white')
    else:
        color('black', sqr_color)
    begin_fill()
    for count in range(4):
        forward(50)
        left(90)
    end_fill()


def index(x, y):
    """Convert (x, y) coordinates to tiles index."""
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)


def xy(count):
    """Convert tiles count to (x, y) coordinates."""
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200


def tap(x, y):
    """Update mark and hidden tiles based on tap."""
    global number_of_taps
    number_of_taps += 1
    spot = index(x, y)
    mark = state['mark']

    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None


def draw():
    """Draw image and tiles."""
    clear()
    goto(0, 0)
    shape(car)
    stamp()

    all_discovered = True
    for count in range(64):
        if hide[count]:
            x, y = xy(count)
            square(x, y)
            all_discovered = False

    if all_discovered:
        up()
        goto(0,-200)
        pencolor("white")
        write("You win!", align="center", font=("Arial", 30, "normal"))
        return

    mark = state['mark']

    if mark is not None and hide[mark]:
        x, y = xy(mark)
        square(x, y, colors[tiles[mark]])
        up()
        goto(x + 25, y)
        write(tiles[mark], align="center", font=('Arial', 30, 'normal'))

    up()
    goto(0,200)
    write(f"Number of taps: {number_of_taps}", align="center",
          font=("Arial", 12, "normal"))

    update()
    ontimer(draw, 100)


shuffle(tiles)
setup(420, 450, 370, 0)
addshape(car)
hideturtle()
tracer(False)
onscreenclick(tap)
draw()
done()
