from pico2d import *

WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 1024
SPRITE_SIZE = 100
FRAME_COUNT = 8
MOVE_SPEED = 5

open_canvas(WINDOW_WIDTH, WINDOW_HEIGHT)

tuk_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')

running = True
x = WINDOW_WIDTH // 2
y = WINDOW_HEIGHT // 2
frame = 0
move_x = 0
move_y = 0
direction = 'down'


def clamp(value, minimum, maximum):
    return max(minimum, min(value, maximum))


def get_move_row():
    global direction
    if move_x > 0:
        direction = 'right'
        return 200
    if move_x < 0:
        direction = 'left'
        return 100
    if move_y > 0:
        direction = 'up'
        return 0
    if move_y < 0:
        direction = 'down'
        return 300
    direction = 'idle'
    return 300


def handle_events():
    global running, move_x, move_y
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                running = False
            elif event.key == SDLK_RIGHT:
                move_x += 1
            elif event.key == SDLK_LEFT:
                move_x -= 1
            elif event.key == SDLK_UP:
                move_y += 1
            elif event.key == SDLK_DOWN:
                move_y -= 1
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                move_x -= 1
            elif event.key == SDLK_LEFT:
                move_x += 1
            elif event.key == SDLK_UP:
                move_y -= 1
            elif event.key == SDLK_DOWN:
                move_y += 1


while running:
    clear_canvas()
    tuk_ground.draw(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)

    if move_x == 0 and move_y == 0:
        row = 300
    else:
        row = get_move_row()

    character.clip_draw(frame * SPRITE_SIZE, row, SPRITE_SIZE, SPRITE_SIZE, x, y)
    update_canvas()
    handle_events()

    x += move_x * MOVE_SPEED
    y += move_y * MOVE_SPEED
    x = clamp(x, SPRITE_SIZE // 2, WINDOW_WIDTH - SPRITE_SIZE // 2)
    y = clamp(y, SPRITE_SIZE // 2, WINDOW_HEIGHT - SPRITE_SIZE // 2)

    frame = (frame + 1) % FRAME_COUNT
    delay(0.05)

close_canvas()
