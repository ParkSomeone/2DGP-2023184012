from pico2d import *

open_canvas()


def handle_events():
    events = []
    print('[handle_events] stage 1: event storage ready')

    events.extend(get_events())
    print('[handle_events] stage 2: events loaded')

    for event in events:
        print('[handle_events] stage 3: events checked')

        if event.type == SDL_QUIT:
            print('[handle_events] stage 4: close event checked')

        if event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            print('[handle_events] stage 5: quit key checked')


def update():
    print('update')


def render():
    print('render')


while True:
    handle_events()
    update()
    render()
