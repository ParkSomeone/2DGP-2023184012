from pico2d import *
import game_framework

image = None


def init():
    global image
    image = load_image('pause.png')


def handle_events():
    for event in get_events():
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                game_framework.quit()
            elif event.key == SDLK_p:
                game_framework.pop_mode()
                return


def update():
    pass


def render():
    clear_canvas()
    image.draw(400, 300)
    update_canvas()


def finish():
    global image
    image = None
