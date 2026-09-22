from pico2d import *


open_canvas(800, 600)

# 여기를 채우시오.

character = load_image('character.png')

character.draw(400, 300)
character.draw(300, 200)
character.draw(500, 400)
update_canvas()

delay(2)

close_canvas()

