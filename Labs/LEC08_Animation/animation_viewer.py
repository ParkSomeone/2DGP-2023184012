from pico2d import *

open_canvas()


def handle_events():
    events = []
    print('[handle_events] stage 1: event storage ready')

    events.extend(get_events())
    print('[handle_events] stage 2: events loaded')


def update():
    print('update')


def render():
    print('render')


while True:
    handle_events()
    update()
    render()
