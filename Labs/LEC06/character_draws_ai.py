from pico2d import *
import math


CANVAS_WIDTH = 800
CANVAS_HEIGHT = 600
CENTER_X = CANVAS_WIDTH / 2
CENTER_Y = CANVAS_HEIGHT / 2
FRAME_DELAY = 0.01

open_canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
character = load_image('character.png')


def draw_position(x, y):
    clear_canvas()
    character.draw(x, y)
    update_canvas()
    delay(FRAME_DELAY)


def move_circle():
    radius = 100
    frame_count = 120

    for frame in range(frame_count + 1):
        angle = 2 * math.pi * frame / frame_count
        x = CENTER_X + math.cos(angle) * radius
        y = CENTER_Y + math.sin(angle) * radius
        draw_position(x, y)


def move_polygon(vertices, steps_per_edge):
    for index, start in enumerate(vertices):
        end = vertices[(index + 1) % len(vertices)]

        for step in range(1, steps_per_edge + 1):
            progress = step / steps_per_edge
            x = start[0] + (end[0] - start[0]) * progress
            y = start[1] + (end[1] - start[1]) * progress
            draw_position(x, y)


def move_rectangle():
    vertices = [
        (500, 300),
        (500, 220),
        (300, 220),
        (300, 380),
        (500, 380),
    ]
    move_polygon(vertices, steps_per_edge=40)


def move_triangle():
    vertices = [
        (500, 300),
        (350, 387),
        (350, 213),
    ]
    move_polygon(vertices, steps_per_edge=45)


try:
    while True:
        move_circle()
        move_rectangle()
        move_triangle()
finally:
    close_canvas()
