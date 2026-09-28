# 실습 과제 진행
## 여기를 채우시오.
from pico2d import *
import math

open_canvas(800, 600)
character = load_image('character.png')

def move_circle():
    print("circle")
    theta=0.0
    r=50
    while theta<2*math.pi:
        delay(0.01)
        theta += 0.1
        clear_canvas()
        character.draw(400+math.cos(theta)*50, 300+math.sin(theta)*50)
        update_canvas()

def draw_top():
    pass

def draw_left():
    pass
def draw_bottom():
    pass
def draw_tright():
    pass


def move_rectangle():
    print("rect")
    draw_top()
    draw_left()
    draw_bottom()
    draw_tright()
    pass
            

def move_triangle():
    print("triangle")
    pass


while(True):
    move_circle()
    move_rectangle()
    move_triangle()
    pass