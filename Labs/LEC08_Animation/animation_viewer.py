from pico2d import *

open_canvas()
running = True
frame_interval = 0.1
last_frame_time = 0.0
frame = 0
animations = [[None] * 8]
current_animation = 0
animation_repeat = 0
is_paused = False
pause_start_time = 0.0


def handle_events():
    global running

    events = []
    print('[handle_events] stage 1: event storage ready')

    events.extend(get_events())
    print('[handle_events] stage 2: events loaded')

    for event in events:
        print('[handle_events] stage 3: events checked')

        if event.type == SDL_QUIT:
            print('[handle_events] stage 4: close event checked')
            running = False
            print('[handle_events] stage 6: quit state updated')

        if event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            print('[handle_events] stage 5: quit key checked')
            running = False
            print('[handle_events] stage 6: quit state updated')


def update():
    global last_frame_time, frame, animation_repeat
    global is_paused, pause_start_time

    current_time = get_time()
    print('[update] stage 1: time prepared')

    if current_time - last_frame_time >= frame_interval:
        last_frame_time = current_time
        print('[update] stage 2: frame interval checked')

        frame_count = len(animations[current_animation])
        print('[update] stage 5: frame count applied')

        if not is_paused:
            frame += 1
            print('[update] stage 3: frame changed')

            if frame >= frame_count:
                frame = 0
                animation_repeat += 1
                print('[update] stage 4: animation cycle completed')

                if animation_repeat >= 5:
                    is_paused = True
                    pause_start_time = current_time
                    print('[update] stage 6: five repetitions checked')


def render():
    print('render')


while running:
    handle_events()

    print('[handle_events] stage 7: loop connection checked')
    if not running:
        break

    update()
    render()
