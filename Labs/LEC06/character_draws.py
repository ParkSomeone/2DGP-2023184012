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
    movecount=20
    theta=0.0
    x=400
    y=300
    speed=4
    for i in range(0,4):
        for j in range(0,movecount):
            delay(0.01)
            clear_canvas()
            x+=math.cos(theta)*speed
            y+=math.sin(theta)*speed
            character.draw(x, y)
            update_canvas()
        theta += math.pi/2
            

def move_triangle():
    movecount=20
    theta=0.0
    x=400
    y=300
    speed=4
    print("triangle")
    for i in range(0,3):
        theta=math.pi*(2/3)
        print("move angle",theta/math.pi)
        for j in range(0, movecount):
            x+=math.cos(theta)*speed
            y+=math.sin(theta)*speed
            print("move",x,y)
    pass

while(True):
    move_circle()
    move_rectangle()
    move_triangle()
    pass