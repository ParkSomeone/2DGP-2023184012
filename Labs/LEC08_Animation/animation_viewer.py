from pico2d import *

open_canvas()
running = True


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
    current_time = get_time()
    print('[update] stage 1: time prepared')


def render():
    print('render')


while running:
    handle_events()

    print('[handle_events] stage 7: loop connection checked')
    if not running:
        break

    update()
    render()
