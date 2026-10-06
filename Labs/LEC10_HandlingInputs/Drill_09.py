from pico2d import *

WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 1024
SPRITE_SIZE = 100
FRAME_COUNT = 8

open_canvas(WINDOW_WIDTH, WINDOW_HEIGHT)

tuk_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')

running = True
x = WINDOW_WIDTH // 2
y = WINDOW_HEIGHT // 2
frame = 0


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False


while running:
    clear_canvas()
    tuk_ground.draw(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)
    character.clip_draw(frame * SPRITE_SIZE, 300, SPRITE_SIZE, SPRITE_SIZE, x, y)
    update_canvas()
    handle_events()
    frame = (frame + 1) % FRAME_COUNT
    delay(0.05)

close_canvas()
