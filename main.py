from dataclasses import dataclass
from designer import *
from random import randint

MINER_SPEED = 50
STARTING_TIME = 60
ROCK_MOVEMENT = 6
ROCK_COUNTER = 6
ROCK_SIZE = 1


@dataclass
class Button:
    background: DesignerObject
    border: DesignerObject
    label: DesignerObject


@dataclass
class GameOverScreen:
    background: DesignerObject
    header: DesignerObject
    score: DesignerObject
    try_again_button: Button
    exit_button: Button


@dataclass
class GameWonScreen:
    background: DesignerObject
    header: DesignerObject
    score: DesignerObject
    play_again_button: Button
    exit_button: Button


@dataclass
class TitleScreen:
    background: DesignerObject
    header: DesignerObject
    start_button: Button
    quit_button: Button
    author_name: DesignerObject


@dataclass
class World:
    background: DesignerObject
    miner: DesignerObject
    miner_speed: int
    food: list[DesignerObject]
    coin: list[DesignerObject]
    rocks: list[DesignerObject]
    mushroom: list[DesignerObject]
    rock_movement: int
    score: int
    score_counter: list[DesignerObject]
    lives: list[DesignerObject]
    unit: int
    seconds: int
    timer: list[DesignerObject]
    rock_count: int
    rock_size: int


def make_button(message: str, x: int, y: int) -> Button:
    """
    Creates a button.

    Args:
        message (str): Message on the button.
        x (int): The x position of the button.
        y (int): The y position of the button.

    Returns:
        Button: A collection of designer objects that forms a button.
    """
    horizontal_padding = 40
    vertical_padding = 14
    label = text("chocolate", message, 30, x, y, layer='top', font_name='Equinox')
    return Button(rectangle("lemonchiffon", label.width + horizontal_padding, label.height + vertical_padding, x, y),
                  rectangle("chocolate", label.width + horizontal_padding, label.height + vertical_padding, x, y, 1),
                  label)


def create_title_screen() -> TitleScreen:
    """
    Creates the title screen.

    Returns:
       TitleScreen: Composed of a background image, header, and two buttons.
    """
    return TitleScreen(background_image("Photos/miner_bg.png"),
                       text("chocolate", "Miner Dance", 60, get_width() / 2, 105, font_name='Equinox'),
                       make_button("Play", get_width() / 2 - 50, 370),
                       make_button("Quit", get_width() / 2 + 50, 370),
                       text("chocolate", "Created By: James Gatonye", 20, get_width() / 2, 500, font_name="Equinox"))


def handle_title_buttons(world: TitleScreen):
    """
    When the buttons of the title screen are clicked, it redirects the user to either the start screen or permits the
    user to quit the game.

    Args:
        world (TitleScreen): Composed of a background image, header, and two buttons.
    """
    if colliding_with_mouse(world.start_button.background):
        change_scene("start")
    if colliding_with_mouse(world.quit_button.background):
        quit()


def create_world() -> World:
    """
    Creates the world that contains everything

    Returns:
        World: The whole world
    """
    return World(create_background(), create_miner(), MINER_SPEED, [], [], [], [],
                 ROCK_MOVEMENT, 0, text("chocolate", "", 35, get_width() / 2, 40, font_name='Equinox'),
                 display_lives([create_heart(), create_heart(), create_heart()])
                 , 0, STARTING_TIME, text("chocolate", "", 30, get_width() / 2, 70, font_name='Equinox'),
                 ROCK_COUNTER, ROCK_SIZE)


def create_background() -> DesignerObject:
    """
    Creates the background image of the volcano for the game

    Return:
        DesignerObject: The background image
    """
    background = image("Photos/background.png")
    return background


def create_miner() -> DesignerObject:
    """
    Creates the miner, increases his size and also sets
    where he spawns in.

    return:
        DesignerObject: Creates the miner image
    """
    miner = image("Photos/miner.png")
    set_scale(miner, 0.5)
    miner.y = get_height() * (1 / 1.5)
    miner.flip_x = True
    return miner


