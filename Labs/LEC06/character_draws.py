# 실습 과제 진행
## 여기를 채우시오.
from pico2d import *
import math

open_canvas(800, 600)
character = load_image('character.png')

def move_circle():
    print("circle")
    #circle 확인했으므로 pass
    return
    theta=0.0
    r=50
    while theta<2*math.pi:
        draw_charater(400+math.cos(theta)*50,300+math.sin(theta)*50)



def draw_top():
    print("top")
    for x in range(50, 751, 5):
        draw_charater(x,550)
    pass

#코드를 함수로 자동변환 하는방법
#코드선택->우클릭->refactor->extract function
def draw_charater(x,y):
    clear_canvas()
    character.draw(x, y)
    update_canvas()
    delay(0.01)

def draw_right():
    print("right")
    for y in range(551, 50, -5):
        draw_charater(750,y)
    pass
def draw_bottom():
    print("bottom")
    for x in range(750, 51, -5):
        draw_charater(x,51)
    pass
def draw_left():
    print("left")
    for y in range(50, 551, 5):
        draw_charater(50,y)
    pass

def move_rectangle():
    print("rect")
    #draw_rectangle skip
    return
    draw_top()
    draw_right()
    draw_bottom()
    draw_left()
    pass

def draw_one():
    print("one")
    for i in range(0,101,10):
        draw_charater(400-i*3,500-i*4)
        print(400-i*3,500-i*4)
    pass
def draw_two():
    print("two")
    for i in range(0,101,10):
        draw_charater(100+i*7,100)
        print(100+i*7,100)
    pass
def draw_three():
    print("three")
    for i in range(0,101,10):
        draw_charater(700-i*3,100+i*4)
        print(700-i*3,100+i*4)
    delay(10)
    pass

def move_triangle():
    print("triangle")
    draw_one()
    draw_two()
    draw_three()
    pass


while(True):
    move_circle()
    move_rectangle()
    move_triangle()
    pass