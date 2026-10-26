from pico2d import *
import random


# Game object class here
#게임 객체를 파악

#class는 첫 문자 대문자로
class Grass:
    def __init__(self):
        self.image = load_image('grass.png')
    def draw(self):
       self.image.draw(400, 30)
    def update(self): 
       pass
class Boy:
    def  __init__(self):
        self.x, self.y = random.randint(100, 700), 90
        self.frame=0
        self.image=load_image('run_animation.png')
    def update(self):
        self.frame=(self.frame+1)%8
        self.x+=5
    def draw(self):
        self.image.clip_draw(self.frame*100,0,100,100,self.x,self.y)
        pass
    pass

class Ball:
    pass

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

def reset_world():
    global running
    global world#월드 전체를 나타내는 리스트, 월드의 모든 객체들이 있다
    world=[]
    running = True
    #잔디 객체를 찍어낸다
    grass = Grass()
    world.append(grass)
    team=[Boy()for i in range(11)]  #11명의 객체생성 후 team리스트에 넣는다
    balls=[Ball()for i in range(20)]
    world+=team                     #world리스트에 team리스트를 합친다

def update_world():
    for o in world:
        o.update()
    pass

def render_world():
    clear_canvas()
    for o in world:
        o.draw()
    update_canvas()


open_canvas()
reset_world()
while running:
    handle_events()
    update_world()
    render_world()
    delay(0.05)

close_canvas()
