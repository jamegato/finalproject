from dataclasses import dataclass
from designer import *
from random import randint

MINER_SPEED = 50

@dataclass
class World:
    miner: DesignerObject
    miner_speed: int
    foods: list[DesignerObject]
    #rocks: DesignerObject
'''
@dataclass
class Button:
    background: DesignerObject
 
@dataclass
class TitleScreen:
    header: DesignerObject
    start_button: Button
    quit_button: Button
    
 '''
def create_world() -> World:
    "Creates the world containing everything"
    return World(create_miner(), MINER_SPEED, [])

def create_miner() -> DesignerObject:
    """
    Creates the miner, increases his size and also sets
    where he spawns in
    """
    miner = emoji("man")
    set_scale(miner, 2.0)
    miner.y = get_height() * (1 / 1.5)
    miner.flip_x = True
    return miner


def bounce_miner(world: World):
    """
    Sets the boundaries of the miner, and prevents him by going off screen by introducimh
    a bounce feature to block him off
    """
    if world.miner.x > get_width():
        head_left(world)
    elif world.miner.x < 0:
        head_right(world)

def head_left(world: World):
    """ Allows for the miner to move to the left
    also controlls how fast he moves by having
    the * 2 next to the speed
    """
    world.miner_speed = -MINER_SPEED * 2
    world.miner.x += world.miner_speed
    world.miner.flip_x = False


def head_right(world: World):
    """Allows for the miner to move to the right
    also controlls how fast he moves by having
    the * 2 next to the speed
    """
    world.miner_speed = MINER_SPEED * 2
    world.miner.x += world.miner_speed
    world.miner.flip_x = True



def flip_miner(world: World, key: str):
    """ Changes the directions that the miner moves depending on
    which direction key is being pressed.
    """
    if key == "left":
        head_left(world)
    elif key == "right":
        head_right(world)

def create_foods() -> DesignerObject:
    """Create food that spawns around on the same level of
    the miner at random intervals
    """
    food = emoji('🍕')
    food.anchor = 'midbottom'
    food.x = randint(-get_width() / 2, get_width() / 2)
    food.y = get_height() * (1 / 1.4)
    return food

def make_foods(world: World):
    """ Controlls the amount of food being spawned
    around in the game, restricting the amount to 2 max,
    also applying a 1/10 chance for it to spawn
    """
    not_too_many_foods = len(world.foods) < 2
    random_chance = randint(1, 10) == 10
    if (not_too_many_foods and random_chance):
        world.foods.append(create_foods())

#def make_rocks(world: World):
    """ Unfinished Rock function that creates
    the rocks that the miner has to dodge at random
    intervals
    """

when('starting', create_world)
when("updating", bounce_miner)
when("typing", flip_miner)
when("updating", make_foods)
start()