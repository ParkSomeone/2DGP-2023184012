"""Single-file Pico2D viewer for the Sonic sprite sheet in this directory."""

from pathlib import Path

import pico2d

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
SPRITE_PATH = Path(__file__).resolve().with_name("sonic-sprite.png")


def load_sprite_sheet(image_path=SPRITE_PATH):
    if not image_path.is_file():
        raise FileNotFoundError(f"스프라이트 시트를 찾을 수 없습니다: {image_path}")
    return pico2d.load_image(str(image_path))


def main():
    pico2d.open_canvas(WINDOW_WIDTH, WINDOW_HEIGHT)
    try:
        sprite_sheet = load_sprite_sheet()
        running = True

        while running:
            for event in pico2d.get_events():
                if event.type == pico2d.SDL_QUIT:
                    running = False
                    break

            if running:
                pico2d.update_canvas()
                pico2d.delay(0.01)
    finally:
        pico2d.close_canvas()


if __name__ == "__main__":
    main()
