from pico2d import *

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

open_canvas(WINDOW_WIDTH, WINDOW_HEIGHT)

# 실제 사용하는 스프라이트 파일 이름에 맞게 수정하세요.
bod = load_image('BOD_SpritSheet.png')

frame_interval = 0.1

animation_wait_time = 1.0


animations = [
    [
        {'x': 0,  'y': 544, 'width': 54, 'height': 85},
        {'x': 55,  'y': 544, 'width': 56, 'height': 85},
        {'x': 112,  'y': 544, 'width': 56, 'height': 85},
        {'x': 169,  'y': 544, 'width': 54, 'height': 85},
        {'x': 224,  'y': 544, 'width': 48, 'height': 85},
        {'x': 273,  'y': 544, 'width': 46, 'height': 85},
        {'x': 320,  'y': 544, 'width': 45, 'height': 85},
        {'x': 366,  'y': 544, 'width': 50, 'height': 85},
    ],

    [
        {'x': 75,   'y': 469, 'width': 60,  'height': 85},
        {'x': 210,  'y': 469, 'width': 75,  'height': 85},
        {'x': 345,  'y': 469, 'width': 75,  'height': 85},
        {'x': 490,  'y': 469, 'width': 70,  'height': 85},

        {'x': 565,  'y': 469, 'width': 135, 'height': 85},
        {'x': 700,  'y': 469, 'width': 135, 'height': 85},
        {'x': 840,  'y': 469, 'width': 130, 'height': 85},
        {'x': 980,  'y': 469, 'width': 140, 'height': 85},
    ],

    [
        {'x': 0,    'y': 359, 'width': 140, 'height': 85},
        {'x': 205,  'y': 359, 'width': 80,  'height': 85},
        {'x': 345,  'y': 359, 'width': 80,  'height': 85},
        {'x': 490,  'y': 359, 'width': 75,  'height': 85},
        {'x': 630,  'y': 359, 'width': 75,  'height': 85},
        {'x': 770,  'y': 359, 'width': 80,  'height': 85},
        {'x': 910,  'y': 359, 'width': 80,  'height': 85},
        {'x': 1050, 'y': 359, 'width': 70, 'height': 85},
    ],

    [
        {'x': 75,   'y': 269, 'width': 70, 'height': 90},
        {'x': 210,  'y': 269, 'width': 75, 'height': 90},
        {'x': 355,  'y': 269, 'width': 70, 'height': 90},
        {'x': 490,  'y': 269, 'width': 70, 'height': 90},
        {'x': 625,  'y': 269, 'width': 75, 'height': 90},
        {'x': 765,  'y': 269, 'width': 75, 'height': 90},
        {'x': 905,  'y': 269, 'width': 70, 'height': 90},
        {'x': 1045, 'y': 269, 'width': 75, 'height': 90},
    ],

    [
        {'x': 75,   'y': 179, 'width': 70, 'height': 90},
        {'x': 210,  'y': 179, 'width': 70, 'height': 90},
        {'x': 350,  'y': 179, 'width': 70, 'height': 90},
        {'x': 490,  'y': 179, 'width': 70, 'height': 90},
        {'x': 625,  'y': 179, 'width': 75, 'height': 90},
        {'x': 765,  'y': 179, 'width': 70, 'height': 90},
        {'x': 910,  'y': 179, 'width': 70, 'height': 90},
        {'x': 1050, 'y': 179, 'width': 70, 'height': 90},
    ],

    [
        {'x': 45,   'y': 74, 'width': 50, 'height': 85},
        {'x': 185,  'y': 74, 'width': 50, 'height': 85},
        {'x': 325,  'y': 74, 'width': 50, 'height': 85},
        {'x': 465,  'y': 74, 'width': 50, 'height': 85},
        {'x': 605,  'y': 74, 'width': 50, 'height': 85},
        {'x': 745,  'y': 74, 'width': 50, 'height': 85},
        {'x': 885,  'y': 74, 'width': 50, 'height': 85},
        {'x': 1025, 'y': 74, 'width': 50, 'height': 85},
    ],

    [
        {'x': 51,   'y': 57, 'width': 33, 'height': 114},
        {'x': 190,  'y': 57, 'width': 34, 'height': 114},
        {'x': 331,  'y': 57, 'width': 35, 'height': 114},
        {'x': 470,  'y': 57, 'width': 36, 'height': 114},
        {'x': 609,  'y': 57, 'width': 34, 'height': 114},
        {'x': 754,  'y': 57, 'width': 29, 'height': 114},
        {'x': 892,  'y': 57, 'width': 31, 'height': 114},
        {'x': 1032, 'y': 57, 'width': 31, 'height': 114},
    ],


    [
        {'x': 45,   'y': 0, 'width': 50, 'height': 69},
        {'x': 185,  'y': 0, 'width': 50, 'height': 69},
        {'x': 325,  'y': 0, 'width': 50, 'height': 69},
        {'x': 465,  'y': 0, 'width': 50, 'height': 69},
        {'x': 605,  'y': 0, 'width': 50, 'height': 69},
        {'x': 745,  'y': 0, 'width': 50, 'height': 69},
        {'x': 885,  'y': 0, 'width': 50, 'height': 69},
        {'x': 1025, 'y': 0, 'width': 50, 'height': 69},
    ],
]


running = True
current_animation = 0
frame = 0
last_frame_time = 0.0
is_waiting = False
wait_start_time = 0.0

def handle_events():
    global running

    events = get_events()

    for event in events:

        # 창 닫기
        if event.type == SDL_QUIT:
            running = False

        # ESC 키
        if event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                running = False


def update():

    global current_animation
    global frame
    global last_frame_time
    global is_waiting
    global wait_start_time

    current_time = get_time()

    if is_waiting:

        if current_time - wait_start_time >= animation_wait_time:
            current_animation += 1
            if current_animation >= len(animations):
                current_animation = 0
            frame = 0
            is_waiting = False
            last_frame_time = current_time

        return

    if current_time - last_frame_time < frame_interval:
        return

    last_frame_time = current_time

    frame_count = len(animations[current_animation])

    frame += 1


    if frame >= frame_count:
        frame = 0
        is_waiting = True
        wait_start_time = current_time

def render():

    sprite = animations[current_animation][frame]

    scale = min(
        WINDOW_WIDTH / sprite['width'],
        WINDOW_HEIGHT / sprite['height']
    )

    draw_width = int(sprite['width'] * scale)
    draw_height = int(sprite['height'] * scale)
    clear_canvas()

    bod.clip_draw(
        sprite['x'],
        sprite['y'],
        sprite['width'],
        sprite['height'],

        # 출력 위치
        WINDOW_WIDTH // 2,
        WINDOW_HEIGHT // 2,

        # 출력 크기
        draw_width,
        draw_height
    )


    update_canvas()

    delay(0.01)

while running:
    handle_events()

    if not running:
        break

    update()
    render()
close_canvas()