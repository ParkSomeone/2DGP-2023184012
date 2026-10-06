from pico2d import *

WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 1024

open_canvas(WINDOW_WIDTH, WINDOW_HEIGHT)

tuk_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')

running = True
x = WINDOW_WIDTH // 2
y = WINDOW_HEIGHT // 2
frame = 0
