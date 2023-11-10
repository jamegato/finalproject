from dataclasses import dataclass
from designer import *
from random import randint

MINER_SPEED = 50

@dataclass
class World:
    miner: DesignerObject
    miner_speed: int
    foods: list[DesignerObject]
def create_world() -> World:
    return World(create_miner(), MINER_SPEED, [])

def create_miner() -> DesignerObject:
    miner = emoji("man")
    set_scale(miner, 2.0)
    miner.y = get_height() * (1 / 1.5)
    miner.flip_x = True
    return miner


def bounce_miner(world: World):
    if world.miner.x > get_width():
        head_left(world)
    elif world.miner.x < 0:
        head_right(world)

def head_left(world: World):
    """ Make the miner start moving left """
    world.miner_speed = -MINER_SPEED * 2
    world.miner.x += world.miner_speed
    world.miner.flip_x = False


def head_right(world: World):
    world.miner_speed = MINER_SPEED * 2
    world.miner.x += world.miner_speed
    world.miner.flip_x = True



def flip_miner(world: World, key: str):
    if key == "left":
        head_left(world)
    elif key == "right":
        head_right(world)

def create_foods() -> DesignerObject:
    food = emoji('🍕')
    food.anchor = 'midbottom'
    food.x = randint(-get_width() / 2, get_width() / 2)
    food.y = get_height() * (1 / 1.4)
    return food

def make_foods(world: World):
    not_too_many_foods = len(world.foods) < 2
    random_chance = randint(1, 10) == 10
    if (not_too_many_foods and random_chance):
        world.foods.append(create_foods())

when('starting', create_world)
when("updating", bounce_miner)
when("typing", flip_miner)
when("updating", make_foods)
start()