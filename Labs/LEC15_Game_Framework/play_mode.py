from pico2d import *
import game_framework
import game_world
from boy import Boy
from grass import Grass
import pause_mode


boy = None


def handle_events():
    for event in get_events():
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_p:
            game_framework.push_mode(pause_mode)
            return
        elif boy is not None:
            boy.handle_event(event)


def init():
    global boy
    game_world.clear()
    boy = Boy()
    game_world.add_oject(boy)
    game_world.add_oject(Grass(), 0)


def update():
    game_world.update()


def render():
    clear_canvas()
    game_world.render()
    update_canvas()


def finish():
    global boy
    game_world.clear()
    boy = None


def pause():
    pass


def resume():
    pass