def bounce_miner(world: World):
    """
    Sets the boundaries of the miner, and prevents him by going offscreen by introducing
    a bounce feature to block him off

    Args:
        world (World): The Worlds Instance.
    """
    if world.miner.x > get_width():
        head_left(world)
    elif world.miner.x < 0:
        head_right(world)


def head_left(world: World):
    """
    Allows for the miner to move to the left
    also controls how fast he moves by having
    the * 2 next to the speed.

    Args:
        world (World): The Worlds Instance.
    """
    world.miner_speed = -MINER_SPEED * 2
    world.miner.x += world.miner_speed
    world.miner.flip_x = True


def head_right(world: World):
    """
    Allows for the miner to move to the right
    also controls how fast he moves by having
    the * 2 next to the speed

    Args:
        world (World): The Worlds Instance.
    """
    world.miner_speed = MINER_SPEED * 2
    world.miner.x += world.miner_speed
    world.miner.flip_x = False


def flip_miner(world: World, key: str):
    """
    Changes the directions that the miner moves depending on
    which direction key is being pressed.

    Args:
        world (World): The Worlds Instance.
        key(str): Keyboard Strokes
    """
    if key == "a":
        head_left(world)
    elif key == "d":
        head_right(world)


def create_foods() -> DesignerObject:
    """
    Create food that spawns around on the same level of
    the miner at random intervals

    Return:
        DesignerObject: The imaging for the food that randomly spawns
    """
    food = image("Photos/kit.png")
    food.anchor = 'midbottom'
    food.x = randint(0, get_width())
    food.y = get_height() * (1 / 1.4)
    return food


def create_coins() -> DesignerObject:
    """
    Create coins that spawns around on the same level of
    the miner at random intervals that can be collected

    Return:
        DesignerObject: The imaging for the coins that randomly spawns
    """
    coin = image("Photos/coins.png")
    coin.anchor = 'midbottom'
    coin.x = randint(0, get_width())
    coin.y = get_height() * (1 / 1.4)
    return coin


def create_mushroom() -> DesignerObject:
    """
    Create mushroom powerup that spawns around on the same level of
    the miner at random intervals that can be collected

    Return:
        DesignerObject: The imaging for the mushrooms that randomly spawn
    """
    mushroom = image("Photos/mushroom.png")
    mushroom.anchor = 'midbottom'
    mushroom.x = randint(0, get_width())
    mushroom.y = get_height() * (1 / 1.4)
    return mushroom


def make_foods(world: World):
    """
    Controls the amount of food being spawned
    around in the game, restricting the amount to 2 max,
    also applying a 1/300 chance for it to spawn

    Args:
        world (World): The Worlds Instance.
    """
    not_too_many_foods = len(world.food) < 3
    random_chance = randint(1, 300) == 1
    if (not_too_many_foods and random_chance):
        world.food.append(create_foods())


def make_coins(world: World):
    """
    Controls the amount of coin being spawned
    around in the game, restricting the amount to 1 max,
    also applying a 1/100 chance for it to spawn

    Args:
        world (World): The Worlds Instance.
    """
    not_too_many_coins = len(world.coin) < 2
    random_chance = randint(1, 100) == 1
    if (not_too_many_coins and random_chance):
        world.coin.append(create_coins())


def make_mushroom(world: World):
    """
    Controls the amount of mushrooms being spawned
    around in the game, restricting the amount to 1 max,
    also applying a 1/200 chance for it to spawn

    Args:
        world (World): The Worlds Instance.
    """
    not_too_many_mushrooms = len(world.mushroom) < 1
    random_chance = randint(1, 200) == 1
    if (not_too_many_mushrooms and random_chance):
        world.mushroom.append(create_mushroom())


def eating_food(world: World):
    """
    When the miner touches the food, the miner will
    increase in speed, and also grow bigger

    Args:
        world (World): The Worlds Instance.
    """
    eaten_food = []
    miner = world.miner
    for food in world.food:
        if colliding(food, world.miner):
            eaten_food.append(food)
            miner.scale_x += 0.14
            miner.scale_y += 0.14
            world.miner_speed = world.miner_speed + 2
    world.food = filter_from(world.food, eaten_food)


