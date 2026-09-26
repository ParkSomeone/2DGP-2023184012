# 실습 과제 진행
## 여기를 채우시오.
from pico2d import *
import math

open_canvas(800, 600)
character = load_image('character.png')

def move_circle():
    theta=0.0
    r=50
    pass
    while theta<2*math.pi:
        delay(0.01)
        theta += 0.1
        print("circle")
        clear_canvas()
        character.draw(400+math.cos(theta)*50, 300+math.sin(theta)*50)
        update_canvas()

def move_rectangle():
    speed=5
    movecount=10
    theta=0.0
    for i in range(0,4):
        for j in range(0,movecount):
            clear_canvas()
            character.draw(400, 300)
            update_canvas()
            print("rect")
        theta += math.pi/2

def move_triangle():
    clear_canvas()
    character.draw(400, 300)
    update_canvas()
    print("triangle")
    pass

while(True):
    move_circle()
    delay(1)
    move_rectangle()
    delay(1)
    move_triangle()
    delay(1)
    pass