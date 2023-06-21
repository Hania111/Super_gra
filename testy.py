import pygame
from assets.Apple import Apple
from assets.Wall import Wall
from settings import APPLE_POINTS, level_2_treshold, level_3_treshold, speed_level_1, speed_level_2, speed_level_3
from Player import Player
from sprite_actions import player_apples_collision, player_walls_collision


# tests of Apples
def test_Apple_init():
    x, y = 100, 200
    apple = Apple(x, y)
    assert apple.rect.x == x
    assert apple.rect.y == y

def test_Apple_update():
    player : Player= Player()
    x, y = 100, 200
    apple = Apple(x, y)
    apple.update(player)
    assert apple.rect.y == y + player.step


# tests of walls
def test_Wall_init():
    x, y = 100, 200
    width, height = 50, 20
    wall = Wall(x, y, width, height)
    assert wall.rect.x == x
    assert wall.rect.y == y
    assert wall.rect.width == width
    assert wall.rect.height == height

def test_Wall_update():
    player: Player = Player()
    x, y = 100, 200
    width, height = 50, 20
    wall = Wall(x, y, width, height)
    wall.update(player)
    assert wall.rect.y == y + player.step


# Test of player and apples collision
def test_Apple_eat():
    apples = pygame.sprite.Group()
    player = Player()
    result = player.score + APPLE_POINTS
    apples.add(Apple(player.rect.x, player.rect.y))
    player_apples_collision(player, apples)
    assert result == player.score


# Test of player and wall
def test_collision_walls():
    walls = pygame.sprite.Group()
    player = Player()
    result = player.rect.y
    walls.add(Wall(player.rect.x, player.rect.y-player.step, 10, 10))
    # pygame.event.post(pygame.event.Event(KEYDOWN, key=K_UP))
    # player.move()
    player.rect.y += player.step
    player_walls_collision(player, walls)
    assert player.rect.y == result + player.step

# speed test
def test_speed_1():
    player = Player()
    player.score = level_2_treshold-1
    player.update()
    assert player.step == speed_level_1

def test_speed_2():
    player = Player()
    player.score = level_3_treshold-1
    player.update()
    assert player.step == speed_level_2

def test_speed_3():
    player = Player()
    player.score = level_3_treshold+1
    player.update()
    assert player.step == speed_level_3


