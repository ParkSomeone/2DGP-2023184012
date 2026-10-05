"""Single-file Pico2D viewer for the Sonic sprite sheet in this directory."""

import pico2d

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600


def main():
    pico2d.open_canvas(WINDOW_WIDTH, WINDOW_HEIGHT)
    running = True

    while running:
        for event in pico2d.get_events():
            if event.type == pico2d.SDL_QUIT:
                running = False
                break

        if running:
            pico2d.update_canvas()
            pico2d.delay(0.01)

    pico2d.close_canvas()


if __name__ == "__main__":
    main()
