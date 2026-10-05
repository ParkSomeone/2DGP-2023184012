"""Single-file Pico2D viewer for the Sonic sprite sheet in this directory."""

from dataclasses import dataclass
from pathlib import Path

import pico2d

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
FRAME_INTERVAL_SECONDS = 0.1
SPRITE_PATH = Path(__file__).resolve().with_name("sonic-sprite.png")
SPRITE_SHEET_WIDTH = 399
SPRITE_SHEET_HEIGHT = 525

# Each frame bound is (left, top, width, height) in the original PNG.
FRAME_BOUNDS_TOP = (
    (
        (1, 39, 29, 39), (31, 40, 26, 38), (58, 39, 28, 39),
        (86, 40, 30, 38), (118, 40, 30, 38), (150, 40, 30, 38),
        (182, 40, 29, 38), (211, 39, 29, 38), (240, 39, 29, 38),
        (270, 45, 24, 32), (302, 51, 29, 26),
    ),
    (
        (8, 80, 26, 37), (37, 80, 27, 37), (65, 80, 31, 38),
        (97, 80, 37, 37), (135, 80, 32, 35), (170, 79, 32, 38),
        (206, 79, 26, 38), (238, 80, 24, 37), (263, 80, 30, 37),
        (295, 80, 36, 37), (334, 80, 32, 36), (370, 79, 29, 38),
    ),
    (
        (1, 124, 33, 40), (39, 124, 35, 39), (89, 125, 35, 38),
        (130, 121, 34, 42), (181, 122, 34, 41), (228, 122, 33, 40),
    ),
    (
        (1, 169, 29, 30), (35, 167, 29, 31), (67, 169, 30, 29),
        (98, 169, 31, 29), (131, 168, 29, 30), (162, 168, 29, 31),
        (193, 170, 30, 29), (230, 170, 31, 29), (268, 170, 30, 30),
    ),
    (
        (1, 206, 30, 27), (36, 206, 29, 27), (70, 206, 29, 27),
        (105, 206, 29, 27), (139, 206, 29, 27), (174, 206, 29, 27),
    ),
    (
        (1, 239, 29, 35), (36, 239, 30, 35), (74, 239, 31, 35),
        (111, 238, 31, 36), (149, 239, 30, 35), (186, 238, 31, 36),
    ),
    (
        (1, 283, 29, 35), (36, 283, 30, 35), (72, 286, 39, 31),
        (123, 285, 39, 32), (172, 286, 39, 31), (218, 285, 38, 32),
    ),
    (
        (1, 326, 24, 45), (31, 327, 29, 44), (65, 327, 20, 44),
        (90, 327, 25, 43), (119, 327, 25, 43), (149, 327, 20, 44),
        (184, 341, 40, 28), (232, 341, 39, 27),
    ),
    (
        (1, 379, 27, 38), (31, 379, 31, 36), (64, 379, 31, 36),
        (99, 377, 33, 38), (136, 379, 32, 36), (176, 379, 33, 36),
        (217, 379, 33, 36), (254, 378, 33, 36),
    ),
    (
        (6, 429, 34, 40), (49, 426, 34, 43),
        (96, 427, 23, 39), (125, 427, 23, 39),
    ),
)

ANIMATION_FRAMES_TOP = FRAME_BOUNDS_TOP
ANIMATION_ORDER = (
    "동작 1", "동작 2", "동작 3", "동작 4", "동작 5",
    "동작 6", "동작 7", "동작 8", "동작 9", "동작 10",
)
ANIMATIONS = tuple(zip(ANIMATION_ORDER, ANIMATION_FRAMES_TOP))


@dataclass
class PlaybackState:
    animation_index: int = 0
    frame_index: int = 0
    completed_cycles: int = 0
    last_frame_change_time: float = 0.0
    is_waiting: bool = False
    wait_started_at: float = 0.0


def frame_interval_elapsed(state, current_time):
    return current_time >= state.last_frame_change_time + FRAME_INTERVAL_SECONDS


def render(sprite_sheet, state):
    _, frames = ANIMATIONS[state.animation_index]
    left, top, width, height = frames[state.frame_index]
    bottom = SPRITE_SHEET_HEIGHT - top - height

    pico2d.clear_canvas()
    sprite_sheet.clip_draw(
        left,
        bottom,
        width,
        height,
        WINDOW_WIDTH // 2,
        WINDOW_HEIGHT // 2,
        width,
        height,
    )
    pico2d.update_canvas()


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
        state = PlaybackState()
        running = True

        while running:
            for event in pico2d.get_events():
                if event.type == pico2d.SDL_QUIT:
                    running = False
                    break

            if running:
                render(sprite_sheet, state)
                pico2d.delay(0.01)
    finally:
        pico2d.close_canvas()


if __name__ == "__main__":
    main()
