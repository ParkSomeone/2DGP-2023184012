world =[[],[]]

#add object, layer지정 필요
def add_object(o, depth=0):     #기본depth는0
    world[depth].append(o)


def remove_object(o):
    for layer in world:
        if o in layer:
            layer.remove(o)
            break   #더이상 찾을 필요가 없으므로 종료, 최적화


#game logic
def update():
    for layer in world:
        for o in layer:
            o.update()


#gmae rendering
def render():
    for layer in world:
        for o in layer:
            o.draw()