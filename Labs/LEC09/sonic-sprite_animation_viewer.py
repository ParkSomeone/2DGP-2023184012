"""Single-file Pico2D viewer for the Sonic sprite sheet in this directory."""

from pathlib import Path

import pico2d

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
SPRITE_PATH = Path(__file__).resolve().with_name("sonic-sprite.png")
SPRITE_SHEET_WIDTH = 399
SPRITE_SHEET_HEIGHT = 525


def load_sprite_sheet(image_path=SPRITE_PATH):
    if not image_path.is_file():
        raise FileNotFoundError(f"스프라이트 시트를 찾을 수 없습니다: {image_path}")
    return pico2d.load_image(str(image_path))


def validate_sprite_sheet_dimensions(sprite_sheet):
    actual_size = (sprite_sheet.w, sprite_sheet.h)
    expected_size = (SPRITE_SHEET_WIDTH, SPRITE_SHEET_HEIGHT)
    if actual_size != expected_size:
        raise ValueError(
            f"스프라이트 시트 크기가 예상과 다릅니다: "
            f"예상 {expected_size}, 실제 {actual_size}"
        )


def main():
    pico2d.open_canvas(WINDOW_WIDTH, WINDOW_HEIGHT)
    try:
        sprite_sheet = load_sprite_sheet()
        validate_sprite_sheet_dimensions(sprite_sheet)
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
