# 실습 과제 진행
## 여기를 채우시오.
from pico2d import *

open_canvas(800, 600)
character = load_image('character.png')

def move_circle():
    print("circle")
    clear_canvas()
    character.draw(400, 300)
    update_canvas()
    #캐릭터 이미지 표시
    pass
def move_rectangle():
    print("rect")
    pass
def move_triangle():
    print("triangle")
    pass

while(True):
    move_circle()
    move_rectangle()
    move_triangle()
    pass