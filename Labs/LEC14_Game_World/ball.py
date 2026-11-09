from pico2d import get_canvas_width, load_image

import game_world


class Ball:
    image = None

    def __init__(self, x, y, direction):
        if Ball.image is None:
            Ball.image = load_image('ball21x21.png')

        self.image = Ball.image
        self.x = x
        self.y = y
        self.direction = direction

    def update(self):
        self.x += self.direction * 10
        if self.x < 0 or self.x > get_canvas_width():
            game_world.remove_object(self)

    def draw(self):
        self.image.draw(self.x, self.y)
