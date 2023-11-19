from dataclasses import dataclass
from designer import *
from random import randint

MINER_SPEED = 60
STARTING_TIME = 60
ROCK_MOVEMENT = 5


@dataclass
class World:
    miner: DesignerObject
    miner_speed: int
    food: list[DesignerObject]
    coin: list[DesignerObject]
    rocks: list[DesignerObject]
    rock_movement: int
    score: int
    score_counter: list[DesignerObject]
    lives: list[DesignerObject]
    unit: int
    seconds: int
    timer: list[DesignerObject]


def create_world() -> World:
    "Creates the world containing everything"
    return World(create_miner(), MINER_SPEED, [], [], [],
                 ROCK_MOVEMENT, 0, text("black", "", 40, get_width() / 2, 30, font_name='Arial'),
                 display_lives([create_heart(), create_heart(), create_heart()])
                 , 0, STARTING_TIME, text("black", "", 30, get_width() / 2, 70, font_name='Arial'))


def create_miner() -> DesignerObject:
    """
    Creates the miner, increases his size and also sets
    where he spawns in.
    """
    miner = emoji("man")
    set_scale(miner, 2.0)
    miner.y = get_height() * (1 / 1.5)
    miner.flip_x = True
    return miner


def bounce_miner(world: World):
    """
    Sets the boundaries of the miner, and prevents him by going off screen by introducing
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
    world.miner_speed = -MINER_SPEED
    world.miner.x += world.miner_speed
    world.miner.flip_x = False


def head_right(world: World):
    """Allows for the miner to move to the right
    also controlls how fast he moves by having
    the * 2 next to the speed
    """
    world.miner_speed = MINER_SPEED
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
    food.x = randint(0, get_width())
    food.y = get_height() * (1 / 1.4)
    return food


def create_coins() -> DesignerObject:
    """Create coins that spawns around on the same level of
    the miner at random intervals that can be collected
    """
    coin = emoji('🪙')
    coin.anchor = 'midbottom'
    coin.x = randint(0, get_width())
    coin.y = get_height() * (1 / 1.4)
    return coin


def make_foods(world: World):
    """ Controlls the amount of food being spawned
    around in the game, restricting the amount to 2 max,
    also applying a 1/100 chance for it to spawn
    """
    not_too_many_foods = len(world.food) < 3
    random_chance = randint(1, 100) == 1
    if (not_too_many_foods and random_chance):
        world.food.append(create_foods())


def make_coins(world: World):
    """ Controlls the amount of coin being spawned
    around in the game, restricting the amount to 1 max,
    also applying a 1/300 chance for it to spawn
    """
    not_too_many_coins = len(world.coin) < 2
    random_chance = randint(1, 300) == 1
    if (not_too_many_coins and random_chance):
        world.coin.append(create_coins())


def eating_food(world: World):
    """When the miner touches the food, the miner will
    increase in speed, and also grow bigger
    """
    eaten_food = []
    miner = world.miner
    for food in world.food:
        if colliding(food, world.miner):
            eaten_food.append(food)
            miner.scale_x += 0.05
            miner.scale_y += 0.05
    world.food = filter_from(world.food, eaten_food)


def collecting_coins(world: World):
    """When the miner collects a coin the score
    will update and time will be added
    """
    collected_coins = []
    miner = world.miner
    for coin in world.coin:
        if colliding(coin, world.miner):
            collected_coins.append(coin)
            world.score += 20
            world.seconds += 5
    world.coin = filter_from(world.coin, collected_coins)


def create_heart() -> DesignerObject:
    "Creates the hearts displayed in the game"
    hearts = emoji("♥")
    hearts.scale_y = 0.8
    hearts.scale_x = 0.8
    hearts.y = 110
    hearts.x = get_width() / 2 - 30
    return hearts


def create_rock() -> DesignerObject:
    "Creates the rocks that fall from the sky"
    rock = emoji("🪨")
    rock.scale_x = 2
    rock.scale_x = 2
    rock.x = randint(0, get_width())
    rock.y = 0
    return rock


def make_rock(world: World):
    "Randomly makes rocks, upto 3 on screen"
    too_many_rocks = len(world.rocks) < 3
    rand_chance = randint(1, 100) == 10
    if too_many_rocks and rand_chance:
        world.rocks.append(create_rock())


def move_rock(world: World):
    """The rock constantly moves downward when spawned
    gets destroyed when hitting the ground
    """
    kept = []
    for rock in world.rocks:
        rock.y += world.rock_movement
        if rock.y < get_height():
            kept.append(rock)
        else:
            destroy(rock)
    world.rocks = kept


def taking_damage(world: World):
    """ When the rock and miner collide the rock disapears and
    the miner loses a life
    """
    miner = world.miner
    hit_rock = []
    lost_life = []
    for rock in world.rocks:
        if colliding(miner, rock):
            hit_rock.append(rock)
            lost_life.append(world.lives[-1])
    world.rocks = filter_from(world.rocks, hit_rock)
    world.lives = filter_from(world.lives, lost_life)


def filter_from(old_objects: list[DesignerObject], destroyed_objects: list[DesignerObject]) -> list[DesignerObject]:
    "Removes Collected Items and destroys objects"
    objects = []
    for object in old_objects:
        if object in destroyed_objects:
            destroy(object)
        else:
            objects.append(object)
    return objects


def update_score(world: World):
    "Updates the score"
    world.score_counter.text = "Score: " + str(world.score)


def display_lives(lives: list[DesignerObject]):
    "The hearts are going to be displayed across the screen"
    lives_screen = []
    offset = 0
    for index, heart in enumerate(lives):
        heart.x = heart.x + offset
        offset = offset + 30
        lives_screen.append(heart)
    return lives_screen


def timer_updates(world: World):
    "Updates the overall"
    world.unit = world.unit + 1
    if world.unit % 60 == 0:
        world.seconds -= 1
    world.timer.text = "Time Remaining: " + str(world.seconds)


when('starting', create_world)
when("updating", bounce_miner)
when("typing", flip_miner)
when("updating", make_foods)
when("updating", eating_food)
when("updating", make_coins)
when("updating", collecting_coins)
when("updating", make_rock)
when("updating", move_rock)
when("updating", taking_damage)
when("updating", update_score)
when("updating", timer_updates)
start()