def collecting_coins(world: World):
    """
    When the miner collects a coin the score
    will update and time will be added.

    Args:
         world (World): The Worlds Instance.
    """
    collected_coins = []
    miner = world.miner
    for coin in world.coin:
        if colliding(coin, world.miner):
            collected_coins.append(coin)
            world.score += 50
    world.coin = filter_from(world.coin, collected_coins)


def eating_mushroom(world: World):
    """
    When the miner touches the mushroom, the miner will
    become smaller

    Args:
        world (World): The Worlds Instance.
    """
    eaten_mushroom = []
    miner = world.miner
    for mushroom in world.mushroom:
        if colliding(mushroom, world.miner):
            eaten_mushroom.append(mushroom)
            miner.scale_x -= 0.05
            miner.scale_y -= 0.05
    world.mushroom = filter_from(world.mushroom, eaten_mushroom)


def create_heart() -> DesignerObject:
    """
    Creates the hearts displayed in the game

    Return:
        DesignerObject: The imaging for the heart that appear on screen
    """
    hearts = emoji("♥")
    hearts.scale_y = 0.8
    hearts.scale_x = 0.8
    hearts.y = 105
    hearts.x = get_width() / 2 - 30
    return hearts


def create_rock(world: World) -> DesignerObject:
    """
    Creates the rocks that fall from the sky at a certain scale

    Return:
        DesignerObject: The imaging for the rocks that randomly spawns
    """
    rock = image("Photos/rock.png")
    rock.scale_x = world.rock_size
    rock.scale_y = world.rock_size
    rock.x = randint(0, get_width())
    rock.y = 0
    return rock


def make_rock(world: World):
    """
    Randomly makes rocks appear on screen, if there is under a certain amount on screen

    Args:
        world (World): The Worlds Instance.
    """
    too_many_rocks = len(world.rocks) < world.rock_count
    rand_chance = randint(1, 100) == 10
    if too_many_rocks and rand_chance:
        world.rocks.append(create_rock(world))


def move_rock(world: World):
    """
    The rock constantly moves downward when spawned
    gets destroyed when hitting the ground.

    Args:
        world (World): The Worlds Instance.
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
    """
     When the rock and miner collide the rock disappears and
    the miner loses a life

    Args:
        world (World): The Worlds Instance.
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
    """
    Removes Collected Items and destroys objects from the screen

    Args:
        old_objects: list[DesignerObject]: The old objects on screen after they have been collected
        destroyed_objects: list([DesignerObject]): Destroys the objects after they have been collected

    Return:
        list([DesignerObject]): Removes the objects from the screen after collision
    """
    objects = []
    for object in old_objects:
        if object in destroyed_objects:
            destroy(object)
        else:
            objects.append(object)
    return objects


def update_score(world: World):
    """
    The game updates the score automatically and displays
    it over time

    Args:
        world (World): The Worlds Instance.
    """
    world.score_counter.text = "Score: " + str(world.score)


def display_lives(lives: list[DesignerObject]) -> list[DesignerObject]:
    """
    Displays the hearts all across the screen

    Args:
        lives (list[DesignerObject]): Displays the number of lives on screen.

    Returns:
        (list[DesignerObject]): Updates the number of lives present on screen.
    """
    lives_screen = []
    offset = 0
    for index, heart in enumerate(lives):
        heart.x = heart.x + offset
        offset = offset + 30
        lives_screen.append(heart)
    return lives_screen


def game_over(world: World):
    """
    Triggers the game end screen whenever the players lives reaches 0,
    this function will continuously check during the duration of the game

    Args:
        world (World): The World's instance.
    """
    no_more_lives = len(world.lives) == 0
    if no_more_lives:
        push_scene("loss", score=world.score)


def game_won(world: World):
    """
    Triggers the game win screen whenever the players time reaches 0,
    this function will continuously check during the duration of the game

    Args:
        world (World): The World's instance.
    """
    no_more_time = world.seconds == 0
    if no_more_time:
        push_scene("win", score=world.score)


