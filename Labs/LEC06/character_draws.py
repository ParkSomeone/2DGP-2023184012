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

def move_rectangle():
    print("rect")
    movecount=30
    theta=0.0
    for i in range(0,4):
        print("now angle",theta/(math.pi))
        for j in range(0,movecount):
            print("move",theta/(math.pi),j)
            pass
        theta += math.pi/2
            

def move_triangle():
    print("triangle")
    clear_canvas()
    character.draw(400, 300)
    update_canvas()
    pass

while(True):
    move_circle()
    move_rectangle()
    move_triangle()
    pass