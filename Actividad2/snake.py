"""Snake, classic arcade game.

Exercises

1. How do you make the snake faster or slower?
2. How can you make the snake go around the edges?
3. How would you move the food?
4. Change the snake to respond to mouse clicks.
"""

from random import randrange
from turtle import *

from freegames import square, vector

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)


def change(x, y):
    """Change snake direction."""
    aim.x = x
    aim.y = y


def inside(head):
    """Return True if head inside boundaries."""
    return -200 < head.x < 190 and -200 < head.y < 190


def food_move():
    """Randomly move the food one segment in any direction."""
    directions = [vector(10, 0), vector(-10, 0), vector(0, 10), vector(0, -10)]
    rand_index = randrange(len(directions))
    food.move(directions[rand_index])

    original_rand_index = rand_index  # Keep track of original direction.
    # Make sure the food doesn't move into the snake body, or out of bounds.
    while food in snake or not inside(food):
        food.move(-directions[rand_index])  # Revert movement.
        rand_index = (rand_index + 1) % len(directions)  # Try next direction.
        # Break loop if all directions are invalid. Food can't move.
        if (rand_index == original_rand_index):
            break
        food.move(directions[rand_index])  # Move in new direction.

    update()
    ontimer(food_move, 100)


def move():
    """Move snake forward one segment."""
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    clear()

    for body in snake:
        square(body.x, body.y, 9, 'black')

    square(food.x, food.y, 9, 'green')
    update()
    ontimer(move, 100)


setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
food_move()
move()
done()
