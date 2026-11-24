import random
import math

from pico2d import load_image, load_font, draw_rectangle, get_canvas_width, get_canvas_height
from py_trees.blackboard import Blackboard
from py_trees.behaviour import Behaviour
from py_trees.common import Status
from py_trees.composites import Selector, Sequence
from py_trees.trees import BehaviourTree

import game_framework
import game_world
import common

# 좀비 달리기 속력: km/h -> 픽셀/초
PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
RUN_SPEED_KMPH = 10.0  # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

# 좀비 애니메이션 속도: 0.5초에 10프레임
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 10

ANIMATION_NAMES = ['Walk', 'Idle']


class SetPatrolLocation(Behaviour):
    def __init__(self, zombie):
        super().__init__('Set Patrol Location')
        self.zombie = zombie

    def update(self):
        target = self.zombie.patrol_locations[self.zombie.patrol_index]
        self.zombie.blackboard.set('target', target)
        self.zombie.tx, self.zombie.ty = target
        return Status.SUCCESS


class MoveToTarget(Behaviour):
    def __init__(self, zombie):
        super().__init__('Move To Target')
        self.zombie = zombie

    def update(self):
        dx = self.zombie.tx - self.zombie.x
        dy = self.zombie.ty - self.zombie.y
        distance = math.sqrt(dx * dx + dy * dy)

        if distance < 5:
            self.zombie.speed = 0.0
            self.zombie.state = 'Idle'
            self.zombie.patrol_index = (
                self.zombie.patrol_index + 1
            ) % len(self.zombie.patrol_locations)
            return Status.SUCCESS

        dt = game_framework.frame_time
        self.zombie.dir = math.atan2(dy, dx)
        self.zombie.speed = RUN_SPEED_PPS
        self.zombie.x += dx / distance * self.zombie.speed * dt
        self.zombie.y += dy / distance * self.zombie.speed * dt
        self.zombie.state = 'Walk'
        return Status.RUNNING


class BoyInRange(Behaviour):
    def __init__(self, zombie):
        super().__init__('Boy In 7m')
        self.zombie = zombie

    def update(self):
        if common.boy is None:
            return Status.FAILURE

        dx = common.boy.x - self.zombie.x
        dy = common.boy.y - self.zombie.y
        distance = math.sqrt(dx * dx + dy * dy)
        if distance <= 7.0 * PIXEL_PER_METER:
            return Status.SUCCESS
        return Status.FAILURE


class SetBoyLocation(Behaviour):
    def __init__(self, zombie):
        super().__init__('Set Boy Target')
        self.zombie = zombie

    def update(self):
        if common.boy is None:
            return Status.FAILURE

        target = (common.boy.x, common.boy.y)
        self.zombie.blackboard.set('target', target)
        self.zombie.tx, self.zombie.ty = target
        return Status.SUCCESS


class ChaseBoy(Behaviour):
    def __init__(self, zombie):
        super().__init__('Chase Boy')
        self.zombie = zombie

    def update(self):
        if common.boy is None:
            return Status.FAILURE

        dx = common.boy.x - self.zombie.x
        dy = common.boy.y - self.zombie.y
        distance = math.sqrt(dx * dx + dy * dy)

        if distance < 5:
            self.zombie.speed = 0.0
            self.zombie.state = 'Idle'
            return Status.SUCCESS

        dt = game_framework.frame_time
        self.zombie.dir = math.atan2(dy, dx)
        self.zombie.speed = RUN_SPEED_PPS
        self.zombie.x += dx / distance * self.zombie.speed * dt
        self.zombie.y += dy / distance * self.zombie.speed * dt
        self.zombie.state = 'Walk'
        return Status.RUNNING


class BlackboardUI:
    def __init__(self, zombie):
        self.zombie = zombie
        self.image = load_image('blackboard.png')
        self.marker_image = load_image('hand_arrow.png')
        self.font = load_font('ENCR10B.TTF', 24)

    def update(self):
        pass

    def draw(self):
        canvas_height = get_canvas_height()
        self.image.draw(180, canvas_height - 85)
        self.font.draw(
            62,
            canvas_height - 85,
            f'target=({self.zombie.tx},{self.zombie.ty})',
            (0, 0, 0)
        )
        self.marker_image.draw(self.zombie.tx, self.zombie.ty)


class Zombie:
    images = None
    font = None

    def load_images(self):
        if Zombie.images is None:
            Zombie.images = {
                name: [load_image(f'./zombie/{name} ({i}).png') for i in range(1, 11)]
                for name in ANIMATION_NAMES
            }
            Zombie.font = load_font('ENCR10B.TTF', 40)

    def __init__(self, x=None, y=None):
        self.load_images()
        self.x = x if x is not None else random.randint(100, get_canvas_width() - 100)
        self.y = y if y is not None else random.randint(100, get_canvas_height() - 100)
        self.dir = 0.0  # 이동 방향 (라디안)
        self.speed = 0.0
        self.frame = random.randint(0, 9)
        self.state = 'Idle'
        self.ball_count = 0  # 주운 공의 개수

        self.blackboard = Blackboard()
        self.patrol_locations = [
            (43, 274),
            (1118, 274),
            (1050, 494),
            (575, 804),
            (235, 991),
            (575, 804),
            (1050, 494),
            (1118, 274),
        ]
        self.patrol_index = 0
        self.blackboard.set('target', self.patrol_locations[self.patrol_index])
        self.tx, self.ty = self.patrol_locations[self.patrol_index]
        patrol_sequence = Sequence(
            name='Patrol',
            memory=False,
            children=[
                SetPatrolLocation(self),
                MoveToTarget(self),
            ]
        )
        chase_sequence = Sequence(
            name='Chase',
            memory=False,
            children=[
                BoyInRange(self),
                SetBoyLocation(self),
                ChaseBoy(self),
            ]
        )
        chase_or_patrol = Selector(
            name='Chase or Patrol',
            memory=False,
            children=[chase_sequence, patrol_sequence]
        )
        self.behaviour_tree = BehaviourTree(chase_or_patrol)

    def update(self):
        dt = game_framework.frame_time
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * dt) % FRAMES_PER_ACTION
        self.behaviour_tree.tick()

    def draw(self):
        image = Zombie.images[self.state][int(self.frame)]
        if math.cos(self.dir) < 0:  # 왼쪽을 향하고 있으면 좌우 반전
            image.composite_draw(0, 'h', self.x, self.y, 100, 100)
        else:
            image.draw(self.x, self.y, 100, 100)
        Zombie.font.draw(self.x - 10, self.y + 60, f'{self.ball_count}', (0, 0, 255))
        draw_rectangle(*self.get_bb())

    # 바운딩 박스: (left, bottom, right, top)
    def get_bb(self):
        return self.x - 50, self.y - 50, self.x + 50, self.y + 50

    def handle_collision(self, group, other):
        if group == 'zombie:ball':
            self.ball_count += 1