def create_game_over_screen(score: int) -> GameOverScreen:
    """
    Creates the game over screen whenever certain conditions are met within
    the games parameters like lives are completely lost

    Args:
        score (int): Player's score.

    Returns:
        GameOverScreen: Composed of a background image, header, game statistics, and a home button.
    """
    return GameOverScreen(background_image("Photos/game_over.png"),
                          text("chocolate", "Game Over!", 60, get_width() / 2, 180, font_name='Equinox'),
                          text("chocolate", "Final Score: " + str(score), 35, get_width() / 2, 245,
                               font_name='Equinox'),
                          make_button("Try Again?", get_width() / 2, 380),
                          make_button("Return to Main Menu", get_width() / 2, 430))


def create_game_won_screen(score: int) -> GameWonScreen:
    """
    Creates the game won screen whenever certain conditions are met within
    the games parameters like time is completely done

    Args:
        score (int): Player's score.

    Returns:
        GameWonScreen: Composed of a background image, header, game statistics, and a home button.
    """
    return GameWonScreen(background_image("Photos/game_win.png"),
                         text("chocolate", "You Win!", 60, get_width() / 2, 180, font_name='Equinox'),
                         text("chocolate", "Final Score: " + str(score), 35, get_width() / 2, 245,
                              font_name='Equinox'),
                         make_button("Play Again?", get_width() / 2, 380),
                         make_button("Return to Main Menu", get_width() / 2, 430))


def handle_game_over_button(world: GameOverScreen):
    """
    When try again button of the end scene is clicked, it redirects the user back to the game scene. User is
    redirected to the title scene when home button is clicked.

    Args:
        world (GameOverScreen): Composed of a background image, header, game statistics, and a home button.
    """
    if colliding_with_mouse(world.try_again_button.background):
        change_scene("start")
    if colliding_with_mouse(world.exit_button.background):
        change_scene("title")


def handle_game_won_button(world: GameWonScreen):
    """
    When try again button of the end scene is clicked, it redirects the user back to the game scene. User is
    redirected to the title scene when home button is clicked.

    Args:
        world (GameWonScreen): Composed of a background image, header, game statistics, and a home button.
    """
    if colliding_with_mouse(world.play_again_button.background):
        change_scene("start")
    if colliding_with_mouse(world.exit_button.background):
        change_scene("title")


def timer_updates(world: World):
    """
    Updates the overall timer of the world

    Args:
        world (World): The Worlds Instance.
    """
    world.unit = world.unit + 1
    if world.unit % 30 == 0:
        world.seconds -= 1
    world.timer.text = "Time Remaining: " + str(world.seconds)


def difficulty_ramp_up(world: World):
    """
    Adds More rocks every 20 seconds inside the game, also
    makes them bigger and harder to dodge by extension. Making the miner also
    move slower in this time interval.

    Args:
        world (World): The Worlds Instance.
    """
    if world.unit % 600 == 0:
        world.rock_count = world.rock_count + 1
        world.rock_movement = world.rock_movement + 2
        world.miner_speed = world.miner_speed - 10
        world.rock_size = world.rock_size + 1


when("starting: title", create_title_screen)
when("clicking: title", handle_title_buttons)
when('starting: start', create_world)
when("updating: start", bounce_miner)
when("typing: start", flip_miner)
when("updating: start", make_foods)
when("updating: start", eating_food)
when("updating: start", make_coins)
when("updating: start", collecting_coins)
when("updating: start", make_mushroom)
when("updating: start", eating_mushroom)
when("updating: start", make_rock)
when("updating: start", move_rock)
when("updating: start", taking_damage)
when("updating: start", update_score)
when("updating: start", timer_updates)
when("updating: start", difficulty_ramp_up)
when("updating: start", game_over)
when("updating: start", game_won)
when("starting: loss", create_game_over_screen)
when("starting: win", create_game_won_screen)
when("clicking: loss", handle_game_over_button)
when("clicking: win", handle_game_won_button)
start()